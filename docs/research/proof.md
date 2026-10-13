# proof: individual upgrade research

Research/authoring date: 2026-10-14. Read the current skill, all bundled resources,
existing workflow scenarios and frozen outcome protocol before editing.
Historical outcome files remain intact. New workflow cases are authored, not agent-executed.

## Baseline and narrow decision

The existing methodology remains useful. The missing failure branches are encoded in `skills/proof/references/result-semantics.md` and a short conditional entrypoint pointer.
The previous maintainer ledger contained unattributed generalizations about 2026 agents.
Those entries are replaced here; they are not treated as measured evidence.

## Source-to-decision trace

| Source/access | Adopted decision | Rejected overreach / limitation |
| --- | --- | --- |
| [How to use skip and xfail](https://docs.pytest.org/en/stable/how-to/skipping.html); read 2026-10-14; Living stable docs; verify installed runner/config names | Report selected, executed, skipped and expected-failure outcomes separately. | A green process is not evidence skipped behavior works. |
| [Skipping and expected-failure implementation](https://raw.githubusercontent.com/pytest-dev/pytest/main/src/_pytest/skipping.py); read 2026-10-14; Moving main branch; not installed pytest evidence | Review reason and strict behavior rather than silently greening failures. | Does not authorize quarantine, external issue creation or broad mutation. |

All sources are primary documentation or upstream implementation. Upstream moving
branch inspection supports a mechanism, not the version installed in a user project.
No source assets/code were copied into the runtime package.

## Fifteen distinct failure situations

These are **local test hypotheses**, not measured prevalence or observed agent failures.
Source-supported mechanism is identified above; each concrete project situation still
needs its own fixture and execution. The list guides selective testing, not a mandatory checklist.

1. Zero tests selected called verified.
2. Skipped behavior included as passed.
3. Expected failure treated as working feature.
4. Non-strict unexpected pass silently accepted.
5. Regression red is import error rather than assertion.
6. Mutation damages dirty user worktree.
7. Mutant not restored before final verification.
8. Test setup already satisfies assertion.
9. DB locking mocked in transaction test.
10. Wrong tenant route tested only via hidden UI.
11. Race retried until green.
12. Coverage padded with tautology.
13. Migration down reverses newly written data.
14. Property generator lacks interpretable shrink failure.
15. Subset green erases full-suite failure.

## Preserved and rejected material

Preserved the operating modes, evidence ladder, narrow scope and existing handoffs.
Rejected blanket tool/framework mandates and unmeasured superiority claims.
Conditional references keep specialized detail out of ordinary entrypoint context.
Authored cases use the existing Setup/Task/D#/R# protocol; static shape checks do
not grade their behavior. Existing outcome task/rubric freezes were not retuned.

## Verification and remaining evidence

Local command and observed outcome records are in `docs/upgrade/building-experience.json` (proof row).
No paid or live agent CLI was invoked. Local fixture/helper checks do not establish
comparative agent benefit, target host installation, production safety or physical-device coverage.

## Verification 2026-10-14

| Basis | Outcome |
| --- | --- |
| git-bisect manual (exit contract); fetched 2026-10-14 | Mapped 0/1-127/125 outcomes into result semantics for automated failing signals. |
