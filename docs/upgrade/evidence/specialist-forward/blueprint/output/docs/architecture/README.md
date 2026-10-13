Question: what order request path is actually implemented in the ts-dashboard fixture? Audience: maintainer; time boundary: copied source at input hashes. Mermaid source: output/docs/architecture/request-flow.mmd. This maps implementation, not deployment. No proposed services or infrastructure included.

| Item/edge | Evidence | State/confidence |
| --- | --- | --- |
| Browser GET, header, local stats/filter/rows | App.tsx:28–51,122, OrderList.tsx:5–16 | Observed source/high; runtime unverified |
| GET handler reads module array and returns JSON | api/orders.ts:14–18 | Observed source/high |
| Router mounted at requested URL; auth/body middleware/server entrypoint | No such file supplied; express import absent from package dependencies | Unknown; do not infer backend is running |
| submitNewOrder sends POST and optimistic append | App.tsx:54–72 | Observed function definition/high; no UI caller supplied |
| POST validation and array append | api/orders.ts:20–31 | Observed source/high; invalid branch returns false without sending response |
| Durable database, cloud topology, TLS, production auth | No supplied evidence | Unknown; omitted |

Load-bearing spot checks: axios GET and router.get path match in source; router pushes payload into the same module-local array used by GET. These checks cannot establish actual runtime wiring. Boundary: browser payload enters the router; server type assertion is not runtime validation. Client example bearer header does not prove server authentication. Failure risks: invalid POST gets no explicit response; client POST is unawaited, so asynchronous rejection is outside synchronous catch; GET failure has no visible message. No change or ADR approved.

Bundled Mermaid heuristic passed (actual exit0); no Mermaid parser/browser render or visual legibility proof. mmdc probe is logged. Source diagram labels unknown wiring rather than claiming a full working request. The task asks Mermaid/checks only; full HTML shell not produced.
