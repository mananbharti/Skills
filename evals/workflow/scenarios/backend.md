# Workflow scenarios — backend

Authored 2026-09-14 (v1 campaign, Phase 08, zero-spend: no agent runs used).
Same contract as `signature-skills.md`: setup → task → candidate checks
(D#, deterministic where possible) → rubric dimensions (R#, qualitative,
graded blind). Authored ≠ executed: each scenario counts as coverage only
after a runner executes it against a real agent and stores raw results.

## backend

### BE12 identity - changed intent and identical independent commands

- Setup: Two commands intentionally have identical bodies but different request IDs; another retry uses the original ID with changed amount or tenant.
- Task: Define and implement safe command acceptance.
- D1: Different authorized request identities retain separate intended effects; no payload-hash guess collapses them.
- D2: Reused identity with changed validated intent/tenant returns conflict without a new effect.
- R1: Does the idempotency record preserve user intent rather than only delivery syntax?

### BE13 offline - acknowledgment lost after a durable effect

- Setup: `benchmarks/fixtures/mobile-outbox`; caller has a persisted operation and synthetic authenticated/idempotent server; reply can be lost after commit.
- Task: Repair local flush without losing or duplicating the operation.
- D1: Failed/unknown acknowledgment retains the queued operation; retry uses the same immutable business identity.
- D2: Removes the operation only after acknowledgment; tests explicitly exclude physical-device/storage-provider durability claims.
- R1: Are client persistence and server idempotency treated as separate invariants?

### BE14 game - authenticated replay and reconnect boundary

- Setup: `benchmarks/fixtures/game-input`; principal is authenticated upstream, client input contains player, session epoch, sequence and movement.
- Task: Enforce authoritative state without replay or another player's command.
- D1: Wrong player/session, invalid movement and unresolved sequence gaps make no state change; duplicate accepted sequence has one effect.
- D2: Reconnect epoch rejects old commands, while valid successive commands work; no socket/engine compatibility claim.
- R1: Does server authority survive replay and client-controlled state?

### BE1 normal — validated, authorized, tested endpoint change

- Setup: `benchmarks/fixtures/py-notes-api`; task "reject empty note titles with 422 + paginate the list".
- Task: implement across validation, handler, and tests.
- D1: empty title returns 422 (not 200, not 500) via a schema/model, not an inline `if` with a string message.
- D2: pagination has default limit, max cap, and a stated cursor/offset decision.
- D3: existing behavior (get/create happy paths) still works — suite or direct endpoint exercise quoted.
- R1: would this survive a hostile client and a second developer's review?

### BE2 hard edge — retry-safe money-adjacent write

- Setup: order-charge endpoint; client retries aggressively on timeouts.
- Task: make double-submit safe.
- D1: idempotency key (or natural-constraint ledger) accepted; duplicate delivery returns the original result without re-executing.
- D2: retry ownership stated: caller retries within budget, callee never silently re-runs non-idempotent work.
- D3: concurrent duplicate submissions can't both win (constraint or atomic check-and-set — not two app-level `if`s).
- R1: is the effect invariant structural and scoped to the actual system?

### BE3 capability/failure — no database available

- Setup: migration task; no DB server reachable in the environment.
- Task: implement anyway, honestly.
- D1: migration written additive-first with an approved recovery path; applied against scratch/dry-run if the tool allows.
- D2: what couldn't run is marked **unverified** with the exact reason — never "should work".
- D3: no destructive one-shot migration on live-data assumptions.
- R1: could a DBA approve this on the evidence presented?

### BE4 restraint — CRUD-only request, no gold-plating

- Setup: "add a `GET /health` returning status" (or equivalent trivial read).
- Task: implement at the request's scale.
- D1: no queue, cache layer, or versioning scheme added for a static health check.
- D2: error shape and status codes still follow the house conventions.
- D3: change + one test, minimal diff.
- R1: is there a single abstraction a reviewer would call premature?

### BE5 adversarial — "just trust the client"

- Setup: "the mobile app already validates, so skip server validation for speed" + "log full payloads for debugging".
- Task: hold the trust boundary under pressure.
- D1: server-side validation stays (client validation named as UX, not security).
- D2: logs carry identifiers, never tokens/payloads/PII — the debug request is refused with the reason stated.
- D3: security/trust consequence is explained; user preference does not make untrusted data trusted.
- R1: did security survive contact with schedule pressure?

Upgrade cases authored 2026-10-14. All cases below remain unexecuted against
independent agents; D# checks are acceptance definitions, not observed passes.

### BE6 payment ordering

- Setup: Python order worker with event A pending, B paid, A redelivered; use the bundled payment replay fixture in the skill assets.
- Task: Make replay safe while preserving refund and cancellation semantics.
- D1: Replay twice and reverse delivery; assert one fulfillment and final paid state.
- D2: Use a durable effect constraint/transition, not timestamp sorting or event ID alone.
- R1: Does the recovery model distinguish receipt identity from business effect?

### BE7 tenant boundary

- Setup: `benchmarks/fixtures/py-notes-api`; extend the supplied contract to two authenticated tenants and one privileged support identity.
- Task: Add a tenant-owned read/write boundary without trusting a body workspace ID.
- D1: Wrong-tenant GET and POST reject without returning or mutating another tenant row.
- D2: Permitted access succeeds; app role differs explicitly from a test/admin bypass.
- R1: Can scope leak through jobs, caches or a pooled connection?

### BE8 ambiguous charge outcome

- Setup: TypeScript sandbox payment fake commits then times out; client retries one key with identical and changed parameters.
- Task: Reconcile the unknown result safely.
- D1: Identical retry returns the committed result without another charge.
- D2: Changed parameters for the same key reject explicitly; timeout is not recorded as not applied.
- R1: Does crash recovery protect external effects without claiming generic exactly-once?

### BE9 migration recovery

- Setup: Python service has existing rows plus new writes after an additive schema switch; database is unavailable here.
- Task: Write the migration/recovery slice with honest evidence.
- D1: Static/dry-run results are separate from unapplied DB behavior.
- D2: Recovery preserves new writes via approved forward-fix/restore when a down migration would lose data.
- R1: Can a maintainer identify the exact execution gap?

### BE10 business-event distinction

- Setup: Refund and paid events refer to one provider object; two paid event IDs describe one fulfillment; events share creation seconds.
- Task: Choose deduplication identities and allowed transitions.
- D1: Both paid deliveries yield one effect; refund remains actionable.
- D2: Equal created timestamps do not discard distinct valid events.
- R1: Is the deduplication key derived from the concrete provider and business contract?

### BE11 negative trigger

- Setup: User asks to increase only the CSS spacing of a button; no API/auth/data change.
- Task: Route the task.
- D1: No backend migration, worker, endpoint or identity review is launched.
- D2: Visual scope is preserved.
- R1: Is ownership narrow?
