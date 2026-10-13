# frugal - current failure-first research pass

Reviewed 2026-10-14 against commit 66668739d4e3b99aab30bdea9594ca6361072c84.

Ownership: context and successful-task cost; recall owns durable memory, hotpath owns app performance.

Observed baseline instruction defect: Retry automatically declared a loss; double retry count assumed erases saving; KPI lacked aggregate failed-task denominator.

Changed judgment: Compute all-attempt cost per independently correct task; unknown usage stays unknown; invalidate stale summaries and preserve producer exit status under output caps.

## Source-to-decision trace

| Source | Organization / version / date | Access | Proposition and exact artifact | Rejected alternative / limit | Refresh |
| --- | --- | --- | --- | --- | --- |
| [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | Anthropic; engineering article; 2025-09-29 | fetched 2026-10-14 | Select relevant context and retain high-signal state; this is not proof of cost savings. Decision encoded in `skills/frugal/references/measurement.md` (cost denominator/invalidation), `skills/frugal/SKILL.md` (routing) and `skills/frugal/scripts/cost-report.py` (observed arithmetic). | No general guarantee or behavioral lift inferred. | source revision, target version, or affected boundary changes |

Each source was opened individually through web access. Dates not shown by a
source are explicitly unknown; retrieval date is not publication date. The
self-contained package retains full source records in its research reference.

## Failure situation register

O = observed instruction defect in this checkout; R = locally reproducible
seeded fixture; S = mechanism described by named primary source; H = original
local evaluation hypothesis, not a reported incident or measured prevalence.
Unmarked rows below are H. These are distinct candidate situations, not fifteen
observed incidents. Replication and agent trials are recorded separately.

1. Any retry treated as automatic cost regression [O: measurement].
2. Doubled retries claimed to erase all savings [O: SKILL].
3. Failed tasks can disappear from successful-task cost [O: missing aggregate method].
4. Zero success denominator could imply zero cost [H: arithmetic guard].
5. Byte reduction confused with provider tokens [O: protected existing categories].
6. Cache read pricing omitted from currency total.
7. Model switch compared as same intervention.
8. Summary remains after source edit.
9. Output head succeeds while tests fail.
10. Truncated log drops only failure.
11. Compaction loses authorization constraint.
12. Pointer inaccessible to receiving worker.
13. Task-critical stack chain overcompressed.
14. Parallel handoffs cost more than local lookup.
15. Empty telemetry fabricated as measured savings.

Rejected fewer tokens or retries alone as a cost conclusion; an intervention must preserve independent correctness and include all attempt costs.

## Validation and evidence boundary

The existing `evals/outcomes/frugal.md` is UNVERIFIED; its frozen tasks remain
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

# frugal — research provenance

## Sources that materially changed the skill

| Source | Key lesson | Why it matters | Where encoded |
| --- | --- | --- | --- |
| Context Engineering Anti-Patterns (2025/2026) | "Context Dumping" degrades model reasoning ("Lost in the Middle") and burns tokens unnecessarily when standard CLI tools could have filtered the data first. | Bans "Context Dumping (Blind Ingestion)", enforcing the use of `grep`, `jq`, and `awk` before reading data into the window. | SKILL.md §Banned List |
| Lossy Compression in Memory | Aggressively summarizing logs or traces to save tokens destroys the exact structural identifiers (line numbers, IDs) needed to actually solve the problem. | Bans "Lossy Compression," establishing that diagnostic payloads must never be destructively summarized. | SKILL.md §Banned List |
| Chatty Reasoning overhead | Outputting extensive "thinking" paragraphs directly to the user wastes output tokens and clutters the session. | Bans "Chatty Reasoning", forcing compactness. | SKILL.md §Banned List |
| v1 campaign audit, Phase 24 (2026-09-14) | All three traces verified encoded; gaps are the missing Prerequisites and Tool selection/fallback sections (gate-first assumed, telemetry→proxy→unknown ladder lived in the reference only) | Prerequisites (task + gate + signal) and Tool selection/fallback sections | SKILL.md (Prerequisites, Tool selection/fallback) |

## Key new intelligence encoded

1. **ContextOps / Context Engineering** — shifts the paradigm from "infinite context" to "selective injection," recognizing that large context windows are a liability if filled with noise.
2. **Preservation of Diagnostics** — creates a hard boundary on token optimization: you may compact prose, but you may never compress a stack trace.

## Fast-moving items

| Topic | Source/version/date |
| --- | --- |
| LLM Context Limits | "Lost in the Middle" degradation benchmarks (2026) |

## Verification 2026-10-14

| Basis | Outcome |
| --- | --- |
| Anthropic prompt-caching docs reviewed 2026-10-13, not independently re-fetched | Cache-prefix mechanics reviewed but not encoded (provider-specific; skill is universal). No change. |
