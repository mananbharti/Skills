# Benchmarks — skill vs no skill

The credibility layer: same agent + same task + skill, versus same
agent + same task + no skill. Controlled where controllable, multiple
runs where stochastic, raw outputs recorded, cherry-picking forbidden.

## Status: empirical proof phase underway

Ten of 28 skill families have executed baseline-vs-skill trials, including
the `handsfree` grader-debugging smoke sample. Current
skill-specific verdicts are: `hotseat` PROVEN LIFT; `concierge`, `proof`,
`recall`, `spelunk`, and `scout` MIXED; `distill`, `masterplan`, and `pilot`
NO LIFT on the available evidence. Nineteen remain UNVERIFIED: `handsfree`
despite its completed smoke sample, plus 18 without completed trials. These are
not suite-wide or cross-model superiority claims.

Each result page under [`docs/benchmarks/`](benchmarks/) records agent +
version, model, date, git commit, run count, grading limits, and the observed
trial table. Raw runner outputs remain under the gitignored `evals/results/`
unless curated evidence is explicitly committed.

## All-Muse-Spark campaign matrix (Batch A + routing smoke, 2026-09-20/21)

One pinned model throughout: `opencode/muse-spark-1.3-contributor-free`
via opencode 1.18.31, outcome schemas 3/4, alternating order, contract
timeouts. Prior-model rows (Codex/gpt-5.6-sol, opencode defaults,
outcome/2) live only on the per-skill pages and in `docs/scorecard.md` —
**never pooled** with the rows below. Durations MEASURED per trial;
token/usage telemetry UNKNOWN everywhere (no headless provider
telemetry). Safety = no secrets written, no destructive ops, no outer
writes, no scope violations (none observed in any new-model run).

| Skill | Task / grader / versions | Exploratory (per cond.) | Post-expl. validation C1 (5/cond.) | Safety | Resources | Limitation | Narrow verdict | Raw |
|---|---|---|---|---|---|---|---|---|
| `handsfree` | O1-v2 + C1 / exe checks + AST / skill+checker frozen | O1-v2 2/2 vs 2/2 (n=2) | 5/5 vs 5/5 (diff 0) | none | 18–26s | one easy task; tie ≠ equivalence | NO CLEAR LIFT | `20260920-085134`, `20260921-190753` |
| `concierge` | O1+O2 + C1 / route parser / skill frozen | O1 0/2 vs 2/2; O2 2/2 vs 2/2 (n=2) | 0/5 vs 0/5, order-gate only, all 10 routes correct | n/a (chat) | 9–47s | C1 order over-constrained (task defect C) | exploratory edge O1; validation INSUFFICIENT | `20260920-085320`, `20260921-191149` |
| `spelunk` | O1+O2 + C1 / fact grader v3–v4 / skill frozen | O1 1/2 vs 1/2; O2 2/2 vs raw 0/2 adj. tie (n=2) | recorded 2/5 vs 0/5, recall 1.0 all 10 | n/a (chat) | 19–63s | grader-flag dominated (negated + sandbox-path residue) | INSUFFICIENT EVIDENCE; no regression | `20260920-085619`, `20260921-191555` |
| `recall` | O1+O2 + C1 / exe checks + markers / skill frozen | O1 0/2 vs 2/2 marker-only; O2 0/4 tie (n=2) | 0/5 vs 5/5, workspace green all 10 | none | 24–119s | +5 is 100% `recall:`-marker advantage | MIXED, format-only | `20260920-090051`, `20260921-192242` |
| `hotseat` | — (not run on this model) | — | — | — | UNKNOWN | prior Codex row only, unpooled | UNVERIFIED (this model) | — |
| `distill` | — | — | — | — | UNKNOWN | prior row only, unpooled | UNVERIFIED (this model) | — |
| `masterplan` | — | — | — | — | UNKNOWN | prior row only, unpooled | UNVERIFIED (this model) | — |
| `scout` | — | — | — | — | UNKNOWN | prior row only, unpooled | UNVERIFIED (this model) | — |
| `pilot` | — | — | — | — | UNKNOWN | prior row only, unpooled | UNVERIFIED (this model) | — |
| `proof` | — | — | — | — | UNKNOWN | prior row only, unpooled | UNVERIFIED (this model) | — |
| `backend` | — | — | — | — | UNKNOWN | zero trials anywhere | UNVERIFIED | — |
| `blueprint` | — | — | — | — | UNKNOWN | zero trials anywhere | UNVERIFIED | — |
| `headroom` | — | — | — | — | UNKNOWN | zero trials anywhere | UNVERIFIED | — |
| `polish` | — | — | — | — | UNKNOWN | zero trials anywhere; visual claims need browser evidence | UNVERIFIED | — |
| `friction` | — | — | — | — | UNKNOWN | zero trials anywhere | UNVERIFIED | — |
| `ditto` | — | — | — | — | UNKNOWN | zero trials anywhere; visual claims need screenshots | UNVERIFIED | — |
| `roadtest` | — | — | — | — | UNKNOWN | zero trials anywhere; browser coverage needs browser execution | UNVERIFIED | — |
| `sleuth` | — | — | — | — | UNKNOWN | zero trials anywhere | UNVERIFIED | — |
| `referee` | — | — | — | — | UNKNOWN | zero trials anywhere | UNVERIFIED | — |
| `hotpath` | — | — | — | — | UNKNOWN | zero trials anywhere | UNVERIFIED | — |
| `harden` | — | — | — | — | UNKNOWN | zero trials anywhere; findings need locations + validation | UNVERIFIED | — |
| `unslop` | — | — | — | — | UNKNOWN | zero trials anywhere | UNVERIFIED | — |
| `janitor` | — | — | — | — | UNKNOWN | zero trials anywhere | UNVERIFIED | — |
| `frontpage` | — | — | — | — | UNKNOWN | zero trials anywhere | UNVERIFIED | — |
| `findable` | — | — | — | — | UNKNOWN | zero trials anywhere | UNVERIFIED | — |
| `frugal` | — | — | — | — | UNKNOWN | zero trials; savings need provider measurements | UNVERIFIED | — |
| `cleared` | — | — | — | — | UNKNOWN | zero trials; must not perform real releases | UNVERIFIED | — |
| `runway` | — | — | — | — | UNKNOWN | zero trials; must not perform real deployments | UNVERIFIED | — |

Routing (separate layer, never merged with outcome): smoke 10/12 on the
pinned model (`evals/results/20260921-194811-opencode.json`);
routing-given-metadata only. Workflow scenarios executed: 0/158.

## Focus skills (signature, public-demo quality)

`hotseat` `polish` `unslop` `blueprint` `harden` `frugal` `frontpage`

## Fixtures

`benchmarks/fixtures/` contains 20 intentionally small repositories or files
with **seeded defects**. The answer key for each fixture lives in
the task contract or `benchmarks/answer-keys/` and is given to the grader,
never to the evaluated agent. `scripts/eval-outcome --check` verifies that
every named fixture resolves before a live run.

| Fixture | Stack | Seeds | Serves |
| --- | --- | --- | --- |
| `ts-dashboard` | TypeScript/React-style web app | swallowed errors, duplicated logic + schema, dead code, unused dep, any-casts, debug leftovers, committed secret, mega-component | `unslop` `harden` `proof` `referee` |
| `py-notes-api` | Python FastAPI-style API | validation gaps, missing tests, config sprawl, doc gaps | `backend` `proof` `frontpage` |
| `ugly-dashboard.html` | single-page vanilla UI | generic AI-UI patterns, missing states, contrast failures | `polish` `friction` |

The table is representative rather than exhaustive; the remaining fixtures
exercise release gates, UI reconstruction, UX, SEO, memory, Git hygiene,
performance, security, browser evidence, and deployment restraint.

PRD §12 names five stack categories. The current set covers TypeScript/web,
Python, and standalone HTML. Go/Rust, Java/Kotlin, and mobile remain explicit
fixture gaps; no cross-stack claim is made for them.

Rules for fixtures: no giant fake repos; every seed documented in the
answer key with location + expected finding; behavior baseline recorded
before benchmarking.

## The frugal protocol (highest-integrity benchmark)

Compare equivalent tasks with/without `frugal`. Track whatever the
runtime exposes (input/output/cache tokens, tool calls, files opened,
bytes read, retries, wall-clock, task success). **Primary metric:
successful-task token cost.** Every number reported as MEASURED /
DERIVED / ESTIMATED / UNKNOWN — a byte-reduction result may be reported
as derived when telemetry is unavailable, and never dressed up as a
token percentage.

## The polish protocol (visual evidence)

Before/after screenshots (desktop + mobile), state coverage
(empty/loading/error), console status, accessibility checks, relevant
Core Web Vitals where practical. No single "aesthetic score" — the
rubric is predefined, and the before/after images are the evidence.
Demo-ready outputs land in `docs/examples/`.
