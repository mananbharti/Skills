# Reproducible local failure gallery

These are deliberately seeded examples and exploratory in-session skill
executions, not customer incidents, testimonials, controlled agent comparisons
or a claim of superiority. Input/package hashes, requests, diffs and raw command
outputs are retained. The seed comments disclose faults to the executing agent;
there was no hidden-discovery benchmark. No public posts have been made.
The [28 demonstration cards](demo-cards.md) give direct requests and draft
hooks tied to these evidence boundaries.

Run the three executable corrections from a checkout with Python 3:

```bash
scripts/check-demos
```

The runner copies seed and corrected artifacts into disposable directories.
Expected seed assertion failures are part of the reproduction; incomplete or
setup-error runs cannot pass the recorded failure-count gate.

## Three verified narratives ready for human review

### A warm cache kept yesterday's value

Read → write replacement → read returned the old value while storage already
contained the new one. `sleuth` traced the cache-hit branch and changed only the
written key's invalidation. Two of three boundary tests failed on the seed;
all three pass on the corrected artifact, including other keys and falsey values.
The evidence covers this local cache, with no concurrency/distributed claim.

Draft hook: “The write succeeded. The next read was wrong. Here is the one
branch and the regression that explain it.”
[Code and evidence](upgrade/evidence/forward/sleuth/report.json).

### Private notes crossed the owner boundary

The synthetic notes app concatenated inputs into SQL and deleted by object ID
without enforcing owner. `harden` parameterized the owner/ID boundary, checked
deletion ownership, and moved its synthetic configuration value out of code.
Four of five tests failed on the seed; all five pass on the corrected artifact.
Authentication is assumed upstream; HTTP auth, real secrets and rotation were
not tested. The retained diff redacts the synthetic seed credential.

Draft hook: “One owner could delete another owner's note. The fix sits in the
query, and the denied-owner test now proves the boundary.”
[Code and evidence](upgrade/evidence/forward/harden/report.json).

### Two paid notifications fulfilled one order twice

Different event IDs described the same paid order, and a late pending event
reversed its local state. `backend` separated delivery identity, business
transition and tenant authority; it coupled receipt/state/effect in a local
transaction. Eight boundary tests fail on the seed and pass on the correction,
including failure/retry and caller-owned transaction recovery. The small demo
changes from pending/two fulfillments to paid/one.

Provider authentication is a stated precondition. This does not prove a real
payment integration, concurrent processes, external fulfillment or money safety.
The correction is a synthetic SQLite exercise, not production starter code.

Draft hook: “Two event IDs can mean one purchase. Deduplicating deliveries
alone is not enough; here is the transition and its replay test.”
[Code and evidence](upgrade/evidence/forward/backend/report.json).

## Other observed exercises

| Exercise | Actual result | Reproduce / limits |
| --- | --- | --- |
| Missing discount regression | Existing three tests passed; the added fourth correctly fails on double discount | [Proof artifact](upgrade/evidence/specialist-forward/proof/artifact.md); app correction was outside this task |
| Memory target changed | PostgreSQL target appended; old rationale preserved; SQLite-live constraint kept; structural checker passed | [Recall artifact](upgrade/evidence/intelligence-forward/recall/artifact.md); live database state is supplied, not observed |
| Theoretical quickstart replaced | README snippets exercised verbatim against a stdlib local tool; imaginary features/counts removed | [Frontpage artifact](upgrade/evidence/specialist-forward/frontpage/artifact.md); only local Python/runtime observed |
| CLI success contradicted served identity | Release judged blocked from supplied old/new fingerprints | [Runway artifact](upgrade/evidence/specialist-forward/runway/artifact.md); no URL, platform or deploy observed |
| Offline acknowledgment lost | Two seed assertions fail; two corrected model assertions pass | `scripts/test-archetypes`; JSON file models persistence, no mobile-device/storage-provider proof |
| Replayed or forged game input | Four seed assertions fail; four corrected model assertions pass | `scripts/test-archetypes`; deterministic authoritative state only, no socket or engine proof |

## Five requested project archetypes

| Archetype | Current evidence | Missing before a real end-to-end claim |
| --- | --- | --- |
| Tiny static site | Metadata/crawl-config source fixes and parser checks | Served headers/status, browser/social preview, crawler observation |
| TS full-stack SaaS + PostgreSQL | Dashboard source/plan/diagram; synthetic tenant/payment contract | Runnable frontend/backend fixture, real PostgreSQL role/RLS/concurrency, browser journey |
| Python API | AST-preserving authorized entrypoint slice and local security/data models | Installed framework/runtime API boundary, request/response tests and deployment |
| Mobile app | Persisted queue/retry model plus authored interruption/UX cases | Native app, real storage, background lifecycle, physical keyboard/network/device trials |
| Browser multiplayer game | Authoritative input/replay/reconnect model and fixed event checks | Real browser/engine/socket/session continuity and staging deployment |

The unfamiliar Requests checkout was read at pinned commit
`611c6162cbc4ac2020a2f91c7cfa4f3abf9bbb60`; no downloaded code ran.
[Navigation artifact](upgrade/evidence/intelligence-forward/spelunk/artifact.md)
and [source record](upgrade/evidence/unfamiliar-repo.json) preserve that boundary.

A dashboard source update preserves token bytes/actions and passes semantic and
computed-contrast checks. Browser access was denied, so there is no before/after
visual demonstration, screenshot, pixel equivalence or device conformance claim.
That flagship visual demo remains pending rather than being staged.
