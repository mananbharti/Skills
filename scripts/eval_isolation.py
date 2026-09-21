#!/usr/bin/env python3
"""eval_isolation — documented, run-scoped experiment isolation helpers.

All mechanisms below are documented vendor behavior; no invented flags,
no global-settings modification:

- Skill-tool denial: OPENCODE_CONFIG_CONTENT (inline runtime overrides,
  https://opencode.ai/docs/config#custom-path) merges
  {"permission": {"skill": {"*": "deny"}}} (deny = hidden from agent,
  access rejected, https://opencode.ai/docs/skills#configure-permissions).
  Run-scoped environment variable: the user's global config is untouched.
  The treatment arm is unaffected: the evaluated skill travels as prompt
  text plus a `.eval-skill/` helper directory, neither of which is a
  skill-discovery location, so helpers stay reachable via shell.
- Project skills: OpenCode walks up from the cwd to the git worktree for
  `.opencode/skills`, `.claude/skills`, `.agents/skills`. Runner workdirs
  are fresh disposable directories that are `git init`-ed before the agent
  starts, so discovery stops at the workdir. `workdir_skill_check`
  asserts no discovery-location skill directory exists inside.
- Sessions: runners never pass --continue/--session, so every invocation
  starts a fresh session (state accumulates under the user's data dir but
  is never continued across trials).

Empirically verified WITHOUT any model call (Phase 1):
- `opencode debug skill` lists global skills (archify, gravitas,
  gravitas-python, gravitas-typescript) from ~/.agents/skills with full
  content paths: contamination is real, denial is necessary.
- `OPENCODE_CONFIG_CONTENT='{"permission":{"skill":{"*":"deny"}}}'`
  `opencode debug config` shows the permission merge in resolved config.

EXPLICIT LIMITATION: runtime hiding (the agent actually being unable to
load a global skill mid-run) is only observable in a live model trace,
which harness-plumbing work does not run. Records therefore carry
isolation.verified = "config-merge" until a live run demonstrates
otherwise. Nothing here disables provider authentication or invents a
`--pure`-style flag: `--pure` (no external plugins) exists but is NOT
set by the harness because its interaction with provider auth cannot be
verified without spending a model call.
"""
import hashlib
import json
import os
import subprocess
from pathlib import Path

# Deny-list for the agent's native skill tool, applied equally to both
# experimental arms. Prompt-supplied skill text is unaffected.
SKILL_DENY_ALL = {"permission": {"skill": {"*": "deny"}}}

# Documented global skill-discovery locations (opencode.ai/docs/skills).
GLOBAL_SKILL_DIRS = [
    os.path.expanduser("~/.config/opencode/skills"),
    os.path.expanduser("~/.claude/skills"),
    os.path.expanduser("~/.agents/skills"),
]

# Project discovery directory names, relative to a workdir.
PROJECT_SKILL_DIRNAMES = (
    os.path.join(".opencode", "skills"),
    os.path.join(".claude", "skills"),
    os.path.join(".agents", "skills"),
)

ISOLATION_VERIFIED = "config-merge"


def isolation_env(agent):
    """Run-scoped environment overlay for an agent invocation.

    Only the opencode adapter has a documented inline-override mechanism;
    other adapters get no overlay (recorded as such in provenance).
    """
    if agent == "opencode":
        return {"OPENCODE_CONFIG_CONTENT": json.dumps(SKILL_DENY_ALL)}
    return {}


def global_skill_manifest():
    """Names (not contents) of globally installed skills per location."""
    manifest = {}
    for location in GLOBAL_SKILL_DIRS:
        try:
            names = sorted(
                d for d in os.listdir(location)
                if os.path.isdir(os.path.join(location, d))
            )
        except OSError:
            names = []
        manifest[location] = names
    return manifest


def workdir_skill_check(workdir):
    """Return discovery-location skill dirs found inside workdir (want [])."""
    found = []
    root = Path(workdir)
    for rel in PROJECT_SKILL_DIRNAMES:
        candidate = root / rel
        try:
            if candidate.is_dir() and any(candidate.iterdir()):
                found.append(rel)
        except OSError:
            continue
    return found


def isolation_record(agent, workdir=None):
    """Provenance-ready isolation block. No secrets collected."""
    record = {
        "skill_tool": (
            "deny-all via OPENCODE_CONFIG_CONTENT (run-scoped, documented)"
            if agent == "opencode"
            else "no documented run-scoped skill isolation for this adapter"
        ),
        "verified": ISOLATION_VERIFIED if agent == "opencode" else "none",
        "global_skills": global_skill_manifest() if agent == "opencode" else {},
        "session": "fresh (runners never pass --continue/--session)",
        "workdir_own_worktree": bool(workdir and (Path(workdir) / ".git").exists()),
        "workdir_skill_dirs": workdir_skill_check(workdir) if workdir else "unchecked",
    }
    return record


def _git(root, *args):
    try:
        result = subprocess.run(
            ["git", *args], capture_output=True, text=True, cwd=root, timeout=30
        )
    except (OSError, subprocess.TimeoutExpired):
        return None
    return result.stdout.strip() if result.returncode == 0 else None


def runner_dependencies(root):
    """sha256 of the shared runner helper modules every record depends on.

    Catches the Phase-4 blind spot: repo provenance hashed the diff but a
    helper added while dirty (e.g. this file) left no per-record trace.
    """
    deps = {}
    for name in ("eval_guard.py", "eval_isolation.py"):
        try:
            deps[name] = hashlib.sha256(
                (Path(root) / "scripts" / name).read_bytes()).hexdigest()
        except OSError:
            deps[name] = "unknown"
    return deps


def untracked_state(root, max_files=200, max_bytes=2_000_000):
    """Bounded digest of untracked non-ignored repository state.

    Records relative names, sizes, and content hashes plus an overall
    digest — never contents, credentials, or absolute local paths.
    Ignored paths (evals/results/, node_modules, caches) are excluded by
    git itself via --exclude-standard.
    """
    try:
        proc = subprocess.run(
            ["git", "ls-files", "--others", "--exclude-standard", "-z"],
            capture_output=True, text=True, cwd=root, timeout=30)
    except (OSError, subprocess.TimeoutExpired):
        return {"available": False}
    if proc.returncode != 0:
        return {"available": False}
    names = sorted(name for name in proc.stdout.split("\0") if name)
    truncated = len(names) > max_files
    files = []
    digest = hashlib.sha256()
    for rel in names[:max_files]:
        candidate = Path(root) / rel
        try:
            data = (candidate.read_bytes()
                    if candidate.is_file() and not candidate.is_symlink()
                    else None)
        except OSError:
            data = None
        if data is None:
            entry = {"path": rel, "bytes": None, "sha256": "unreadable"}
        elif len(data) > max_bytes:
            entry = {"path": rel, "bytes": len(data),
                     "sha256": "skipped-too-large"}
        else:
            entry = {"path": rel, "bytes": len(data),
                     "sha256": hashlib.sha256(data).hexdigest()}
        files.append(entry)
        digest.update(json.dumps(entry, sort_keys=True).encode() + b";")
    return {"available": True, "count": len(names), "truncated": truncated,
            "files": files, "digest": digest.hexdigest()}


def repo_provenance(root, runner_path):
    """Immutable commit/dirty provenance. Stores HASHES, never content."""
    commit_full = _git(root, "rev-parse", "HEAD") or "unknown"
    status = _git(root, "status", "--porcelain") or ""
    diff_proc = subprocess.run(
        ["git", "diff", "--binary", "HEAD"],
        capture_output=True, cwd=root, timeout=60,
    )
    diff_bytes = diff_proc.stdout if diff_proc.returncode == 0 else b""
    try:
        runner_sha = hashlib.sha256(Path(runner_path).read_bytes()).hexdigest()
    except OSError:
        runner_sha = "unknown"
    return {
        "commit_full": commit_full,
        "commit_short": commit_full[:7] if commit_full != "unknown" else "unknown",
        "working_tree_dirty": bool(status.strip()),
        "working_tree_diff_sha256": hashlib.sha256(diff_bytes).hexdigest(),
        "runner_sha256": runner_sha,
        "runner_deps": runner_dependencies(root),
        "untracked": untracked_state(root),
    }


def dir_manifest(path, max_files=1000, max_bytes=2_000_000):
    """Hash every file under path. Caps keep giant trees bounded.

    Returns {"files": [{path, bytes, sha256}], "digest": overall}.
    Files over max_bytes are size-recorded, not hashed.
    """
    root = Path(path)
    files = []
    if root.is_file():
        candidates = [root]
        base = root.parent
    else:
        base = root
        candidates = sorted(p for p in root.rglob("*") if p.is_file())
    truncated = len(candidates) > max_files
    digest = hashlib.sha256()
    for candidate in candidates[:max_files]:
        try:
            data = candidate.read_bytes()
        except OSError:
            continue
        rel = str(candidate.relative_to(base))
        if len(data) > max_bytes:
            files.append({"path": rel, "bytes": len(data), "sha256": "skipped-too-large"})
            digest.update(rel.encode() + b":skipped-too-large;")
            continue
        file_sha = hashlib.sha256(data).hexdigest()
        files.append({"path": rel, "bytes": len(data), "sha256": file_sha})
        digest.update(rel.encode() + b":" + file_sha.encode() + b";")
    return {"files": files, "digest": digest.hexdigest(), "truncated": truncated}
