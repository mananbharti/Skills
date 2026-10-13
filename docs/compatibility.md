# Cross-agent compatibility matrix

**Portability is an empirical claim, not a format assumption.** Cells are
filled only from actual tests or clearly-labeled research, never from
"the Agent Skills format is theoretically portable".

Status semantics:

- ✅ **tested**: executed against a live agent, date recorded
- ◐ **supported with fallback**: works, but degraded vs the primary path
- ? **unverified**: researched/documented, not yet executed here
- — **unavailable**: not installed / no headless capability found

## Local probe results (2026-09-14)

| Agent | Installed | Version | Headless invocation | Routing eval |
| --- | --- | --- | --- | --- |
| Codex | yes | 0.153.4 (gpt-5.6-sol) | ✅ tested (`codex exec`, stdin closed) | ✅ measured — smoke 0.917 accuracy (11/12), 2026-09-14 |
| OpenCode | yes | 1.18.30 | ✅ tested (`opencode run`) | ✅ measured — smoke 1.0 accuracy (12/12), 2026-09-14 |
| Claude Code | yes | 2.1.235 | ? flags documented; **execution hangs in dev env** | ? — pending a working environment |
| Cursor | no | — | — | — unavailable locally |
| Antigravity | no | — | — | — unavailable locally |

## Capability matrix (by agent, when installed)

| Capability | Claude Code | Codex | OpenCode | Cursor | Antigravity |
| --- | --- | --- | --- | --- | --- |
| Skill discovery (skills CLI) | ◐ tested | ? | ? | ? | ? |
| Filesystem | ? | ? | ? | ? | ? |
| Shell | ? | ? | ? | ? | ? |
| Web research | ? | ? | ? | ? | ? |
| Browser automation | ? | ? | ? | ? | ? |
| Subagents | ? | ? | ? | ? | ? |
| Structured output | ? (JSON mode documented, execution hung) | ? | ? | ? | ? |
| Token telemetry | ? | ? | ? | ? | ? |
| GitHub CLI passthrough | ? | ? | ? | ? | ? |
| Artifacts on disk | ? | ? | ? | ? | ? |

The skills themselves are Tier A/B portable by design (pure Markdown +
references; deterministic standard-library scripts; graceful capability
fallbacks in `shared/capability-map/`), but **design intent is not measured
compatibility**. Unknown cells remain unknown until a future proof pass runs the
specific agent/capability and records the date. They do not make the runtime
implementation incomplete.

## Installation compatibility (measured 2026-09-14)

- `npx skills add udaysharmadev/Skills --all -y` was verified on
  2026-09-14: a clean-directory install yielded all 28 folders under
  `./.agents/skills/`, including `handsfree`; see C-004 in
  [claims.md](claims.md).
- Interactive single-skill install (`npx skills add udaysharmadev/Skills`):
  same CLI, selection mode; discovery verified, interactive flow
  exercised manually.

The command is verified. The live skills.sh listing and badge status remain
unverified until the public listing can be checked directly.

## Current packaging observations, 2026-10-14

These observations supplement the historical runtime table; no historical
result is silently updated to a current-model pass.

| Check | Observed result | Evidence / limit |
| --- | --- | --- |
| Public `udaysharmadev/Skills --all --yes`, CLI 1.7.2 | PASS: 28 skill folders | [Raw install record](upgrade/evidence/install-public.json); public default branch, not this unpushed implementation |
| Each selected local package, `--agent codex --copy --yes` | PASS on final package snapshot | [Final 28 install manifests](upgrade/evidence/install-individual-final.json); each file and executable bit checked; interim manifests retained separately |
| Standalone offline copies | PASS: 28 copies | [Final checks](upgrade/evidence/final-checks.json); no host discovery or model execution implied |
| Native Codex / Claude / OpenCode / Cursor / Antigravity / Gemini activation | UNVERIFIED for this upgrade | No current live campaign executed; old observations retain their dates |
| Linux / Windows package execution | UNVERIFIED locally | CI adds offline copies on Ubuntu; configured CI is not an observed CI result |
| Current interactive CLI selection | UNVERIFIED | Historical manual evidence only |

Reproduce individual checks with the installed, pinned official CLI:

```bash
scripts/check-packages --cli /path/to/skills/bin/cli.mjs --output /tmp/install.json
```

The default `scripts/check-packages` path is offline. The optional CLI path
performs only owned disposable project installs, disables CLI telemetry and
never invokes a coding agent. The initial registry query failed under the
network sandbox; a host-approved registry query/download then succeeded.

Current read-only [CLI probe](upgrade/evidence/runtime-probe.json): Claude Code
2.1.235 and Codex CLI 0.153.4 are present; OpenCode's binary resolves but its
version output was empty; Cursor/Antigravity binaries do not resolve. The
probe's “verified” adapter column is historical configuration metadata, not a
fresh invocation or activation result. Gemini CLI was not probed. None of these
presence observations fills a current behavior-compatibility cell.
