# janitor - current failure-first research pass

Reviewed 2026-10-14 against commit 66668739d4e3b99aab30bdea9594ca6361072c84.

Ownership: Git state and repository metadata hygiene; frontpage owns prose, harden handles secret incident.

Observed baseline instruction defect: Orphan-looking name called litter; broken multiline for-each-ref command; main assumed; dirty/ignored preservation not operationalized; local authorization unnecessarily reset.

Changed judgment: Snapshot staged/unstaged/untracked/ignored boundaries and attached worktrees; path-scoped dry-run; preserve prior scope authorization; candidate branch never classified from name/age alone.

## Source-to-decision trace

| Source | Organization / version / date | Access | Proposition and exact artifact | Rejected alternative / limit | Refresh |
| --- | --- | --- | --- | --- | --- |
| [git-status](https://git-scm.com/docs/git-status) | Git project; local Git version recorded separately; living; manual shows 2.53.0 update | fetched 2026-10-14 | Porcelain separates index/worktree state; ignored files require explicit inspection. Decision encoded in `skills/janitor/SKILL.md` (authorization/candidates), `skills/janitor/references/maintenance-protocol.md` (dirty state) and `skills/janitor/references/hygiene-checklists.md` (commands). | No general guarantee or behavioral lift inferred. | source revision, target version, or affected boundary changes |
| [git-clean](https://git-scm.com/docs/git-clean) | Git project; current manual; verify local help; living; date not established | fetched 2026-10-14 | Dry-run lists deletion candidates; ignored files can be included by destructive options. Decision encoded in `skills/janitor/SKILL.md` (authorization/candidates), `skills/janitor/references/maintenance-protocol.md` (dirty state) and `skills/janitor/references/hygiene-checklists.md` (commands). | No general guarantee or behavioral lift inferred. | source revision, target version, or affected boundary changes |
| [git-worktree](https://git-scm.com/docs/git-worktree) | Git project; current manual; living; date not established | fetched 2026-10-14 | Branches can be attached to other checkouts. Decision encoded in `skills/janitor/SKILL.md` (authorization/candidates), `skills/janitor/references/maintenance-protocol.md` (dirty state) and `skills/janitor/references/hygiene-checklists.md` (commands). | No general guarantee or behavioral lift inferred. | source revision, target version, or affected boundary changes |

Each source was opened individually through web access. Dates not shown by a
source are explicitly unknown; retrieval date is not publication date. The
self-contained package retains full source records in its research reference.

## Failure situation register

O = observed instruction defect in this checkout; R = locally reproducible
seeded fixture; S = mechanism described by named primary source; H = original
local evaluation hypothesis, not a reported incident or measured prevalence.
Unmarked rows below are H. These are distinct candidate situations, not fifteen
observed incidents. Replication and agent trials are recorded separately.

1. Agent-looking branch name treated as disposable [O: banned list].
2. Broken for-each-ref newline is not runnable shell [O: hygiene checklist].
3. Main assumed although default branch differs [O: hygiene checklist].
4. Ignored file omitted from ordinary status [S: git-status].
5. Staged and unstaged edits coexist [S: git-status].
6. Untracked file contains important source.
7. Merged branch has attached worktree.
8. Remote tracking ref stale without fetch.
9. Branch shared with open review unseen offline.
10. Secret removal from tree mistaken for revocation.
11. Add-all stages another worker changes.
12. Clean dry-run mistaken for authority.
13. Stash obscures user work and ignored files.
14. Malicious issue supplies shell cleanup command.
15. Force-push target changes after inspection.

Rejected deleting branches from agent-like names/merged state and treating ignored files as disposable.

## Validation and evidence boundary

The existing `evals/outcomes/janitor.md` is UNVERIFIED; its frozen tasks remain
unchanged. The workflow cases retain the original five and add five specific
negative/adverse/cross-stack/recovery cases. Authorship is coverage design, not
a behavioral pass. Deterministic outputs and source access are recorded in
`docs/upgrade/safety-shipping.json`. No live agent CLI, paid campaign, public
publication, security scan guarantee, ranking result, or deployment is implied.

Preserved: substantial existing purpose, modes, authority, verification, and
output contracts were already useful; no wholesale rewrite. Rejected: replacing
the package with a generic checklist, adding stack names without adapters, or
counting fixture arithmetic as independent agent effectiveness.

Research-depth gaps: this pass verifies relevant primary documentation and
local implementation evidence. It does not complete five independent source
perspectives, 8-15 sources, skill-specific Reddit/X interviews, a systematic
skills.sh leaderboard audit, or new empirical comparison. Those dimensions
remain pending; no invented source titles or prevalence are used as evidence.

## Historical provenance notes (retained, not refreshed evidence)

The older notes below contain unsourced labels such as agentic anti-pattern
reports and generic 2026 studies. Treat these as historical local hypotheses,
not bibliographic evidence. Current corrections above supersede contradictory
claims below; historical results and frozen rubrics are not regraded.

# janitor — research provenance

## Sources that materially changed the skill

| Source | Key lesson | Why it matters | Where encoded |
| --- | --- | --- | --- |
| Agentic Git Anti-Patterns (2025/2026) | Autonomous agents create "multi-concern" changes and squash them into single commits, destroying the atomic history necessary for bisecting regressions. | Bans "Blind Squashing" and mandates atomic commits by concern. | SKILL.md §Banned List |
| AI Branch Sprawl | Rapid agentic experimentation litters repositories with abandoned, unmerged branches, confusing automated tooling and humans alike. | Adds "Orphaned Branch Sprawl" to the Banned List and hygiene checklist as a primary cleanup target. | SKILL.md §Banned List, references/hygiene-checklists.md |
| Commit Message Vibe Coding | Agents summarize the diff line-by-line rather than explaining the architectural intent, rendering the git log useless for RCA. | Forbids diff narration in favor of business intent ("Why > what"). | SKILL.md §Banned List |
| v1 campaign audit, Phase 21 (2026-09-14) | All three traces verified encoded; gaps are the missing Prerequisites and Tool selection/fallback sections (repo assumed, gh-probe ladder lived in modes only) | Prerequisites (repo + conditional gh) and Tool selection/fallback sections | SKILL.md (Prerequisites, Tool selection/fallback) |

## Key new intelligence encoded

1. **Context Preservation** — forces agents to respect the repository's history by breaking down large, generated code blocks into atomic commits.
2. **AI Sprawl Cleanup** — directs the agent to actively hunt down and propose the deletion of abandoned experimental branches created by other agents.
3. **Intent-Driven Commit Messages** — halts the practice of LLM-generated diff narration in favor of writing the missing "why" context.

## Fast-moving items

| Topic | Source/version/date |
| --- | --- |
| Agent-assisted PR automation | Structured PR generation (2026) |

## Dated evaluator conflict - 2026-10-14

Historical JN5 and frozen outcome O3 require a second explicit yes despite the request already naming squash/force-push. This conflates missing remote/precondition authority with repeated consent. Preserve the rubric for historical comparison, but independently adjudicate authorization semantics before a new campaign. JN2 also uses a fixed 50-character title gate not supported by repository convention.
