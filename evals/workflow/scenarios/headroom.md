# Workflow scenarios — headroom

Authored 2026-09-14 (v1 campaign, Phase 10, zero-spend: no agent runs used).
Same contract as `signature-skills.md`: setup → task → candidate checks
(D#, deterministic where possible) → rubric dimensions (R#, qualitative,
graded blind). Authored ≠ executed: each scenario counts as coverage only
after a runner executes it against a real agent and stores raw results.

## headroom

### HR1 normal — growing workload, three levels

- Setup: 10k users today, 10× growth expected in a year, read-heavy workload, single region.
- Task: produce the Now/Next/Scale design.
- D1: all three levels present; each Next/Scale item carries a trigger metric (not a vibe).
- D2: load numbers shown with arithmetic (users → req/s at peak, units on everything).
- D3: at least one explicit "don't do yet" item.
- R1: are the gaps between levels the actual advice (what's deliberately deferred)?

### HR2 hard edge — tiny workload, restraint graded

- Setup: 50-user college project, maybe 500 next year, one developer.
- Task: design it without embarrassment.
- D1: Now level is proportionate; technologies may be named as rejected alternatives, without prescribing them.
- D2: no measured headroom multiplier is invented from user count; assumptions and limiting resource are explicit.
- D3: total response proportionate (no 200-line design doc for a class project).
- R1: did restraint read as competence or as dismissal?

### HR3 capability/failure — no numbers obtainable

- Setup: user cannot provide traffic, data size, or growth ("no idea, just make it scale").
- Task: design without numbers.
- D1: no cargo-cult numbers presented as the user's ("millions of requests" banned).
- D2: delivers the decision framework: the estimate ranges that would flip each choice + what to measure first.
- D3: unknowns labeled as estimates with visible arithmetic, conclusions stress-tested ("survives 10× off" or not, stated).
- R1: is the framework actionable the moment real numbers arrive?

### HR4 restraint — premature distribution request

- Setup: 200 daily users; user asks "should we split into microservices".
- Task: answer the question, not the ambition.
- D1: verdict is "no" with the trigger that WOULD justify the split (metric + threshold), not a lecture.
- D2: offers what to do instead now (modular monolith seams that keep the option cheap).
- D3: no resume-driven patterns smuggled in as "best practice".
- R1: does the "no" preserve the user's dignity and future options?

### HR5 adversarial — "design for a billion users"

- Setup: side project with 100 users; user demands billion-user architecture "to be safe".
- Task: hold proportionality under fantasy-scale pressure.
- D1: no billion-user machinery recommended for today (sharding/event-sourcing/multi-region all land in Scale-or-later with triggers, or "don't do yet").
- D2: arithmetic shown proving the gap (current load vs claimed scale, orders of magnitude apart).
- D3: response doesn't mock; it redirects to the real risks (the single box's actual failure modes).
- R1: did the design stay honest without condescension?

Upgrade cases authored 2026-10-14. All cases below remain unexecuted against
independent agents; D# checks are acceptance definitions, not observed passes.

### HR6 backlog recovery

- Setup: Bundled capacity-case.json: queue 9000 jobs, current arrivals 20/s, completions 15/s, candidate completion rate 35/s; all values assumed for planning.
- Task: Compare recovery options with units and limits.
- D1: Current scenario has no finite drain time; candidate estimate is 9000/(35-20)=600 seconds.
- D2: Inputs remain assumed; retry/startup/dependency limits are explicit exclusions.
- R1: Does the model retain unknowns that could reverse the recommendation?

### HR7 generator confound

- Setup: An open-load report schedules 100/s but starts 60/s and drops 40/s; a closed test reports low p95.
- Task: Interpret capacity evidence before sizing.
- D1: Scheduled, achieved, dropped and completed counts stay separate.
- D2: Low closed-test p95 is not used as proof of 100/s capacity.
- R1: Can the generator limit be distinguished from the service?

### HR8 autoscaler lag

- Setup: Kubernetes app has not-ready pods, missing CPU metrics and a fixed downstream DB pool.
- Task: Plan safe launch capacity.
- D1: Ready capacity and autoscaler demand differ; missing metrics not assumed healthy.
- D2: Replica recommendation includes downstream cap, readiness delay and bounded experiment.
- R1: Does the plan address the resource that binds first?

### HR9 workload class

- Setup: `benchmarks/fixtures/ts-dashboard`; product adds exports to cheap reads and reports aggregate request count only.
- Task: Build conditional workload model.
- D1: Reads/exports, payload and DB connection demand are segmented.
- D2: Unknown export service time gets a measurement plan rather than invented capacity.
- R1: Does an aggregate average hide the expensive class?

### HR10 tenant burst

- Setup: Single Python API tenant accounts for most exports during a known burst; retries compete with interactive traffic.
- Task: Choose Now/Next/Scale controls.
- D1: Fairness, admission/retry budget and deadline identify what work may be deferred.
- D2: No new service split without an evidenced ownership/isolation trigger.
- R1: Does the simplest design protect the interactive objective?

### HR11 negative trigger

- Setup: A slow pure pricing function has a profiler showing repeated scans; no demand forecast requested.
- Task: Route the known bottleneck.
- D1: hotpath owns measured code diagnosis; no system-sizing exercise.
- D2: No replicas/cache/cloud spend recommended from the symptom alone.
- R1: Is the handoff useful?
