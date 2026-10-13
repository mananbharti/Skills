# runway - current failure-first research pass

Reviewed 2026-10-14 against commit 66668739d4e3b99aab30bdea9594ca6361072c84.

Ownership: candidate deployment, live verification and recovery; cleared judges readiness, headroom designs capacity.

Observed baseline instruction defect: Preview freely authorized regardless paid/shared data risk; local build always required; rolling assumed everywhere; speculative rollback commands; deployment existence confused with verified behavior.

Changed judgment: Scope preview data/cost/exposure; accept trusted candidate CI build; preserve dirty work; platform-checked recovery; bounded fingerprint/smoke observations and data-compatible rollback.

## Source-to-decision trace

| Source | Organization / version / date | Access | Proposition and exact artifact | Rejected alternative / limit | Refresh |
| --- | --- | --- | --- | --- | --- |
| [Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) | Kubernetes project; current concepts documentation; target cluster version required; living; date not established | fetched 2026-10-14 | Controller progress and Deployment revision rollback do not restore application data. Decision encoded in `skills/runway/SKILL.md`, `skills/runway/references/platforms.md`, `skills/runway/references/release-protocol.md` and `skills/runway/scripts/check-receipt.py` (bounded observations). | No general guarantee or behavioral lift inferred. | source revision, target version, or affected boundary changes |
| [Performing an Instant Rollback](https://vercel.com/docs/instant-rollback) | Vercel; current platform guidance; plan and CLI verified per project; living; date not established | fetched 2026-10-14 | Rollback restores previous deployment assumptions; external data and configuration must be checked separately. Decision encoded in `skills/runway/SKILL.md`, `skills/runway/references/platforms.md`, `skills/runway/references/release-protocol.md` and `skills/runway/scripts/check-receipt.py` (bounded observations). | No general guarantee or behavioral lift inferred. | source revision, target version, or affected boundary changes |

Each source was opened individually through web access. Dates not shown by a
source are explicitly unknown; retrieval date is not publication date. The
self-contained package retains full source records in its research reference.

## Failure situation register

O = observed instruction defect in this checkout; R = locally reproducible
seeded fixture; S = mechanism described by named primary source; H = original
local evaluation hypothesis, not a reported incident or measured prevalence.
Unmarked rows below are H. These are distinct candidate situations, not fifteen
observed incidents. Replication and agent trials are recorded separately.

1. Preview automatically allowed against shared production data [O: safety rails].
2. Mandatory local build duplicates trusted pipeline [O: prerequisites].
3. Rolling assumed default for every platform [O: workflow].
4. Unverified Netlify/Workers rollback command supplied for Pages [O: platforms].
5. CLI zero accepted while old public fingerprint remains [H: receipt guard].
6. Remote build queued not complete.
7. Public alias routes to older build.
8. Cache-busted route new but normal user route old.
9. Health200 but checkout fails.
10. Secrets presence check prints values.
11. Schema migration makes old build incompatible.
12. Rollback command succeeds but prior smoke fails.
13. Missing access claimed as deployment success.
14. Preview resource spends beyond authorization.
15. Installed mobile binaries cannot instantly be reverted.

Rejected automatic free preview scope, application rollback as database undo, Workers commands as Pages guarantees, and CLI zero as live proof.

## Validation and evidence boundary

The existing `evals/outcomes/runway.md` is UNVERIFIED; its frozen tasks remain
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

# runway — research provenance

## Sources that materially changed the skill

| Source | Key lesson | Why it matters | Where encoded |
| --- | --- | --- | --- |
| The Execution Layer Gap (2025/2026) | Autonomous agents often suffer from "Blind Fire-and-Forget"—executing a deployment command but failing to observe the resulting remote state before declaring success. | Bans "Blind Fire-and-Forget", enforcing a hard requirement to verify the live URL after the deployment tool exits. | SKILL.md §Banned List |
| Dashboard Hallucinations | AI systems incorrectly assume a workflow succeeded because the deployment agent exited 0, while the actual web server is crash-looping. | Bans "Dashboard Hallucination", forcing the agent to verify the exact build fingerprint on the live endpoint. | SKILL.md §Banned List |
| Enterprise Cosplay | Agents trained on generic "best practices" inject massive unnecessary infrastructure complexity (e.g. k8s canary deploys for static sites). | Explicitly names and bans "Enterprise Cosplay", keeping deployment strategy tethered to the actual platform. | SKILL.md §Banned List |
| v1 campaign audit, Phase 26 (2026-09-14) | All three traces verified encoded; gaps are the missing Prerequisites and Tool selection/fallback sections (cleared-fresh assumed, CLI→preflight→plan-only ladder scattered) | Prerequisites (cleared-fresh + build + access) and Tool selection/fallback sections | SKILL.md (Prerequisites, Tool selection/fallback) |

## Key new intelligence encoded

1. **Visible Execution** — mandates that deployment is not complete when the CLI returns, but only when the live URL serves the new build.
2. **Contextual Infrastructure** — stops agents from over-engineering deployment strategies beyond the needs of the detected platform.

## Fast-moving items

| Topic | Source/version/date |
| --- | --- |
| Agentic CI/CD | Specialist Agent Networks for deployment verification (2026) |

## Dated evaluator conflict - 2026-10-14

Frozen outcome O2 demands confirmation despite explicit deploy wording; inability to deploy due missing access/readiness is separate from missing authorization. RW1 historical clean/local-build requirements are superseded by candidate identity and trusted pipeline evidence. No frozen task was changed or regraded.

## Verification 2026-10-14

| Basis | Outcome |
| --- | --- |
| Fowler ParallelChange; fetched 2026-10-14 | Migration section requires contract-phase evidence, not strategy prose alone. |
