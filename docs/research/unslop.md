# unslop - current failure-first research pass

Reviewed 2026-10-14 against commit 66668739d4e3b99aab30bdea9594ca6361072c84.

Ownership: behavior-preserving structure cleanup; sleuth owns bug fix, polish owns appearance.

Observed baseline instruction defect: No tests means no detox contradicted characterization fallback; any red suite forced revert; net-negative lines treated as target; single implementation assumed pointless.

Changed judgment: Bounded characterization and unchanged failing baseline allowed; scope rollback; line delta informational; preserve lifecycle, compatibility and integration seams.

## Source-to-decision trace

| Source | Organization / version / date | Access | Proposition and exact artifact | Rejected alternative / limit | Refresh |
| --- | --- | --- | --- | --- | --- |
| [Refactoring](https://refactoring.com/) | Martin Fowler; current catalog overview; living; date not established | fetched 2026-10-14 | Refactoring changes structure while preserving observable behavior. Decision encoded in `skills/unslop/SKILL.md` (baseline and metrics) and `skills/unslop/references/slop-catalog.md` (intentional seams). | No general guarantee or behavioral lift inferred. | source revision, target version, or affected boundary changes |
| [importlib](https://docs.python.org/3/library/importlib.html) | Python Software Foundation; 3.15 documentation; target runtime detected; living; retrieved 2026-10-14 | fetched 2026-10-14 | Programmatic imports can make text-search absence misleading. Decision encoded in `skills/unslop/SKILL.md` (baseline and metrics) and `skills/unslop/references/slop-catalog.md` (intentional seams). | No general guarantee or behavioral lift inferred. | source revision, target version, or affected boundary changes |

Each source was opened individually through web access. Dates not shown by a
source are explicitly unknown; retrieval date is not publication date. The
self-contained package retains full source records in its research reference.

## Failure situation register

O = observed instruction defect in this checkout; R = locally reproducible
seeded fixture; S = mechanism described by named primary source; H = original
local evaluation hypothesis, not a reported incident or measured prevalence.
Unmarked rows below are H. These are distinct candidate situations, not fifteen
observed incidents. Replication and agent trials are recorded separately.

1. Formal suite required despite allowed smoke characterization [O: SKILL rules].
2. Pre-existing unrelated failure blocks bounded batch [O: SKILL rules].
3. Line-count reduction rewards risky deletion [O: workflow].
4. One implementation treated as proof interface is pointless [O: slop catalog].
5. Legacy pipe export is load-bearing [R: unslop-shop tests].
6. Dynamic plugin appears unused in static imports.
7. Import order changes singleton initialization.
8. Wrapper removal drops cancellation.
9. Consolidation changes error ordering.
10. Dependency needed by code generator removed.
11. Generated file edited rather than generator.
12. Game tick extraction changes ordering.
13. Refactor alters serialized public names.
14. Existing user edits lost by rollback.
15. Swallowed error changed under cleanup without product decision.

Rejected forced net-negative lines, automatic removal of one-provider seams, and whole-tree rollback after a bounded batch failure.

## Validation and evidence boundary

The existing `evals/outcomes/unslop.md` is UNVERIFIED; its frozen tasks remain
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

# unslop — research provenance

## Sources that materially changed the skill

| Source | Key lesson | Why it matters | Where encoded |
| --- | --- | --- | --- |
| Agentic Codebase Mess Patterns (2025/2026) | "AI Sprawl" occurs because it is cognitively cheaper for an agent's context window to accrete new parallel files than to refactor existing ones. | Adds "AI Sprawl (Accretion by Avoidance)" to the slop catalog to force consolidation. | references/slop-catalog.md |
| Zombie Abstractions | Agents trained on 2015-era enterprise Java patterns tend to hallucinate strategy patterns and abstract base classes for single-implementation functions. | Renames "Premature abstractions" to "Zombie abstractions," directing the agent to flatten these AI-hallucinated layers. | references/slop-catalog.md |
| The Refactor Loop of Death | Agents instructed to "clean up this code" without a behavioral baseline will successfully produce pristine, bug-free code that has completely lost its business logic. | Adds the explicit warning against the "Refactor Loop of Death," making tests a hard prerequisite for any detox operation. | SKILL.md §Rules |
| v1 campaign audit, Phase 20 (2026-09-14) | All three traces verified encoded; only gap is the missing Tool selection/fallback section (runner → smoke-baseline → no-signal-no-detox ladder lived in workflow/rules only) | Tool selection/fallback section consolidating the three signal rungs | SKILL.md (Tool selection/fallback) |

## Key new intelligence encoded

1. **AI Sprawl Diagnosis** — recognizes that unslop's main job is reversing the agentic tendency to write net-new code instead of modifying the old.
2. **Zombie Abstraction Removal** — targets the specific architectural hallucinations (unnecessary interfaces/managers) introduced by AI models.
3. **The Refactor Loop of Death** — enforces the rule that syntactic cleanup without behavioral verification is destruction.

## Fast-moving items

| Topic | Source/version/date |
| --- | --- |
| LLM code-accretion benchmarks | Context-window bloat studies (2026) |

## Dated evaluator conflict - 2026-10-14

Historical UN1 requires net-negative lines; current line delta is informational. Preserve historical rubric, but a successful behavior-preserving extraction may add characterization lines and still be useful.

## Independent review follow-through - 2026-10-14

Independent review found mandatory per-batch commits and universal green/browser gates contradicted safe dirty-state handling and the bounded-baseline rule. Checkpoints now preserve task changes and user index/worktree state; commits require authorization, and applicable checks distinguish pre-existing failure from regression. Trace: skills/unslop/SKILL.md batch step 3 and Quality gates.

This is an observed contract contradiction and correction, not a comparative
result. New forward trials have separate retained evidence and do not regrade
historical task outputs.
