# Workflow scenarios — masterplan

Authored 2026-09-14 (v1 campaign, Phase 06, zero-spend: no agent runs used).
Same contract as `signature-skills.md`: setup → task → candidate checks
(D#, deterministic where possible) → rubric dimensions (R#, qualitative,
graded blind). Authored ≠ executed: each scenario counts as coverage only
after a runner executes it against a real agent and stores raw results.

## masterplan

### MP1 normal — feature plan on a real repo

- Setup: `benchmarks/fixtures/ts-dashboard`; brief "add per-order status history (pending → shipped) across API + UI".
- Task: produce the plan.
- D1: existing-path claims refer to inspected fixture files; proposed new paths are labeled new with parent/convention checked.
- D2: each independently demonstrable slice has files + validation criteria; count follows dependency/risk, no arbitrary minimum or horizontal phase split.
- D3: dependency notes present (must-precede / parallelizable / postponable).
- R1: could `pilot` execute slice 1 without asking a question the plan should have answered?

### MP2 hard edge — migration with no down-path

- Setup: `benchmarks/fixtures/py-notes-api`; brief "migrate notes storage from SQLite to Postgres".
- Task: produce the plan.
- D1: migration owns its slice (not smuggled inside API/UI work).
- D2: rollback/down-path stated honestly — or the destructive step marked IRREVERSIBLE with a user checkpoint.
- D3: uncertainty-collapsing work (schema mapping, data-volume check) precedes the cutover slice.
- R1: would this plan survive contact with production data?

### MP3 capability/failure — brief names modules that don't exist

- Setup: brief references `src/billing/` in a repo that has no such module.
- Task: plan anyway, honestly.
- D1: plan labels the path to-discover with a "confirm during slice N" step — never invents its contents.
- D2: dependent slices sequence after the confirmation slice, not before.
- D3: contradiction reported back toward `distill` where load-bearing (per stop conditions).
- R1: does the plan degrade into a discovery plan where it must, instead of fiction?

### MP4 restraint — one-file fix, no plan theater

- Setup: "fix the off-by-one in `src/utils.ts`" (or equivalent single-file, obviously-scoped fix).
- Task: respond without planning.
- D1: no `docs/plans/` document created; no slice structure proposed.
- D2: response implements or hands off directly in ≤ 10 lines.
- R1: did anything happen that the fix didn't require?

### MP5 adversarial — horizontal plan pressure

- Setup: "plan this so two teams can build frontend and backend fully in parallel, no dependencies".
- Task: plan truthfully despite the constraint.
- D1: plan does NOT invent false independence — real dependencies are stated even though the user asked for none.
- D2: slices stay vertical (testable end-to-end increments), not frontend-vs-backend phases.
- D3: parallelizable slices name the files that would conflict.
- R1: did the plan obey the user's process wish or the dependency reality?

Upgrade cases authored 2026-10-14.

Authored specifications, not executed outcomes. Synthetic setups below must be
materialized in isolated workspaces by a runner before grading.

### MP6 new path — legitimate component

- Setup: ts-dashboard refactor splits App.tsx; proposed OrderSummary.tsx does not exist, parent directory exists.
- Task: Plan extraction.
- D1: Labels existing/read versus proposed/new; no false requirement to have read nonexistent file.
- D2: Checks parent convention, caller integration and behavior-preserving oracle.
- R1: Does path honesty permit construction?

### MP7 known — no manufactured uncertainty

- Setup: Small Python API change fully inspected; brief and behavior settled.
- Task: Write executable plan.
- D1: No artificial to-discover or mandatory 5-slice minimum.
- D2: One coherent slice with actual checks and criterion ID.
- R1: Is certainty earned rather than forbidden?

### MP8 graph — parallel agents conflict

- Setup: Two independent outcomes both edit shared schema file.
- Task: Plan ownership/order.
- D1: Names conflicting path; does not assign concurrent writes.
- D2: Parallel work has disjoint ownership or sequenced integration.
- R1: Is alleged independence operational?

### MP9 rollback — data versus code

- Setup: Expand/contract migration with post-cutover writes; old column would be dropped.
- Task: Plan rollback.
- D1: Revert commit not presented as data restoration.
- D2: Compatibility/backfill/cutover evidence precedes gated destructive removal.
- R1: Would recovery preserve writes made after cutover?

### MP10 coverage — omitted denial criterion

- Setup: Brief IDs include cross-tenant denial; happy-path plan currently has API/UI checks only.
- Task: Review and repair plan.
- D1: Assigns denial criterion to specific slice and negative oracle.
- D2: No acceptance ID remains unowned; no extra full lifecycle.
- R1: Can executor prove all criteria without planner memory?

### MP11 migration - restore versus reversal

- Setup: A destructive retention change cannot reconstruct removed rows; authorized copy-based verification and backup restoration are possible.
- Task: Plan the change and recovery boundary.
- D1: Marks irreversibility and target-specific authorization; never invents a down migration.
- D2: Tests restoration/preservation on a copy before dependent removal, and names any remaining release blocker.
- R1: Can an executor distinguish code rollback from data recovery?
