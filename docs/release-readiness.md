# Release readiness, 2026-10-14

**Local implementation checkpoint: PASS. Master behavioral acceptance: NOT YET MET.**

All 28 names remain frozen. The branch includes individual corrections, current
primary-source traces, domain cases, copied-package tests and retained exploratory
tasks. That does not establish significantly better results than an ordinary
agent, native host activation, complete source-perspective coverage or production
readiness. No new comparative performance claim, PR, push, deployment or release
was made. Historical outcome evidence is preserved.

## Current 28-row status matrix

Implemented means the recorded narrow change exists. Review means independent
static inspection of the retained snapshot; later changed files are recorded
in the ledger. Local observations are scoped task artifacts, not global skill
passes. Native activation and controlled current-model lift are UNVERIFIED for
every row.

| Skill | Implemented | Independent static review | Local observation | Remaining behavior gate |
| --- | --- | --- | --- | --- |
| `backend` | yes, narrow upgrade | reviewed snapshot; later changes self-reviewed | [EXECUTABLE_LOCAL](upgrade/evidence/forward/backend/report.json) | native activation / comparative lift UNVERIFIED; source depth partial |
| `blueprint` | yes, narrow upgrade | reviewed snapshot | [SOURCE_OR_SCENARIO_ONLY](upgrade/evidence/specialist-forward/blueprint/artifact.md) | native activation / comparative lift UNVERIFIED; source depth partial |
| `cleared` | yes, narrow upgrade | reviewed snapshot | [SOURCE_OR_SCENARIO_ONLY](upgrade/evidence/specialist-forward/cleared/artifact.md) | native activation / comparative lift UNVERIFIED; source depth partial |
| `concierge` | yes, narrow upgrade | reviewed snapshot | [SOURCE_OR_SCENARIO_ONLY](upgrade/evidence/intelligence-forward/concierge/artifact.md) | native activation / comparative lift UNVERIFIED; source depth partial |
| `distill` | yes, narrow upgrade | reviewed snapshot | [SOURCE_OR_SCENARIO_ONLY](upgrade/evidence/intelligence-forward/distill/artifact.md) | native activation / comparative lift UNVERIFIED; source depth partial |
| `ditto` | yes, narrow upgrade | reviewed snapshot | [DEGRADED_STATIC; BROWSER_UNVERIFIED](upgrade/evidence/specialist-forward/ditto/artifact.md) | native activation / comparative lift UNVERIFIED; source depth partial |
| `findable` | yes, narrow upgrade | reviewed snapshot | [SOURCE_OR_SCENARIO_ONLY](upgrade/evidence/specialist-forward/findable/artifact.md) | native activation / comparative lift UNVERIFIED; source depth partial |
| `friction` | yes, narrow upgrade | reviewed snapshot | [DEGRADED_STATIC; BROWSER_UNVERIFIED](upgrade/evidence/specialist-forward/friction/artifact.md) | native activation / comparative lift UNVERIFIED; source depth partial |
| `frontpage` | yes, narrow upgrade | reviewed snapshot | [EXECUTABLE_LOCAL](upgrade/evidence/specialist-forward/frontpage/artifact.md) | native activation / comparative lift UNVERIFIED; source depth partial |
| `frugal` | yes, narrow upgrade | reviewed snapshot | [SOURCE_OR_SCENARIO_ONLY](upgrade/evidence/specialist-forward/frugal/artifact.md) | native activation / comparative lift UNVERIFIED; source depth partial |
| `handsfree` | yes, narrow upgrade | reviewed snapshot | [EXECUTABLE_LOCAL](upgrade/evidence/intelligence-forward/handsfree/artifact.md) | native activation / comparative lift UNVERIFIED; source depth partial |
| `harden` | yes, narrow upgrade | reviewed snapshot | [EXECUTABLE_LOCAL](upgrade/evidence/forward/harden/report.json) | native activation / comparative lift UNVERIFIED; source depth partial |
| `headroom` | yes, narrow upgrade | reviewed snapshot | [SOURCE_OR_SCENARIO_ONLY](upgrade/evidence/specialist-forward/headroom/artifact.md) | native activation / comparative lift UNVERIFIED; source depth partial |
| `hotpath` | yes, narrow upgrade | reviewed snapshot | [EXECUTABLE_LOCAL](upgrade/evidence/specialist-forward/hotpath/artifact.md) | native activation / comparative lift UNVERIFIED; source depth partial |
| `hotseat` | yes, narrow upgrade | reviewed snapshot | [SOURCE_OR_SCENARIO_ONLY](upgrade/evidence/intelligence-forward/hotseat/artifact.md) | native activation / comparative lift UNVERIFIED; source depth partial |
| `janitor` | yes, narrow upgrade | reviewed snapshot | [EXECUTABLE_LOCAL](upgrade/evidence/specialist-forward/janitor/artifact.md) | native activation / comparative lift UNVERIFIED; source depth partial |
| `masterplan` | yes, narrow upgrade | reviewed snapshot | [SOURCE_OR_SCENARIO_ONLY](upgrade/evidence/intelligence-forward/masterplan/artifact.md) | native activation / comparative lift UNVERIFIED; source depth partial |
| `pilot` | yes, narrow upgrade | reviewed snapshot | [EXECUTABLE_LOCAL](upgrade/evidence/intelligence-forward/pilot/artifact.md) | native activation / comparative lift UNVERIFIED; source depth partial |
| `polish` | yes, narrow upgrade | reviewed snapshot | [DEGRADED_STATIC; BROWSER_UNVERIFIED](upgrade/evidence/forward/polish/report.json) | native activation / comparative lift UNVERIFIED; source depth partial |
| `proof` | yes, narrow upgrade | reviewed snapshot | [EXECUTABLE_LOCAL](upgrade/evidence/specialist-forward/proof/artifact.md) | native activation / comparative lift UNVERIFIED; source depth partial |
| `recall` | yes, narrow upgrade | reviewed snapshot | [EXECUTABLE_LOCAL](upgrade/evidence/intelligence-forward/recall/artifact.md) | native activation / comparative lift UNVERIFIED; source depth partial |
| `referee` | yes, narrow upgrade | reviewed snapshot | [SOURCE_OR_SCENARIO_ONLY](upgrade/evidence/specialist-forward/referee/artifact.md) | native activation / comparative lift UNVERIFIED; source depth partial |
| `roadtest` | yes, narrow upgrade | reviewed snapshot; later changes self-reviewed | [DEGRADED_STATIC; BROWSER_UNVERIFIED](upgrade/evidence/specialist-forward/roadtest/artifact.md) | native activation / comparative lift UNVERIFIED; source depth partial |
| `runway` | yes, narrow upgrade | reviewed snapshot | [SOURCE_OR_SCENARIO_ONLY](upgrade/evidence/specialist-forward/runway/artifact.md) | native activation / comparative lift UNVERIFIED; source depth partial |
| `scout` | yes, narrow upgrade | reviewed snapshot | [SOURCE_OR_SCENARIO_ONLY](upgrade/evidence/intelligence-forward/scout/artifact.md) | native activation / comparative lift UNVERIFIED; source depth partial |
| `sleuth` | yes, narrow upgrade | reviewed snapshot | [EXECUTABLE_LOCAL](upgrade/evidence/forward/sleuth/report.json) | native activation / comparative lift UNVERIFIED; source depth partial |
| `spelunk` | yes, narrow upgrade | reviewed snapshot | [SOURCE_OR_SCENARIO_ONLY](upgrade/evidence/intelligence-forward/spelunk/artifact.md) | native activation / comparative lift UNVERIFIED; source depth partial |
| `unslop` | yes, narrow upgrade | reviewed snapshot | [EXECUTABLE_LOCAL](upgrade/evidence/specialist-forward/unslop/artifact.md) | native activation / comparative lift UNVERIFIED; source depth partial |

## Checks actually executed

| Command | Observed result | Receipt |
| --- | --- | --- |
| `scripts/validate-skills` | PASS (exit 0) | [raw record](upgrade/evidence/final-checks/validate-skills.json) |
| `scripts/check-names` | PASS (exit 0) | [raw record](upgrade/evidence/final-checks/check-names.json) |
| `scripts/check-links` | PASS (exit 0) | [raw record](upgrade/evidence/final-checks/check-links.json) |
| `scripts/validate-frontmatter` | PASS (exit 0) | [raw record](upgrade/evidence/final-checks/validate-frontmatter.json) |
| `scripts/check-claims` | PASS (exit 0) | [raw record](upgrade/evidence/final-checks/check-claims.json) |
| `scripts/check-readme-sync` | PASS (exit 0) | [raw record](upgrade/evidence/final-checks/check-readme-sync.json) |
| `scripts/test-regressions` | PASS (exit 0) | [raw record](upgrade/evidence/final-checks/test-regressions.json) |
| `scripts/test-upgrade` | PASS (exit 0) | [raw record](upgrade/evidence/final-checks/test-upgrade.json) |
| `scripts/check-packages` | PASS (exit 0) | [raw record](upgrade/evidence/final-checks/check-packages.json) |
| `scripts/check-demos` | PASS (exit 0) | [raw record](upgrade/evidence/final-checks/check-demos.json) |
| `scripts/test-archetypes` | PASS (exit 0) | [raw record](upgrade/evidence/final-checks/test-archetypes.json) |
| `scripts/run-evals` | PASS (exit 0) | [raw record](upgrade/evidence/final-checks/run-evals.json) |
| `scripts/check-context` | PASS (exit 0) | [raw record](upgrade/evidence/final-checks/check-context.json) |
| `skills/frugal/scripts/cost-report.py --self-test` | PASS (exit 0) | [raw record](upgrade/evidence/final-checks/cost-report.py-self-test.json) |
| `skills/runway/scripts/check-receipt.py --self-test` | PASS (exit 0) | [raw record](upgrade/evidence/final-checks/check-receipt.py-self-test.json) |
| `git diff --check` | PASS (exit 0) | [raw record](upgrade/evidence/final-checks/diff-check.json) |

Existing regressions: 45 passed. Upgrade integrity/helper regressions: 12 passed.
Fixture contracts: 267 trigger cases, 324 workflows (54 fixture-backed), 87
unchanged outcome tasks. The three corrected executable demonstrations have
16 passing boundary tests; six corrected offline/game model tests pass. Their
faulty seeds still fail the intended assertions. These counts describe local
checks and authored cases, not comparative skill performance.

Optional `skills-ref` was unavailable; local strict frontmatter validation ran.
Node 24.11.0 and Python 3.14.6 were observed locally. Remote GitHub Actions was
not run; its updated deterministic configuration is not CI-execution evidence.
Generated docs were regenerated and their index did not change (frontmatter
was preserved). No mypy/ruff/global framework claim is made.

## Installation and host evidence

Public default-branch bundle install with pinned CLI 1.7.2: PASS, 28 folders.
Final local implementation packages installed individually: PASS, exact bytes
and executable flags match; no extra skill installed in a selected-skill run.
[Packaging receipts and runtime cells](compatibility.md). The public install
does not include this unpushed branch.

| Runtime/platform | Current native activation / task compatibility |
| --- | --- |
| Codex | UNVERIFIED; CLI present; no paid CLI trial |
| Claude Code | UNVERIFIED; CLI present, historical hang evidence retained |
| OpenCode | UNVERIFIED; binary present, current version output empty |
| Cursor | UNAVAILABLE locally; UNVERIFIED behavior |
| Antigravity | UNAVAILABLE locally; UNVERIFIED behavior |
| Gemini CLI | NOT TESTED |
| Linux / Windows | NOT TESTED locally; Ubuntu CI configured, not executed remotely |
| Real mobile/device, browser, PostgreSQL, hosted deployment | UNVERIFIED |

## Source and operational limits

The requested five source perspectives, 8–15 load-bearing sources and real
developer-incident triangulation per skill are incomplete. Each note labels
current accessed docs, historical unsupported notes, original test hypotheses
and failed access. A further researcher hit the session usage limit after
identifying two mechanisms; those mechanisms were adopted only after the
primary agent read the official AWS and Playwright sources.

Browser local-file access was policy-denied, and loopback server creation was
unavailable. No workaround or invented screenshot was used. There was no native
mobile app, real PostgreSQL service, safe staging deployment/rollback or manual
study with real developers. The five archetype gaps are listed in the
[gallery](demo-gallery.md).

No paid-agent CLI or spend-enabling keys were used. Exploratory in-session
worker costs are not exposed and remain UNKNOWN. Workers hit usage limits;
completed artifacts and interruptions were retained. No causal, cross-model or
cross-runtime benefit is inferred from these shared-session tasks.

## Concrete continuation order

1. Complete per-skill source-perspective and real-incident research only where
   it changes a decision; retain opposing evidence and source/version limits.
2. Materialize the missing full-stack/PostgreSQL, mobile and browser/game
   integrations and obtain genuine browser/device/staging capabilities.
3. Run native activation and outcome trials on pinned tasks/models/tools with
   independent oracles; authorize billed campaigns separately with both human
   keys. Preserve historical results and all failures.
4. Run the consented novice/expert onboarding study and the pending visual
   demonstration; use the [launch drafts](launch-plan.md) only after the human
   authorizes any publication.

[28-row detailed ledger](upgrade-ledger.md), [research index](research/README.md),
[ownership matrix](skill-matrix.md), [independent review](upgrade/independent-review.json),
[verified follow-through](upgrade/followthrough.json), and
[three genuine local narratives](demo-gallery.md) provide resumable evidence.

## Late staged-diff correction

The earlier working-tree `git diff --check` did not inspect untracked evidence.
The staged check found generated CSV CRLF plus spaces intrinsic to raw patch
context lines and numbered source-read captures. A commit mistakenly proceeded
after that failure. The follow-up normalizes the generated CSV to LF, preserves
raw captures, and executes an explicit whole-change source/docs check excluding
only those raw formats. [Discovery](upgrade/evidence/staged-whitespace-discovery.json)
and [scoped source check](upgrade/evidence/source-diff-check.json) record both.
No raw test outcome or review receipt was rewritten to manufacture a pass.

## Clean committed checkout and Git record

A new local clone of committed candidate
`c86c38e3c5b87627074a467e000030f23ef942b8` passed the required validators,
45 existing regressions, 12 upgrade regressions, fixture checks, 28 standalone
package copies, demo replays, offline/game models and regenerated-index check.
The clone remained clean. [Exact clean-checkout receipt](upgrade/evidence/clean-checkout.json).
This is local execution evidence, not a remote GitHub Actions run.

Implementation commits on `codex/deep-skills-v2`:

- `190ca7a`: evaluation identity, on-demand context and package/trigger checks.
- `9a03932`: intelligence workflow corrections and individual cases.
- `8164472`: backend, architecture, UX and verification boundaries.
- `274f6d2`: safety, cleanup and release evidence contracts.
- `b66defd`: retained task/review evidence, CI, ownership and readiness docs.
- `c86c38e`: CSV newline correction and explicit raw-capture whitespace scope.

A final evidence-only commit saves the clean-checkout receipt. No PR, push,
external post, deployment or release was created.
