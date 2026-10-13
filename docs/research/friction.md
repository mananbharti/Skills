# friction: individual upgrade research

Research/authoring date: 2026-10-14. Read the current skill, all bundled resources,
existing workflow scenarios and frozen outcome protocol before editing.
Historical outcome files remain intact. New workflow cases are authored, not agent-executed.

## Baseline and narrow decision

The existing methodology remains useful. The missing failure branches are encoded in `skills/friction/references/recovery-journeys.md` and a short conditional entrypoint pointer.
The previous maintainer ledger contained unattributed generalizations about 2026 agents.
Those entries are replaced here; they are not treated as measured evidence.

## Source-to-decision trace

| Source/access | Adopted decision | Rejected overreach / limitation |
| --- | --- | --- |
| [Understanding Redundant Entry](https://www.w3.org/WAI/WCAG22/Understanding/redundant-entry.html); read 2026-10-14; WCAG 2.2 explanatory guidance; no conformance claim adopted | Test entered-value preservation and recovery in the relevant process. | Does not require saving sensitive data persistently in all forms. |
| [Offline data](https://web.dev/learn/pwa/offline-data); read 2026-10-14; Living tutorial with IndexedDB examples; not a required library | Distinguish local storage from remote confirmation; test failed storage and privacy boundaries. | Its example can insert duplicate rows if repeated; it is not a synchronization/conflict protocol. |

All sources are primary documentation or upstream implementation. Upstream moving
branch inspection supports a mechanism, not the version installed in a user project.
No source assets/code were copied into the runtime package.

## Fifteen distinct failure situations

These are **local test hypotheses**, not measured prevalence or observed agent failures.
Source-supported mechanism is identified above; each concrete project situation still
needs its own fixture and execution. The list guides selective testing, not a mandatory checklist.

1. Timed-out save shown as confirmed.
2. Retry creates repeated purchase.
3. Offline draft confused with server state.
4. Validation erases entered fields.
5. Session expiry loses recoverable draft.
6. Logout exposes prior user draft.
7. Workspace switch reveals prior tenant cache.
8. Storage quota failure hidden from user.
9. Reconnect overwrites newer work.
10. Mobile keyboard covers next step.
11. Back navigation destroys progress.
12. Error copy offers unsafe repeated submit.
13. Audit-only task changes production policy.
14. Static inspection called novice walk.
15. Conversion gain invented from one internal walkthrough.

## Preserved and rejected material

Preserved the operating modes, evidence ladder, narrow scope and existing handoffs.
Rejected blanket tool/framework mandates and unmeasured superiority claims.
Conditional references keep specialized detail out of ordinary entrypoint context.
Authored cases use the existing Setup/Task/D#/R# protocol; static shape checks do
not grade their behavior. Existing outcome task/rubric freezes were not retuned.

## Verification and remaining evidence

Local command and observed outcome records are in `docs/upgrade/building-experience.json` (friction row).
No paid or live agent CLI was invoked. Local fixture/helper checks do not establish
comparative agent benefit, target host installation, production safety or physical-device coverage.

## Verification 2026-10-14

| Basis | Outcome |
| --- | --- |
| W3C WCAG 2.2 SC 3.3.8 + F109; fetched 2026-10-14 | Paste-blocking in auth set as blocker; Knight case kept analogical, not encoded as UX precedent. |
