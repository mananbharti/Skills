# referee - current failure-first research pass

Reviewed 2026-10-14 against commit 66668739d4e3b99aab30bdea9594ca6361072c84.

Ownership: actionable independent diff review; harden owns deep security, proof owns test strategy.

Observed baseline instruction defect: Major findings defined as should-not-merge yet verdict allowed majors forward; simpler alternative automatically major; missing criteria stopped all review.

Changed judgment: Require changes for merge-blocking majors; factual cost before complexity severity; recover intent while continuing bounded correctness review; recovery need not be down migration.

## Source-to-decision trace

| Source | Organization / version / date | Access | Proposition and exact artifact | Rejected alternative / limit | Refresh |
| --- | --- | --- | --- | --- | --- |
| [What to look for in a code review](https://google.github.io/eng-practices/review/reviewer/looking-for.html) | Google; current engineering practices; living; date not established | fetched 2026-10-14 | Functionality, tests and context matter; personal style preferences do not block. Decision encoded in `skills/referee/SKILL.md` (prerequisites/verdict) and `skills/referee/references/finding-format.md` (severity/recovery). | No general guarantee or behavioral lift inferred. | source revision, target version, or affected boundary changes |

Each source was opened individually through web access. Dates not shown by a
source are explicitly unknown; retrieval date is not publication date. The
self-contained package retains full source records in its research reference.

## Failure situation register

O = observed instruction defect in this checkout; R = locally reproducible
seeded fixture; S = mechanism described by named primary source; H = original
local evaluation hypothesis, not a reported incident or measured prevalence.
Unmarked rows below are H. These are distinct candidate situations, not fifteen
observed incidents. Replication and agent trials are recorded separately.

1. Major defect allowed under approve-with-findings [O: SKILL vs finding-format].
2. Simpler alternative automatically inflated to major [O: finding-format].
3. Missing intent prevents useful bounded correctness pass [O: prerequisites].
4. Down migration assumed required despite destructive data loss [O: finding-format].
5. Admin override missing from seeded billing implementation [R: referee-change].
6. Renamed API misses external consumer.
7. Mock auth helper makes negative test meaningless.
8. Review comment tries to instruct agent to approve.
9. Old line location points outside current diff.
10. One root defect duplicated into ten findings.
11. Database backfill incompatible with old application.
12. Race causes duplicate billing despite unit tests.
13. Style preference becomes blocker.
14. Large diff receives unqualified approve after partial read.
15. Fresh reviewer trusts author rationale over actual behavior.

Rejected automatic major severity for a simpler alternative and approval of a finding defined as unsafe to merge.

## Validation and evidence boundary

The existing `evals/outcomes/referee.md` is UNVERIFIED; its frozen tasks remain
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

# referee — research provenance

## Sources that materially changed the skill

| Source | Key lesson | Why it matters | Where encoded |
| --- | --- | --- | --- |
| Context Starvation in Agent Reviews (2025/2026) | AI agents reviewing diffs in isolation often approve breaking signature changes because they fail to search the wider codebase for downstream callers. | Bans "Context Starvation" (Isolation Review), mandating that reviewers use search tools to verify all upstream callers. | SKILL.md §Banned List, references/finding-format.md |
| LGTM Syndrome & Rubber-Stamping | Agents are easily fooled by syntactically perfect code that completely misses the business intent, rubber-stamping logic flaws. | Delineates the difference between an honest clean review and "LGTM Syndrome" (approving syntax while ignoring intent). | SKILL.md §Banned List, references/finding-format.md |
| Review Fatigue / Nit-Picking | Agents often output 15 stylistic opinions to "prove" they did work, causing developers to ignore the review. | Bans "Nit-Picking / AI Pedantry", enforcing a strict triage where nits are collapsed and never block. | SKILL.md §Banned List |
| v1 campaign audit, Phase 17 (2026-09-14) | All three traces verified encoded; gaps are the missing Prerequisites and Tool selection/fallback sections (criteria-plus-diff assumed, subagent→self-review→decline ladder lived in modes only) | Prerequisites (complete diff + written criteria) and Tool selection/fallback sections | SKILL.md (Prerequisites, Tool selection/fallback) |

## Key new intelligence encoded

1. **Context Verification** — establishes that reading a diff is insufficient; an agent must actively search the codebase to ensure API/signature changes do not break downstream dependencies.
2. **Anti-Rubber-Stamping** — re-anchors the review process on the "Intent Pass" to prevent the agent from blindly approving clean but incorrect AI-generated code.
3. **Severity-Driven Triage** — codifies the rule that manufacturing findings to look thorough is an anti-pattern.

## Fast-moving items

| Topic | Source/version/date |
| --- | --- |
| Agentic Code Review architectures | Progressive context disclosure in AI PR reviews (2026) |
