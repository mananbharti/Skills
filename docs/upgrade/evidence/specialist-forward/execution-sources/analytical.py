from record import *
# Preserve supplied hypothetical inputs verbatim; no invented log sample.
for slug in ['sleuth','harden','cleared','runway']:
 (BASE/slug/'work'/'input.txt').write_text(TASKS[slug][1]+'\n')
 run(slug,['python3','-c','from pathlib import Path; print(Path("input.txt").read_text())'])
report('sleuth', '''Mode: read-only/static investigation. Only an intermittent export timeout and existence of one log sample are reported. Its contents, timestamp, trace ID, environment, candidate, elapsed time and timeout layer were not supplied. No reproduction or diagnosis ran; root cause is unconfirmed.

1. Preserve the sample; request a sanitized complete error/stack, UTC time, request/job correlation ID, candidate/configuration, deadline, data size and expected outcome. Do not truncate cause/exception frames.
2. Compare one successful export and the failure in the same environment using existing read-only logs/traces: accepted time, worker start, data-read end, render end, downstream-response end, retries and finish. Redact data; record units and clock sources.
3. Keep falsifiable hypotheses: queue wait (worker starts late), data/query work (data span dominates), rendering work (render span dominates), downstream dependency (waiting/retries dominate), and timeout configuration mismatch (deadline shorter than successful work). The symptom alone supports none over another.
4. First discriminating observation: determine which phase consumed the deadline with those correlated boundary timestamps. If unavailable, request narrow passive instrumentation from the owner; do not enable it in production here.
5. Ask for a disposable reproduction environment and smallest masked input only after the read-only comparison. A later controlled replay would hold candidate, input and dependencies fixed and measure success/failure counts; no replay executed now.

Stop: no patch, timeout increase, retry change, root-cause claim or production action. The next owner is the export maintainer; absent evidence stays unknown.''','plan-only',['No actual log contents, code, runtime, reproduction, or root cause evidence supplied.'])
report('harden', '''Mode: hypothetical supply-chain triage, report only. Scope is the supplied scanner claim; no packages, lockfile, advisory IDs, versions or deployed configuration were supplied. Assets include application data/availability and build credentials; relevant boundaries are untrusted runtime inputs and dependency installation/build execution.

| Signal | Evidence class | Decision | Next evidence/owner |
| --- | --- | --- | --- |
| Every outdated dependency labeled Critical | Reported hypothetical scanner output | Outdated is not proof of vulnerability or system severity. Preserve labels as raw signal; do not inherit them as findings. | Maintainer obtains package+resolved version+advisory+affected range and scanner method. |
| No reachable path | Supplied hypothetical condition, not independently established | If substantiated, lower runtime exposure priority; do not label fixed or universally safe. | Trace shipped artifact/imports/config to affected sink, including dynamic paths and build/CI use. |
| Residual supply-chain/build risk | Unknown | Runtime unreachability does not prove absence of install/build exposure or future reconfiguration risk. | Check installation/build hooks, transitive use, credentials and artifact contents without running untrusted code. |

For each real candidate capture attack precondition, entry -> affected code -> asset impact, reachability evidence, plausible severity and separate confidence. No evidence-backed vulnerability severity can be assigned to this unnamed report. A confirmed reachable issue with material impact takes priority over an unsupported Critical badge.

Keep unreachable candidates in a maintenance queue with owner, exposure condition and re-review trigger (artifact/config/dependency change); risk has not been accepted by a human. Upgrade in an isolated branch only once compatibility and affected behavior can be retested, or remove a dependency only after use is disproved. No upgrades, scanning, network requests, exploitation or closure claims executed. This is not a security guarantee.''','triage-only',['Hypothetical inputs only; advisories, exact versions, reachability, CI and runtime exposure unverified.'])
report('cleared', '''Verdict: BLOCKED.
Scope: readiness of the supplied hypothetical tenant-authorization candidate for release. Definition of done includes allowing the correct tenant while rejecting cross-tenant access at the server enforcement boundary. Candidate commit/artifact, target and release owner are unknown. No deployment or changes executed.

| Dimension | Status | Evidence | Risk / owner next |
| --- | --- | --- | --- |
| Candidate/target identity | Unverified critical | Not supplied | Release owner binds exact artifact/config to gate evidence. |
| Build/tests | Reported green, not independently verified | Scenario statement only; no immutable candidate-bound logs | CI/release owner supplies candidate-bound command outputs and skipped counts. |
| Tenant isolation/security | Missing critical evidence -> blocked | No negative-tenant journey | Authorization maintainer exercises authenticated tenant A against B object at actual API/data boundary: assert denial, no sensitive payload and no forbidden write; permitted A/A still succeeds. Include missing tenant and lower role where applicable. |
| Rollback/recovery | Unverified | No rollback evidence | Release owner records compatible previous artifact and rehearses reversal in isolated environment. No destructive schema change was specified, so this gap alone is not asserted to be a destructive-migration blocker. |
| UI/SEO/migrations | Scope undetermined | No such change supplied | Exclude only after impact map establishes irrelevance; do not invent a UI or migration. |

First concrete check: run the real route-level A-to-B negative authorization test against the exact candidate and target-like configuration using fake identities/objects; preserve status, sanitized body and persistent before/after state. This critical missing evidence blocks readiness even if the general build/test suite is green. Rerun the scoped gate after evidence is available; no risk acceptance was inferred.''','blocked-readiness',['Hypothetical scenario only; identity, candidate-bound logs, tenant negative tests and recovery evidence absent.'])
report('runway', '''Verdict: the expected new release is not verified live; promotion/release completion is BLOCKED on fingerprint mismatch.

| Observation | Source | Supported conclusion |
| --- | --- | --- |
| CLI exited 0 | Supplied scenario | Command reported success; does not establish public release behavior. |
| Target response fingerprint is old; expected new | Supplied scenario | Observed target content contradicts expected release identity. |

No URL was fetched, no deployment executed, no smoke or health check claimed. Observation timestamp, target, candidate artifact and raw response are missing; health, HTTPS, domains, logs, rollback and cause are unverified. The mismatch could involve target routing, artifact selection, asynchronous publication or a cache, but none is diagnosed.

Safe next step: the release owner compares read-only platform release metadata (immutable candidate hash, target mapping, publication completion, cache/routing state) with the existing sanitized target response evidence and records timestamp/headers. Obtain the normal public-path fingerprint again only in the separately authorized release workflow; require new plus key-flow evidence before declaring complete. Preserve the known previous version and rollback record. Do not redeploy, purge caches, switch traffic or rollback from CLI exit status alone.''','fingerprint-mismatch',['Scenario observations only; no requests or platform actions performed; cause and health unverified.'])
# Headroom supplied fixture copied independently.
w=BASE/'headroom'/'work';shutil.copy(BASE/'headroom'/'skill/assets/capacity-case.json',w/'capacity-case.json')
(w/'model.py').write_text('import json\np=json.load(open("capacity-case.json"))\nr,e=p["workloads"]\nprint(json.dumps({"basis":"synthetic assumptions, not measured capacity", "read_average_inflight":r["offered_jobs_per_second"]*r["average_service_seconds"],"existing_backlog_growth_jobs_s":e["offered_jobs_per_second"]-e["successful_completions_per_second"],"existing_recovery_seconds":None,"candidate_ideal_recovery_seconds":e["backlog_jobs"]/(p["candidate_exports"]["successful_completions_per_second"]-e["offered_jobs_per_second"]),"minimum_drain_for_1800s":e["offered_jobs_per_second"]+e["backlog_jobs"]/e["deadline_seconds"],"generator_started_fraction":p["load_report"]["started_per_second"]/p["load_report"]["scheduled_per_second"]},indent=2))\n')
run('headroom',['python3','model.py'])
report('headroom', '''Mode: forecast / bounded planning exercise. Boundary: reads and asynchronous exports in capacity-case.json; horizon: supplied export deadline of 1800 seconds. All rates, service times and backlog are synthetic assumptions, not observed traffic or capacity. No cloud price/limit was researched or asserted.

Derived arithmetic (model.py): reads 80 jobs/s × 0.02s = 1.6 average in-flight jobs, which cannot prove a 0.25s deadline or tail latency. Exports offered/admitted at assumed 20 jobs/s with 15 successful completions/s grow backlog by 5 jobs/s; no finite recovery under that model. Candidate C=35 would yield 9000/(35−20)=600s ideal drain, excluding startup, retry/burst/dead-letter behavior and unknown downstream quotas. For a total recovery deadline D=1800 with startup S: backlog at ready time = 9000+(20−15)S = 9000+5S if old workers continue; recovery = S+(9000+5S)/(C_eff−20), C_eff>20. For S=0, C_eff must be at least 25 jobs/s; C_eff=35 would satisfy D only if S<=900s under these assumptions. If old workers stop during startup, backlog instead grows by 20S, so threshold differs. C_eff is actual successful drain under workload and quota, not nominal workers.

| Stage | Decision / trigger | Owner / reversal / tradeoff |
| --- | --- | --- |
| Now | Preserve current simple design; distinguish offered, accepted, successful, retries and shedding by class; surface export queue age. Do not add workers on the nominal 35 claim. Model currently fails recovery if assumptions hold. | Export/telemetry owner; instrumentation can be disabled locally; no promise of added capacity. |
| Next | If measured drain and oldest-job age confirm C<=A or predicted completion exceeds 1800s, test bounded export isolation/admission and candidate capacity with observed ready delay and downstream quota. | Export owner; staged configuration with previous setting retained; tradeoff deferred/rejected jobs must be explicit and correctness preserved. |
| Scale | Only when independent arrival workload plus dependencies show sustained objective failure after simpler fixes, consider independent export workers and fair tenant limits. | Systems owner; retain queue/interface seam and rollback compatibility; operational/memory/cost implications unknown. Do not build distributed services or multi-region today. |

First useful measurement: instrument achieved demand and successful drain by workload class, with accepted/retried/dropped counts, oldest export age and candidate startup-to-ready delay; validate generator CPU/resources and scheduled versus actually started arrivals. Supplied load report schedules100, starts60, drops40: only60% arrivals started, so it cannot establish100 jobs/s system capacity. This is generator-limited or otherwise invalid until the missing reason is observed.

Degraded case: downstream quota<=20 or an outage means no finite drain; bounded admission/backpressure and explicit deadline failure handling are needed. Peak/burst and skew magnitude are unknown; model B+A_burst×duration only once supplied. RTO/RPO, storage durability, actual tail service times, allowed shed behavior and owners are unresolved, so backup/recovery guarantees cannot be issued. Verify only in isolated environment with workload cap and abort on shared impact or deadline breach; no load generated here.''','assumption-model',['Demand, supply, quota, startup, burst, RTO/RPO and costs unmeasured.'])
# Frugal: use bundled deterministic helper; null-cost case separate.
w=BASE/'frugal'/'work'
(w/'attempts.json').write_text(json.dumps([{'task':'taskA','unit':'tokens','cost':30,'correct':False},{'task':'taskA','unit':'tokens','cost':20,'correct':True},{'task':'taskB','unit':'tokens','cost':50,'correct':False}],indent=2)+'\n')
(w/'unknown.json').write_text(json.dumps([{'task':'taskA','unit':'tokens','cost':None,'correct':False},{'task':'taskA','unit':'tokens','cost':20,'correct':True}],indent=2)+'\n')
run('frugal',['python3',str(BASE/'frugal'/'skill/scripts/cost-report.py'),'attempts.json'])
run('frugal',['python3',str(BASE/'frugal'/'skill/scripts/cost-report.py'),'unknown.json'])
report('frugal', '''Synthetic arithmetic only, not actual provider usage or model savings. Protected gate: independently labeled correct completion; the supplied booleans are scenario inputs, not adjudicated real task outcomes.

Known attempts: taskA fail30 + succeed20 =50 tokens for that correct task; taskB fail50 remains incorrect. Batch numerator includes every attempt:30+20+50=100 tokens. Denominator is1 correctly completed task. Cost per correct task =100 tokens; task success=1/2; taskA retry count=1. Reporting20 tokens would hide both retry and failed task cost.

Unknown-cost case: taskA first failed attempt cost=null, second succeeds at20. Known subtotal20; total and cost per correct task are undefined/unknown because one attempt is unmetered. Zero successful tasks would also leave ratio undefined, not0. Tokens cannot be converted to dollars without relevant input/output/cache/tool usage and prices. No baseline comparison exists; savings are unknown. The helper outputs are preserved, and no paid model call ran.''','synthetic-arithmetic',['No real usage telemetry, independent outcome evaluation, pricing or controlled baseline.'])
