# Evidence — spelunk

Status: **MIXED** (2026-09-15, opencode 1.18.31 on muse-spark-1.3, n=2 per
condition O1+O2 + held-out O3 once per condition, zero Codex). Treatment
shows lift on the full-map task (O1 2/2 vs 1/2 — the failing baseline
omitted two required facts); no lift available on the Python fact map
(O2 2/2 vs 2/2 after artifact adjudication, raw 1/2 vs 1/2) or the
held-out re-map (O3 1/1 both after adjudication, raw 0/1 vs 1/1); no
regressions anywhere (treatment never worse).

## Primary claim

Build the smallest accurate mental model of an unfamiliar repository
(fact accuracy per unit of reading).

## Boundaries

Owns: mode selection (quick/deep/teach/risk-map), discovery order,
epistemic labels, budget discipline. Must route elsewhere: settled
single-file questions (just read it), fresh memory (read it instead),
empty repos (say so). Must not: read blindly, invent commands, record
secret values, cite generated/vendor code without verification.

## Method

- Layer A: 6 trigger cases + risk-map case; bundle smoke (C-005) applies.
- Layer B: 5 scenarios `evals/workflow/scenarios/spelunk.md` (SP1–SP5);
  authored, unexecuted.
- Layer C: protocol `evals/outcomes/spelunk.md` + frozen
  `spelunk-tasks.json` (seeded fixtures, answer keys isolated).
  Harness support implemented and offline-tested: fixture workspaces +
  fact-recall/contaminant/hallucinated-path grader. Grader edge cases
  (missing fact, contaminant, invented path) verified to fail correctly
  with diagnostics — no agent involved.

## Raw results

| task | baseline | treatment | runs |
| --- | --- | --- | --- |
| O1 full map (ts-dashboard) | 1/2 | 2/2 | opencode 1.18.31, commit `5a031fc`, 2026-09-15T15:34Z |
| O2 fact map (py-notes-api) | 1/2 | 1/2 | same |
| O3 held-out risk map | 0/1 | 1/1 | same, 15:38Z |

Raw traces: `evals/results/20260915-153842-outcome-spelunk-opencode.json`,
`20260915-153925-outcome-spelunk-opencode-heldout.json` (gitignored).

Grading notes, stated not hidden: three mechanical grader artifacts were
fixed in `scripts/eval-outcome` after these runs and the saved raw
outputs re-graded offline (no agent re-runs): (1) the sandbox workdir
path the agent quotes when reading fixtures (`…/outcome-XXXX/.env`)
counted as an invented path; (2) `lstrip("./")` mangled dotfiles
(`.gitignore` → `gitignore`, then "invented"); (3) no-fixture tasks
flagged every filename mention (not hit here — both spelunk tasks have
fixtures — fixed alongside). With the fixed grader, O3 baseline is 1/1
(its only flags were artifacts). Two semantic flags stand adjudicated as
grader brittleness, not agent error: O2 trial 1 fails in *both*
conditions on `notes.db` (fixture-quoted content —
`sqlite3.connect("notes.db")` in `app/main.py`) and `pyproject.toml`
(a negated claim — "no pyproject.toml found"), so O2 is 2/2 vs 2/2
adjudicated. O1 baseline trial 2 is a genuine miss: `vitest` and
`lodash` absent from a 19-line report the treatment covers in full.

## Limitations (known before first run)

- Headless runners expose no tool-call/file/byte telemetry: accuracy is
  graded first; cost stays honestly labeled from duration/output size.
- Path-existence check covers extension-bearing mentions only.
- Held-out O3 shares the ts-dashboard fixture with O1 (unseen questions;
  no tuning occurs anywhere, so leakage is N/A — stated, not hidden).

## Trial environment notes (first live runs, 2026-09-15, opencode)

- Model scoped: opencode default free model muse-spark-1.3-contributor-
  free at the time of the runs. Results are model-scoped; re-runs on a
  different model are a different row, not an update.
- TMPDIR under the repo (`evals/results/tmp`); durations 15.9–44.2s;
  zero Codex (paid-agent guard default-deny).

## Context audit

SKILL.md ~140 lines, 1 reference (discovery checklist), 1 script
(`inventory`: manifests, ext distribution, largest files, debt, test
ratio, generated/vendor candidates, scoped churn). Phase 03 added the
trace-one-path-early step, precise-symbols-before-grep rung, and
commit/dirty provenance — all inside existing structure.

## Reproduce (requires an explicit trial budget — see policy)

```bash
scripts/eval-outcome --skill spelunk --agent <agent> --trials 2
scripts/eval-outcome --skill spelunk --agent <agent> --trials 1 --heldout
scripts/validate-skills && scripts/check-links && scripts/run-evals
```

## Phase 3 exploratory — Batch A (2026-09-20, new model, not comparable)

Model `opencode/muse-spark-1.3-contributor-free` via opencode 1.18.31,
schema outcome/3, alternating order, regular tasks only (O1+O2, no
holdouts), 8 calls, zero invocation errors. Raw traces gitignored
(`20260920-085619-*-outcome-spelunk-opencode.json`).

| Task | Baseline | Treatment |
|---|---|---|
| O1 full map | 1/2 | 1/2 — symmetric short-output failures, one per arm |
| O2 fact map | 2/2 | raw 0/2, recall 1.0 both — both failures are hallucinated-path flags on negated/absent mentions (`pyproject.toml`/`setup.py` "no files found", `notes.db` "not present") while the baseline passes by saying less |

Failure classification: O1 failures in both arms follow the `.env`
read auto-rejection derailing the run into a short fact-poor report
(environment-triggered task failure, symmetric — recorded as a
suspected harness/environment interaction for offline review, not fixed
during the batch). The O1 `/.env` path flag is auto-rejection trace
residue, a new variant of the known workdir-path brittleness. O2
treatment maps are substantively correct; adjudicated 2/2 vs 2/2 the
task is a tie — verdict shape MIXED-or-tie pending blind review, and
**not comparable** to the 2026-09-15 outcome/2 rows. Durations
19.1–63.1s. Token/file-read efficiency UNKNOWN (no headless telemetry).
Small exploratory sample, not "proven performance."

## Adjudication v1 (2026-09-20, grader v3, outcome/3 records)

Original recorded scores stand and raw records are unmodified. O2
treatment raw 0/2: both failures are hallucinated-path flags on
negated/absent mentions (`pyproject.toml`/`setup.py` "no files found",
`notes.db` "not present") with recall 1.0 and otherwise fully correct
maps; the passing baselines omit those mentions. Adjudicated tally: O2
2/2 vs 2/2 (tie). O1 1/2 vs 1/2 stands (symmetric environment-derailed
shorts, genuine downstream omissions). This re-interpretation is
versioned separately and never replaces a recorded FAIL.

## Post-exploratory validation — Phase 5 Batch A, C1 (2026-09-21)

Frozen C1 (`unslop-shop` fact map), 5 trials per condition on the pinned
model, schema outcome/4, 10 calls, zero invocation errors. Raw:
`evals/results/20260921-191555-*-outcome-spelunk-opencode.json`.

Result: baseline 2/5, treatment 0/5 (recorded difference +2 baseline)
with fact recall 1.0 in ALL 10 runs. Baseline fails: one genuine
over-budget report (141 vs 60 lines) + two negated-mention path flags.
Treatment fails 5/5 on path flags only: four on negated absence
sentences (`package.json`/`pyproject.toml`/`setup.py` "not found") and
one additionally on absolute sandbox-path residue
(`<workdir>/tests/test_shop.py` quoted from the agent's own tool trace —
the recorded workdir matches exactly, yet the strip leaves the
remainder; new suspected grader defect, recorded for offline repair, NOT
fixed during the frozen runs). Every treatment map is substantively
excellent and file-grounded. Verdict: **INSUFFICIENT EVIDENCE —
grader-dominated post-exploratory validation** (class B across the treatment arm). The
+2 recorded gap is a flag artifact, not a skill signal; no regression is
claimed. Durations 23.9–39.7s; reading efficiency UNKNOWN. One task; no
generalization; no reruns.
