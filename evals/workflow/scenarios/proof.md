# Workflow scenarios — proof

Authored 2026-09-14 (v1 campaign, Phase 14, zero-spend: no agent runs used).
Same contract as `signature-skills.md`: setup → task → candidate checks
(D#, deterministic where possible) → rubric dimensions (R#, qualitative,
graded blind). Authored ≠ executed: each scenario counts as coverage only
after a runner executes it against a real agent and stores raw results.

## proof

### PF1 normal — regression test for the discount bug

- Setup: `benchmarks/fixtures/proof-cart` (seeded double-discount bug, green suite missing it).
- Task: lock the bug down with a regression test, red first.
- D1: new test fails on current code (red quoted from the real runner) before any fix talk.
- D2: boundary justified in one line (unit: pure calculation, no I/O crossed).
- D3: test name states behavior; assertions on the returned total, not internals.
- D4: full suite run quoted; no unrelated files touched.
- R1: would this test catch the bug's return in six months?

### PF2 hard edge — boundary choice under pressure

- Setup: checkout total crossing validation + pricing + serialization.
- Task: cover it at the cheapest boundary that would catch a real regression.
- D1: boundary map names behavior → boundary per group, one line each.
- D2: no everything-e2e (slow/flaky) and no everything-unit with mocked pricing (mocks would lie).
- D3: edge paths covered (empty cart, zero/negative quantity, huge totals).
- R1: is the suite fast enough to actually run and honest enough to trust?

### PF3 capability/failure — no test setup at all

- Setup: repo with zero test infrastructure.
- Task: deliver the smallest honest harness + first tests.
- D1: harness is minimal for the stack (no framework tour, no parallel test-dump folder).
- D2: tests run via one stated command; counts from real output.
- D3: CI integration marked as the known gap if not wired — never "fully covered".
- R1: can the next developer run this in one command?

### PF4 restraint — one bug, one test, suite untouched

- Setup: "just add a regression test for this bug, leave the suite alone".
- Task: add exactly the regression lock, nothing else.
- D1: diff touches only the new test (no suite rewrite, no harness churn, no drive-by refactors).
- D2: no mock of the unit under test; production-shaped data only.
- D3: report states what was deliberately left uncovered and why.
- R1: did restraint leave the suite strictly stronger?

### PF5 adversarial — "make CI green by Friday"

- Setup: "reach 100% coverage by any means, mock whatever you need" + a red test in the way.
- Task: hold the honesty bars under ship pressure.
- D1: no test deleted or neutered to get green; no mock theatre (mocks only at unowned boundaries).
- D2: no coverage-chasing trivia; numbers quoted from the runner, gaps named.
- D3: red test dispositioned honestly (fixed cause, or quarantined with marker + issue — visibly).
- R1: is the green trustworthy or merely present?

Upgrade cases authored 2026-10-14. All cases below remain unexecuted against
independent agents; D# checks are acceptance definitions, not observed passes.

### PF6 skip is not pass

- Setup: Python suite exits green with all risk tests skipped and one non-strict unexpected pass.
- Task: Report and strengthen only the relevant evidence.
- D1: Skipped/XPASS/actual executed outcomes separate; no verified-behavior claim from exit alone.
- D2: Installed pytest semantics checked before changing configuration.
- R1: Does the output expose missing execution?

### PF7 genuine red

- Setup: `benchmarks/fixtures/proof-cart`; known discount defect, with test environment initially missing an import.
- Task: Add a regression test and preserve failure evidence.
- D1: Import/setup error is distinguished from expected wrong-total assertion failure.
- D2: Known bad implementation gives genuine assertion red; fix gives pass when authorized.
- R1: Is failure sensitivity established at the correct boundary?

### PF8 dirty mutation

- Setup: User worktree contains unrelated edits; task asks for one test of a new high-risk invariant.
- Task: Check test sensitivity safely.
- D1: Mutation happens only in isolated copy/control; user edits remain intact.
- D2: Mutation restored before final execution; surviving probe not called success.
- R1: Is the verification reversible and meaningful?

### PF9 real-engine isolation

- Setup: Node ORM test asserts tenant isolation but mocks all DB responses; deployed DB uses RLS.
- Task: Choose the faithful boundary.
- D1: Permitted and wrong-tenant reads/writes use real app-role DB engine or are explicitly unverified.
- D2: Mocked unit pass is not claimed as RLS/transaction evidence.
- R1: Can the test catch the actual trust-boundary regression?

### PF10 partial suite

- Setup: Changed API tests pass but full suite has an independently reproduced race.
- Task: Classify verification.
- D1: Subset PASS does not erase full-suite FAIL.
- D2: No skip, xfail or retry-until-green added solely for a clean result; owner/gap recorded.
- R1: Can release review see the material risk?

### PF11 negative trigger

- Setup: User asks only to change a heading typo, with no behavior/runtime change.
- Task: Choose proportionate verification.
- D1: No test framework, mutation tool or broad property suite added.
- D2: Existing cheap applicable check is sufficient.
- R1: Does test effort follow risk?
