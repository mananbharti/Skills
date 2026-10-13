# headroom: individual upgrade research

Research/authoring date: 2026-10-14. Read the current skill, all bundled resources,
existing workflow scenarios and frozen outcome protocol before editing.
Historical outcome files remain intact. New workflow cases are authored, not agent-executed.

## Baseline and narrow decision

The existing methodology remains useful. The missing failure branches are encoded in `skills/headroom/references/workload-experiments.md` and a short conditional entrypoint pointer.
The previous maintainer ledger contained unattributed generalizations about 2026 agents.
Those entries are replaced here; they are not treated as measured evidence.

## Source-to-decision trace

| Source/access | Adopted decision | Rejected overreach / limitation |
| --- | --- | --- |
| [Horizontal Pod Autoscaling](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/); read 2026-10-14; Living docs; no controller version adopted | Model ready-capacity delay and downstream caps when Kubernetes is present. | Does not require Kubernetes or a universal utilization target. |
| [Replica calculator implementation](https://raw.githubusercontent.com/kubernetes/kubernetes/master/pkg/controller/podautoscaler/replica_calculator.go); read 2026-10-14; Moving master branch; not a deployed controller version | A desired replica count is not immediate usable capacity. | Does not predict this application's throughput. |
| [Open and closed models](https://grafana.com/docs/k6/latest/using-k6/scenarios/concepts/open-vs-closed/); read 2026-10-14; Living docs; no installed k6 version adopted | Match workload model to arrival contract; retain offered and dropped demand. | Does not make open load universally preferable for fixed-user journeys. |

All sources are primary documentation or upstream implementation. Upstream moving
branch inspection supports a mechanism, not the version installed in a user project.
No source assets/code were copied into the runtime package.

## Fifteen distinct failure situations

These are **local test hypotheses**, not measured prevalence or observed agent failures.
Source-supported mechanism is identified above; each concrete project situation still
needs its own fixture and execution. The list guides selective testing, not a mandatory checklist.

1. Closed load model hides overload by slowing arrivals.
2. Dropped generator iterations omitted.
3. CPU average hides expensive export class.
4. Single tenant burst starves other tenants.
5. Retry fanout exceeds provider quota.
6. Consumers drain no faster than arrivals.
7. Queue depth used without age/deadline.
8. Ready-capacity lag omitted during peak.
9. Missing autoscaler metrics assumed zero need.
10. New replicas exhaust DB pool.
11. Primary writes scaled by adding read replicas.
12. Cache hit average hides critical miss route.
13. RTO claim omits restore duration.
14. Scenario estimate reported as measured throughput.
15. Service split prescribed without bottleneck evidence.

## Preserved and rejected material

Preserved the operating modes, evidence ladder, narrow scope and existing handoffs.
Rejected blanket tool/framework mandates and unmeasured superiority claims.
Conditional references keep specialized detail out of ordinary entrypoint context.
Authored cases use the existing Setup/Task/D#/R# protocol; static shape checks do
not grade their behavior. Existing outcome task/rubric freezes were not retuned.

## Verification and remaining evidence

Local command and observed outcome records are in `docs/upgrade/building-experience.json` (headroom row).
No paid or live agent CLI was invoked. Local fixture/helper checks do not establish
comparative agent benefit, target host installation, production safety or physical-device coverage.

Source access limitation: AWS queue-backlog URL redirected to a page with no extracted body.
It was not used to substantiate new arithmetic or timing claims.
