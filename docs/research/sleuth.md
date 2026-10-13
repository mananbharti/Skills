# sleuth - current failure-first research pass

Reviewed 2026-10-14 against commit 66668739d4e3b99aab30bdea9594ca6361072c84.

Ownership: causal debugging; hotpath owns measured performance, proof owns test strategy.

Observed baseline instruction defect: Failed fix was declared proof that the hypothesis is dead; stack direction and 2026 trace/APM assertions were universal.

Changed judgment: Separate failed intervention from rejected prediction; runtime-specific exception order; competing hypotheses only when plausible; observable traces without hidden reasoning.

## Source-to-decision trace

| Source | Organization / version / date | Access | Proposition and exact artifact | Rejected alternative / limit | Refresh |
| --- | --- | --- | --- | --- | --- |
| [Effective Troubleshooting](https://sre.google/sre-book/effective-troubleshooting/) | Google SRE; SRE book chapter; 2016 | fetched 2026-10-14 | Hypothesis-driven observation supports diagnosis, not guaranteed causation. Decision encoded in `skills/sleuth/SKILL.md` (hypotheses/failure handling) and `skills/sleuth/references/techniques.md` (exception/trace interpretation). | No general guarantee or behavioral lift inferred. | source revision, target version, or affected boundary changes |
| [traceback](https://docs.python.org/3/library/traceback.html) | Python Software Foundation; 3.15 documentation; target runtime must be detected; living; retrieved 2026-10-14 | fetched 2026-10-14 | Exception chains and frame order are runtime-specific. Decision encoded in `skills/sleuth/SKILL.md` (hypotheses/failure handling) and `skills/sleuth/references/techniques.md` (exception/trace interpretation). | No general guarantee or behavioral lift inferred. | source revision, target version, or affected boundary changes |
| [Signals](https://opentelemetry.io/docs/concepts/signals/) | OpenTelemetry; current concepts documentation; living; date not established | fetched 2026-10-14 | Traces, logs and metrics are complementary observations. Decision encoded in `skills/sleuth/SKILL.md` (hypotheses/failure handling) and `skills/sleuth/references/techniques.md` (exception/trace interpretation). | No general guarantee or behavioral lift inferred. | source revision, target version, or affected boundary changes |

Each source was opened individually through web access. Dates not shown by a
source are explicitly unknown; retrieval date is not publication date. The
self-contained package retains full source records in its research reference.

## Failure situation register

O = observed instruction defect in this checkout; R = locally reproducible
seeded fixture; S = mechanism described by named primary source; H = original
local evaluation hypothesis, not a reported incident or measured prevalence.
Unmarked rows below are H. These are distinct candidate situations, not fifteen
observed incidents. Replication and agent trials are recorded separately.

1. Failed patch incorrectly kills a still-plausible hypothesis [O: SKILL banned list].
2. Universal bottom-first stack rule mislocates Python throw site [O: techniques].
3. Invented 2026 APM limitation demands hidden reasoning traces [O: techniques].
4. Forced second hypothesis adds theater to deterministic contract defect [O: workflow].
5. Cache returns old value after set [R: sleuth-cache fixture].
6. Timezone change mistaken for data corruption.
7. Logging perturbs race ordering.
8. Sampling hides one failing request.
9. Retry conceals repeated side effect.
10. Bisect classifies skipped build failure as product bad.
11. Wrong release telemetry attributed to candidate.
12. Mitigation reported as causal fix.
13. Production payload copied with PII.
14. A failing test is the defect rather than product.
15. Unreachable upstream dependency prevents replay.

Rejected universal frame direction, hidden model reasoning retrieval, and interpreting a failed intervention as proof that the entire hypothesis is false.

## Validation and evidence boundary

The existing `evals/outcomes/sleuth.md` is UNVERIFIED; its frozen tasks remain
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

# sleuth — research provenance

## Sources that materially changed the skill

| Source | Key lesson | Why it matters | Where encoded |
| --- | --- | --- | --- |
| Agentic Debugging Anti-Patterns (2025/2026) | The "Guess-and-Check" loop is the primary failure mode of autonomous debugging agents, burning tokens without converging on a root cause. | Explicitly bans guess-and-check edits and "Amnesia" (retrying the same failed action), forcing hypothesis-driven elimination instead. | SKILL.md §Banned List |
| Observability Blind Spots in Agentic Systems | Traditional black-box APM tools cannot debug non-deterministic agent workflows. | Adds "Trace-Based Observability" to ensure agents inspect the entire reasoning and tool-call hierarchy when debugging orchestrations. | references/techniques.md |
| Hallucinated Fixes | Agents without strict runtime grounding default to suggesting plausible but incorrect structural patches. | Bans suggesting any fix before gathering runtime evidence (logs, DB state). | SKILL.md §Banned List |
| v1 campaign audit, Phase 16 (2026-09-14) | All three traces verified encoded; gaps are the missing Prerequisites and Tool selection/fallback sections (repro access assumed, debugger→prints→static ladder unstated) | Prerequisites (code + runnable path + evidence sources) and Tool selection/fallback sections | SKILL.md (Prerequisites, Tool selection/fallback) |

## Key new intelligence encoded

1. **Anti-Amnesia / Action Fingerprinting** — bans the agent from repeatedly trying identical or trivially tweaked fixes that have already failed, forcing it to kill the underlying hypothesis instead.
2. **Trace-Based Observability** — directs the debugging effort away from shallow HTTP responses and toward deep LLM reasoning traces when diagnosing modern orchestrated systems.
3. **The Banned List** — formalizes the rejection of the "vibe debugging" behaviors that make LLMs untrustworthy maintainers.

## Fast-moving items

| Topic | Source/version/date |
| --- | --- |
| Agent state observability | OpenTelemetry for LLM traces (2026 standards) |

## Dated evaluator conflict - 2026-10-14

Historical SL1 requires two hypotheses even for conclusive deterministic evidence. The current skill requires plausible rivals, not manufactured alternatives; retain historical rubric and adjudicate this confound independently.

## Verification 2026-10-14

| Basis | Outcome |
| --- | --- |
| git-bisect manual + SEC 2013-222; fetched 2026-10-14 | Bisect exit-125/skip constraints; Knight dead-code/alerts case in environment bugs. |
