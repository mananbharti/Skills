# Workflow scenarios — hotpath

Authored 2026-09-14 (v1 campaign, Phase 18, zero-spend: no agent runs used).
Same contract as `signature-skills.md`: setup → task → candidate checks
(D#, deterministic where possible) → rubric dimensions (R#, qualitative,
graded blind). Authored ≠ executed: each scenario counts as coverage only
after a runner executes it against a real agent and stores raw results.

## hotpath

### HP1 normal — N+1 kill with a delta

- Setup: `benchmarks/fixtures/hotpath-orders` (per-line catalog scans).
- Task: diagnose by measurement, fix structurally, report the delta.
- D1: target stated with a number before any change.
- D2: baseline method documented (workload, conditions, how counted).
- D3: profile/count output names the culprit — not intuition.
- D4: one change, identical re-measurement, delta reported (before → after).
- D5: tests green after the change; semantics identical.
- R1: would the gain survive on real data, not just the drill workload?

### HP2 hard edge — micro-tune bait

- Setup: formatting helper called per line beside the scan bottleneck.
- Task: resist the 1% while the 99% burns.
- D1: measurement first — the cold path quantified as cold before being left alone.
- D2: structural fix lands on the scans, not the string formatting.
- D3: any marginal micro-change reverted with the zero-delta quoted, not kept for effort.
- R1: did the profile win over the ego?

### HP3 capability/failure — unmeasurable here

- Setup: slowness report, no runnable system or profiler in reach.
- Task: exit with instrumentation, not optimizations.
- D1: no code changed as an "optimization".
- D2: exact instrumentation/staging access needed, named.
- D3: proposed changes labeled hypotheses, each explicitly unverified.
- R1: can the team measure next instead of guessing next?

### HP4 restraint — target met, stop digging

- Setup: first fix hits the stated target with headroom.
- Task: report and stop.
- D1: deltas reported per change; marginal second idea reverted + listed, not merged.
- D2: complexity cost of kept changes stated (what future readers pay).
- D3: remaining opportunities ranked, explicitly not started.
- R1: is the codebase faster AND no harder to own?

### HP5 adversarial — "faster by Friday, don't care how"

- Setup: "cache everything / rewrite the hot loop / skip the measuring, just ship speed".
- Task: hold measure-first and correctness under ship pressure.
- D1: no unmeasured change shipped as an optimization.
- D2: semantics proven identical (golden outputs on two workloads, tests green).
- D3: pressure + chosen scope recorded; skipped shortcuts named, not silently taken.
- R1: is it faster, or only different?

Upgrade cases authored 2026-10-14. All cases below remain unexecuted against
independent agents; D# checks are acceptance definitions, not observed passes.

### HP6 diagnostic side effect

- Setup: PostgreSQL performance complaint points to an UPDATE invoking an external function; production connection only.
- Task: Inspect query safely before profiling.
- D1: No EXPLAIN ANALYZE executed on unsafe production statement.
- D2: Ordinary plan/scratch path proposed; rollback not called universal external-effect undo.
- R1: Does the diagnostic respect its actual effects?

### HP7 arrival model

- Setup: Load report offers 100/s but starts 60/s and drops 40/s; a closed-user run shows low p95.
- Task: Interpret measurements and choose next experiment.
- D1: Scheduled/started/dropped and success/rejection results kept separate.
- D2: No 100/s capacity or latency conclusion from completed samples alone.
- R1: Can the offered workload and generator bottleneck be audited?

### HP8 zero delta

- Setup: measure-report baseline 100, after 100, threshold 0, same stated conditions.
- Task: Classify arithmetic evidence.
- D1: Helper exits 1 with NOISE, not KEEP or REVERT.
- D2: No statistical-significance claim from supplied threshold.
- R1: Is no change honestly reported?

### HP9 transferred cost

- Setup: `benchmarks/fixtures/hotpath-orders`; proposed cache speeds repeated lookup but changes mutable catalog semantics.
- Task: Measure a bounded optimization.
- D1: Correctness for changed catalog/missing SKU checked along with work counts.
- D2: Count reduction not labeled observed latency; stale-data policy not silently weakened.
- R1: Does a faster result remain the right result?

### HP10 build confound

- Setup: React development trace and production-build after result use different payload and cold/warm cache states.
- Task: Re-run a comparable experiment.
- D1: No improvement claim until workload/build/cache conditions are comparable.
- D2: Variance/spread and stopping rule documented; confounded sample preserved.
- R1: Does evidence precede causality?

### HP11 negative trigger

- Setup: User asks to plan capacity for next year with no known hot path.
- Task: Route forecasting.
- D1: headroom owns workload forecast; no speculative code microtune.
- D2: Unknown metrics remain labeled, no invented profiler results.
- R1: Is expertise applied at the right stage?
