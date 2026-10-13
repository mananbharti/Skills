# backend: individual upgrade research

Research/authoring date: 2026-10-14. Read the current skill, all bundled resources,
existing workflow scenarios and frozen outcome protocol before editing.
Historical outcome files remain intact. New workflow cases are authored, not agent-executed.

## Baseline and narrow decision

The existing methodology remains useful. The missing failure branches are encoded in `skills/backend/references/boundary-cases.md` and a short conditional entrypoint pointer.
The previous maintainer ledger contained unattributed generalizations about 2026 agents.
Those entries are replaced here; they are not treated as measured evidence.

## Source-to-decision trace

| Source/access | Adopted decision | Rejected overreach / limitation |
| --- | --- | --- |
| [Receive Stripe events in your webhook endpoint](https://docs.stripe.com/webhooks); read 2026-10-14; Living documentation; no fixed API or SDK version adopted | Separate event receipt and business-effect deduplication; verify current state when needed. | Does not prove atomic local effects or tenant authorization. |
| [Row Security Policies](https://www.postgresql.org/docs/current/ddl-rowsecurity.html); read 2026-10-14; Page identifies PostgreSQL 18; check target engine/version separately | Run tenant read/write tests with the real application role. | Does not establish another database's isolation behavior. |
| [Webhook implementation](https://raw.githubusercontent.com/stripe/stripe-node/master/src/Webhooks.ts); read 2026-10-14; Moving master branch; inspected, not a pinned installed SDK | Use the installed provider SDK rather than custom signature parsing. | Signature verification does not supply a fulfillment ledger or authorize an order. |

All sources are primary documentation or upstream implementation. Upstream moving
branch inspection supports a mechanism, not the version installed in a user project.
No source assets/code were copied into the runtime package.

## Fifteen distinct failure situations

These are **local test hypotheses**, not measured prevalence or observed agent failures.
Source-supported mechanism is identified above; each concrete project situation still
needs its own fixture and execution. The list guides selective testing, not a mandatory checklist.

1. Repeated event ID repeats fulfillment.
2. Distinct event IDs describe one paid effect.
3. Paid event arrives before pending event.
4. Distinct events share created timestamp.
5. Crash occurs after effect before inbox marker.
6. Ingress acknowledges only an in-memory queue.
7. Signature verified after body mutation.
8. Valid signature references wrong provider account.
9. Client workspace ID used without membership.
10. Worker loses authenticated tenant scope.
11. Cache key omits tenant scope.
12. RLS tests use a bypass role.
13. Pool connection retains prior tenant setting.
14. Refund deduped with all events for one object.
15. Concurrent duplicate commands both pass app-level checks.

## Preserved and rejected material

Preserved the operating modes, evidence ladder, narrow scope and existing handoffs.
Rejected blanket tool/framework mandates and unmeasured superiority claims.
Conditional references keep specialized detail out of ordinary entrypoint context.
Authored cases use the existing Setup/Task/D#/R# protocol; static shape checks do
not grade their behavior. Existing outcome task/rubric freezes were not retuned.

## Verification and remaining evidence

Local command and observed outcome records are in `docs/upgrade/building-experience.json` (backend row).
No paid or live agent CLI was invoked. Local fixture/helper checks do not establish
comparative agent benefit, target host installation, production safety or physical-device coverage.

## Primary follow-through - 2026-10-14

[Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/), Malcolm Featonby / Amazon Web Services, accessed 2026-10-14; exact publication date
not established. Proposition: Same request identity with different parameters is a conflict; distinct intentional requests must not be collapsed merely because payloads match.
Decision: Bind idempotency keys to validated operation/tenant/intent; reject mismatches and preserve separate intentional commands.
Trace: `skills/backend/references/boundary-cases.md`.
Limits: current documentation guides the mechanism, not installed-version or
behavioral proof. Refresh on tool/provider version or contract change.
