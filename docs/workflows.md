# Workflow recipes

Skills compose through small, explicit handoffs. These recipes are examples,
not rituals: skip any step whose output already exists or whose question is not
blocking the work.

## Build from an idea

```text
hotseat
→ distill
→ scout, only where an external choice needs current evidence
→ masterplan
→ pilot
→ proof
→ roadtest, where a UI exists
→ referee
→ cleared
→ runway
→ recall, for decisions worth keeping
```

The idea is challenged before it becomes scope. The brief fixes what “done”
means; research resolves unstable external facts; the plan becomes verified
slices. Testing, browser evidence, and independent review precede the release
gate. Deployment is a separate act, and only durable decisions enter memory.

## Rescue vibe-coded spaghetti

```text
spelunk → unslop → proof → referee
```

First map what is load-bearing. Then establish a behavior baseline and remove
accidental complexity in small batches. Tests protect the result; review catches
cleanup that quietly changed intent. Use `polish` separately if the mess is
visual rather than structural.

## Fix a hard bug

```text
sleuth → proof → roadtest, if the trigger is browser-dependent
```

Diagnosis produces a failing signal and a causal chain. `proof` turns that
signal into permanent regression protection. `roadtest` is earned only when the
browser is part of the mechanism or the user-visible verification.

## Build a polished frontend

```text
polish → friction → roadtest
```

If users cannot finish the task, start with `friction` before visual work.
Otherwise `polish` can act directly. The browser pass proves applicable paths,
console observations, network expectations and viewports.

If the task is “match this screenshot,” replace `polish` with `ditto`.

## Prepare an open-source launch

```text
janitor → frontpage → findable → cleared
```

Repository truth and hygiene come before the landing page. `frontpage` turns
that truth into documentation; `findable` handles machine-readable discovery
where a public site exists; `cleared` checks the applicable release dimensions.

## Review architecture

```text
spelunk → blueprint → headroom
```

`spelunk` maps what exists. `blueprint` makes the current boundaries and flows
legible. `headroom` evaluates what should change at measured thresholds. Do not
draw the future as if it already exists.

## Change a backend contract safely

```text
scout, if the framework/API behavior is version-sensitive
→ backend
→ proof
→ harden, for auth/data/trust-boundary changes
→ referee
```

Current external facts are pinned before code. Backend invariants guide the
implementation, tests sit at the contract boundary, security reviews the
changed attack surface, and review checks consumers and migration safety.

## When one skill is enough

- A precise library question: `scout`.
- A readable map of an unfamiliar repo: `spelunk`.
- A commit message from an already-staged diff: `janitor`.
- A performance investigation with no planned refactor: `hotpath`.
- A final readiness decision without deployment: `cleared`.
- A session handoff with durable decisions: `recall`.

The smallest sufficient workflow is a design rule. More specialists do not
automatically mean a better result.

## Autonomous execution

```text
handsfree + pilot
handsfree + sleuth
handsfree + unslop
```

When you already know what needs to be built, fixed, or cleaned up, and you do not want the agent to stop for permission to run tests, inspect files, or make routine engineering decisions. The workflow runs continuously until it hits a human-level product decision, a destructive risk, or completion.

## Compact novice and expert contracts

Each recipe below can be used independently. The fixture is a safe rehearsal
input, not evidence that the full workflow has run. Never load all owners at
once; skip a stage when its output is already valid. Carry the
[handoff identity and authorization](handoff.md) when changing owners.

### A. Vague idea to one working slice

Say: “Help me build a small notes app; get one useful flow working.”
Use `hotseat` only for uncertain product choices, `distill` for acceptance,
`masterplan` when sequencing matters, then `pilot` and the applicable checks.
Expert contract: `user goal → acceptance → scoped slice → check output`.
Expected artifact: a brief plus runnable code and verification for one user path.
Stop when a material product choice lacks an answer; continue approved local work.
Common failure: turning every feature into the whole lifecycle.
Rehearsal: [Python notes API](../benchmarks/fixtures/py-notes-api/README.md).

### B. Rescue an accumulated mess

Say: “Simplify this shop, but its legacy export must stay identical.”
Use `spelunk` if boundaries are unknown, `sleuth` for a real defect or `unslop`
for accidental complexity; keep `proof` and review at changed boundaries.
Expert contract: `behavior baseline + protected invariants → small diff → same checks`.
Expected artifact: keep-list, cleanup diff, compatible outputs, before/after checks.
Stop if there is no characterization evidence for behavior about to change.
Common failure: calling a functional rewrite cleanup.
Rehearsal: [shop source](../benchmarks/fixtures/unslop-shop/shop.py).

### C. Mystery bug or incident

Say: “This value stays stale after a write; fix the cause and prove it.”
Use `sleuth`; hand off to `backend` or `hotpath` only after causal evidence
points there. Add the regression with `proof`; release gates apply to the target.
Expert contract: `trigger → separating experiment → causal fix → failing/green regression`.
Expected artifact: reproduction, cause, scoped patch and check output.
Stop unsafe production experiments; retain an explicitly provisional workaround.
Common failure: speculative rewrites or a disappearing symptom without explanation.
Rehearsal: [cache source](../benchmarks/fixtures/sleuth-cache/cache.py).

### D. Useful and distinctive interface

Say: “Make this dashboard easier to use on mobile without replacing its tokens.”
Start with `friction` for task barriers, `polish` for presentation; use `ditto`
only when matching an authorized reference is the requirement. `roadtest`
supplies browser evidence when available.
Expert contract: `task/state/viewport → change → comparable capture + interaction checks`.
Expected artifact: preserved tokens, state coverage, screenshots and actual observations.
Stop a claimed visual verdict when fonts, viewport or browser evidence are missing.
Common failure: claiming pixel equivalence from source inspection alone.
Rehearsal: [dashboard](../benchmarks/fixtures/polish-dashboard/index.html).

### E. Payment, auth or multi-tenant boundary

Say: “Handle paid events safely when they repeat or arrive late.”
Use `backend` for behavior, `harden` for trust-boundary review, `proof` for
negative principals/replays and `cleared` for release evidence if shipping.
Expert contract: `trusted principal + legal state transitions → atomic write → denial/replay checks`.
Expected artifact: authenticated event contract, tenant ownership and durable deduplication evidence.
Stop live financial actions without authorization; synthetic fixture events stay local.
Common failure: confusing event-ID deduplication with one business side effect.
Rehearsal: [synthetic event worker](../skills/backend/assets/payment-demo.py).

### F. Slow now or capacity later

Say: “Measure today's bottleneck, then decide our next scale trigger.”
Use `hotpath` for current measurements and `headroom` only when workload
projection changes the decision. Preserve the same correctness gate.
Expert contract: `arrival rate + work per request + measured capacity → bottleneck → trigger`.
Expected artifact: comparable measurements, assumptions, queue/recovery model and keep/revert decision.
Stop if the generator or downstream limit invalidates the load result.
Common failure: treating a closed workload or registered-user count as peak demand.
Rehearsal: [explicit assumed workload](../skills/headroom/assets/capacity-case.json).

### G. Open-source release

Say: “Make this project's install instructions trustworthy.”
Use `janitor` for repository state, `frontpage` for factual docs, `findable`
only for an actual public site's discoverability and `cleared` for applicable gates.
Expert contract: `clean task workspace + tested commands → documented artifact → scoped release verdict`.
Expected artifact: tested quickstart, evidence-linked claims and protected user Git changes.
Stop external publication until its actual authorization; a local docs edit may proceed.
Common failure: invented users, badges or forcing app deployment on a library.
Rehearsal: [small notes tool](../benchmarks/fixtures/frontpage-tool/README.md).

### H. Multi-session authorized execution

Say: “Continue our approved slice using the last session's decisions.”
Use `recall` to refresh durable facts and `handsfree` for routine local execution;
the actual task owner performs the work. Old memory does not expand approval.
Expert contract: `current repo + refreshed decision + approved scope → owned work → checkpoint`.
Expected artifact: current facts, superseded notes, scoped result and next useful action.
Stop repeated denials for the same action; complete safe independent work.
Common failure: stale notes outranking current code or a perpetual agent loop.
Rehearsal: [memory fixture](../benchmarks/fixtures/recall-notes/PROJECT_CONTEXT.md).
