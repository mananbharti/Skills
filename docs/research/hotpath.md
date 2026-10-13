# hotpath: individual upgrade research

Research/authoring date: 2026-10-14. Read the current skill, all bundled resources,
existing workflow scenarios and frozen outcome protocol before editing.
Historical outcome files remain intact. New workflow cases are authored, not agent-executed.

## Baseline and narrow decision

The existing methodology remains useful. The missing failure branches are encoded in `skills/hotpath/references/experiment-hazards.md` and a short conditional entrypoint pointer.
The previous maintainer ledger contained unattributed generalizations about 2026 agents.
Those entries are replaced here; they are not treated as measured evidence.

## Source-to-decision trace

| Source/access | Adopted decision | Rejected overreach / limitation |
| --- | --- | --- |
| [EXPLAIN](https://www.postgresql.org/docs/current/sql-explain.html); read 2026-10-14; Page identifies PostgreSQL 18; verify target DB version | Inspect side effects and prefer safe scratch execution or ordinary planning. | Rollback does not guarantee every external/nontransactional effect is reversible. |
| [Open and closed models](https://grafana.com/docs/k6/latest/using-k6/scenarios/concepts/open-vs-closed/); read 2026-10-14; Living docs; no installed generator version adopted | Retain offered load and result classes when interpreting latency. | Does not choose a universal load model. |
| [Constant arrival executor implementation](https://raw.githubusercontent.com/grafana/k6/master/lib/executor/constant_arrival_rate.go); read 2026-10-14; Moving master branch; not a pinned tested generator | Check generator capacity alongside target capacity. | Does not establish application latency or comparative skill lift. |

All sources are primary documentation or upstream implementation. Upstream moving
branch inspection supports a mechanism, not the version installed in a user project.
No source assets/code were copied into the runtime package.

## Fifteen distinct failure situations

These are **local test hypotheses**, not measured prevalence or observed agent failures.
Source-supported mechanism is identified above; each concrete project situation still
needs its own fixture and execution. The list guides selective testing, not a mandatory checklist.

1. EXPLAIN ANALYZE modifies live rows.
2. Rollback assumed to undo external function call.
3. Closed load reduces demand as latency rises.
4. Dropped arrivals omitted from results.
5. Only successful latency hides rejected work.
6. Zero delta with zero threshold labeled REVERT.
7. Helper threshold called statistical significance.
8. Cold and warm runs compared as equivalent.
9. Dataset/query parameters drift between runs.
10. Index fix increases writes/storage beyond budget.
11. Cache speedup weakens tenant scope.
12. Background offload transfers latency into queue age.
13. Microtune retained despite noise.
14. Operation count labeled measured user speedup.
15. Dev build profile called production field evidence.

## Preserved and rejected material

Preserved the operating modes, evidence ladder, narrow scope and existing handoffs.
Rejected blanket tool/framework mandates and unmeasured superiority claims.
Conditional references keep specialized detail out of ordinary entrypoint context.
Authored cases use the existing Setup/Task/D#/R# protocol; static shape checks do
not grade their behavior. Existing outcome task/rubric freezes were not retuned.

## Verification and remaining evidence

Local command and observed outcome records are in `docs/upgrade/building-experience.json` (hotpath row).
No paid or live agent CLI was invoked. Local fixture/helper checks do not establish
comparative agent benefit, target host installation, production safety or physical-device coverage.
