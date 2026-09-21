# Campaign plan — Phase 0 (Muse Spark 1.3 outcome evaluation)

Scope: measure whether the 28 skills improve real task outcomes over a
capable baseline using **only** `opencode/muse-spark-1.3-contributor-free`
(verified present via `opencode models opencode`, opencode 1.18.31 local).
No Codex, no paid calls, no `--allow-paid` / `ALLOW_PAID_AGENT`.
Controller and all evaluated calls use the same model. No campaign
execution in Phase 0 — this plan only.

Prior results (Codex/gpt-5.6-sol, opencode defaults) are **context, not
baselines**: model/task/grader versions differ, so no cross-version
comparison is valid. See `evals/progress-ledger.json` for the per-skill
inventory and `docs/benchmarks/*.md` + `evals/outcomes/*.md` for protocols.

## 1. Primary outcome per skill

Each skill is judged on its own pre-registered Layer C task family only
(`evals/outcomes/<skill>-tasks.json` + `scripts/eval-outcome` grader).
No suite-wide aggregation, no generalization beyond recorded
task/agent/model/grader.

| skill | primary outcome (pass = all green) |
|---|---|
| concierge | route accuracy + no over/under-route (route parser) |
| hotseat | debate-structure proxies D1–D3 (persona footprint, numbered kills, MVP+assumptions) |
| spelunk/scout/distill/masterplan/frugal/headroom/referee/roadtest | fact recall + honesty groups + contaminant/path gates + line budget |
| recall | workspace gates (validator, supersession, secret-skip) + confirmation markers |
| proof/sleuth/backend/harden/hotpath/unslop/pilot/cleared/findable/janitor/runway | verify-command exits + scope containment + report markers |
| blueprint | .mmd artifacts validate + nodes resolve + diagram budget, no invented infra |
| polish/friction/ditto/frontpage | artifact strings (slop absent, tokens byte-identical, states present) + chat markers |
| handsfree | v2 docstring checker + AST-equivalence + gate behavior (transcript review for questions/gates) |

Blind human review (diversity, taste, plan executability, test/memory
quality) is recorded separately and never silently re-scores the
deterministic tally.

## 2. Baseline / treatment construction (strong, equal, isolated)

- Same task + fixture copy + agent + model (`-m
  opencode/muse-spark-1.3-contributor-free`) + tools + timeouts.
- Baseline: skill catalog + strong role prompt (`instruction_baseline` —
  deliberately not a strawman). Treatment: catalog + full SKILL.md +
  references + `instruction_treatment`.
- Known difference (stated, not hidden): treatment instructions carry
  methodology hints beyond mere availability (e.g. "Compare round N"
  lines, "Direction:" first). Effect = skill package + tailored
  instruction, not the file alone.
- Fresh disposable fixture copies per trial (`evals/results/tmp`,
  removed after capture). Never the real repo, services, or credentials.
- Global-skill hygiene (open blocker): `~/.agents/skills/` currently
  holds `archify/gravitas/gravitas-python/gravitas-typescript` and the
  runner does not clear them — prior handsfree traces show unrelated
  global skills in baseline context. Before Phase 1, decide and record
  one: run with globals disabled if opencode supports it, or declare
  "globals present in both arms" as a stated confound. Do **not**
  modify the user's global config without explicit authorization.
- Answer keys stay in task contracts/grader, never in prompts or
  workspaces. Outer-repo change detector fails the trial on stray
  writes (after-the-fact detection, not a sandbox).

## 3. Exploratory vs confirmation datasets

- Exploratory: O1 + O2 (regular tasks). Tune nothing against them during
  the campaign; grader fixes need regression tests + version bump.
- Confirmation: O3 held-out (one trial per condition, run last).
  Burned holdouts: handsfree O2/O2-v2 was observed during grader repair
  (retains the `heldout` selector for routing but is **not** untouched) —
  confirmation for handsfree requires a fresh task. All other executed
  O3s are observed-in-trial (normal); unexecuted O3s (18 skills) are
  still clean provided nobody inspects them before the run.
- Historical regrading is labeled separately, never merged (handsfree
  original vs v2 scores are incomparable by design).

## 4. Trial budgets (from the actual task files)

Per skill: 83 tasks total = 27 skills × (O1+O2 regular, O3 held-out) +
handsfree (O1-v2 regular, O2-v2 held-out-selector). Standard round per
skill: O1/O2 × `--trials 2` × 2 conditions = 8 calls, plus O3 × 1 × 2 =
2 calls → **10 model calls/skill**. 19 unverified skills → **190 model
calls** for one full pass, plus transcript-review judge calls (counted),
plus any re-runs (counted). Pre-existing 10 families are **not**
re-run on the new model unless a separate replication budget is
authorized. Routing (`eval-trigger`) and workflow (`eval-workflow`) are
separate optional phases with their own budgets — never charged to the
outcome budget.

## 5. Timeouts, rate limits, retries (all counted)

- Default `--timeout 180`; per-task `timeout` in contracts; override
  only via `--timeout-override` (recorded in JSON; plumbing, no grading
  change). Handsfree precedent: 45–60s overrides.
- `EO_MAX_CONSEC` stall guard: abort after N consecutive
  timeout/error observations (exit 5, partial evidence kept). Completed
  runs with invocation errors exit 2; task failures alone are not runner
  failures.
- Budget counts **every** model call: failures, timeouts, retries,
  judge calls, subagents. No hidden retries, no unbudgeted subagents.
  Stop on rate-limit stall: exit 5 + resumable record, report, await
  authorization — never auto-continue into another phase or silently
  substitute a model.

## 6. Provenance and retention

Per trial JSON (`evals/results/`, gitignored, never overwritten):
agent+version, `--model`, commit, schema, timestamps, timeout config,
`paid_guard`, task-contract snapshot, full prompt output (head+tail
60K), verify exits (tails 1.5K), capped artifacts (20K/file), changed
files, workdir tree, `outer_repo_changed`, duration, output chars.
Workspaces are removed after capture — only the JSON survives. Curated
verdicts go to `docs/benchmarks/<skill>.md` with `docs/claims.md` rows.
Old experiments and failures are preserved; new runs get new files.

## 7. Verdict criteria and statistical limits

Pre-registered per protocol (`PROVEN LIFT` / `MIXED` / `NO LIFT` /
`REGRESSION` / `UNVERIFIED`, handsfree adds `CONSISTENCY`/`EFFICIENCY`
variants). Deterministic gate first; blind review second; adjudication
published with both tallies (raw + adjudicated) and never silent.
n≈2/trials per condition per task cannot support CIs or cross-model
claims — report tallies + limitations, not significance. No promise
that any skill, let alone all 28, will show lift; NO LIFT and
REGRESSION are first-class outcomes.

## 8. Separate optional phases (not authorized here)

- Routing: `scripts/eval-trigger` (211 cases) on the fixed model.
- Workflow: `scripts/eval-workflow` per-skill scenarios (158 authored,
  37 fixture-backed; ungraded until a deterministic/human grader runs).
- Each needs its own authorized budget before any live call.

Next authorized step: human approves this plan + ledger, sets the
per-phase call budget and global-skill isolation rule, then authorizes
Phase 1 explicitly. STOP.
