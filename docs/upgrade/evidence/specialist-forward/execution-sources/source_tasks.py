from record import *
import difflib, re
# Explicit source-read transcripts with line numbers; active skill hashes already recorded.
for slug in ['blueprint','friction','ditto','roadtest','referee','frontpage','findable']:
 files=sorted(p for p in (BASE/slug/'original').rglob('*') if p.is_file())
 # Do not copy secret-looking fixture literals into read logs for ditto: raw input is already preserved.
 for p in files:
  if p.suffix in ['.html','.js','.ts','.tsx','.py','.md','.json','.txt','.xml']:
   src=p.read_text()
   if slug=='ditto':src=re.sub(r'const ANALYTICS_KEY = "[^"]+";', 'const ANALYTICS_KEY = "[REDACTED FIXTURE LITERAL]";',src)
   dest=EVID/slug/('read-'+str(p.relative_to(BASE/slug/'original')).replace('/','_')+'.txt')
   dest.write_text('\n'.join(f'{n}: {line}' for n,line in enumerate(src.splitlines(),1))+'\n')
# Blueprint: implemented code edges versus wiring unknowns.
w=BASE/'blueprint'/'work';d=w/'docs/architecture';d.mkdir(parents=True,exist_ok=True)
(d/'request-flow.mmd').write_text('''sequenceDiagram
    participant UI as App.tsx browser component
    participant Wiring as Runtime route wiring unknown
    participant API as api/orders.ts router
    participant Store as Module-local orders array
    participant Row as OrderRow
    UI->>Wiring: Implemented GET /api/orders with example bearer header
    Note over Wiring,API: Router mounting, Express install, body parsing and auth enforcement not supplied
    Wiring-->>API: Mapping unknown, not runtime-verified
    API->>Store: Implemented read
    Store-->>API: Current in-process orders
    API-->>UI: Implemented JSON handler; actual response path unknown
    UI->>UI: Implemented setOrders and stats aggregation
    UI->>Row: Implemented filtered order props
    Note over UI: Fetch rejection clears loading; no visible error
    Note over UI: submitNewOrder defined but no form or call site in rendered JSX
    UI->>Wiring: Defined POST call, not awaited
    UI->>UI: Defined optimistic local append before response
    Wiring-->>API: POST mapping unknown
    alt customer empty or total negative
        API->>API: Implemented return false, no error response sent
    else accepted by basic checks
        API->>Store: Implemented push payload
        API-->>UI: Implemented JSON ok response
    end
''')
run('blueprint',[str(BASE/'blueprint/skill/scripts/validate-mermaid'),str(d/'request-flow.mmd')],name='mermaid-static-check.txt')
run('blueprint',['rg','-n','axios|setOrders|submitNewOrder|OrderRow|router\.|orders\.push|res\.json|return false','src'],name='edge-spot-checks.txt')
run('blueprint',['python3','-c','import shutil; print({"mmdc":shutil.which("mmdc"),"browser":"local route blocked, no render attempted"})'],name='render-capability.txt')
report('blueprint','''Question: what order request path is actually implemented in the ts-dashboard fixture? Audience: maintainer; time boundary: copied source at input hashes. Mermaid source: output/docs/architecture/request-flow.mmd. This maps implementation, not deployment. No proposed services or infrastructure included.

| Item/edge | Evidence | State/confidence |
| --- | --- | --- |
| Browser GET, header, local stats/filter/rows | App.tsx:30–59, OrderList.tsx:5–16 | Observed source/high; runtime unverified |
| GET handler reads module array and returns JSON | api/orders.ts:14–17 | Observed source/high |
| Router mounted at requested URL; auth/body middleware/server entrypoint | No such file supplied; express import absent from package dependencies | Unknown; do not infer backend is running |
| submitNewOrder sends POST and optimistic append | App.tsx:59–81 | Observed function definition/high; no UI caller supplied |
| POST validation and array append | api/orders.ts:19–31 | Observed source/high; invalid branch returns false without sending response |
| Durable database, cloud topology, TLS, production auth | No supplied evidence | Unknown; omitted |

Load-bearing spot checks: axios GET and router.get path match in source; router pushes payload into the same module-local array used by GET. These checks cannot establish actual runtime wiring. Boundary: browser payload enters the router; server type assertion is not runtime validation. Client example bearer header does not prove server authentication. Failure risks: invalid POST gets no explicit response; client POST is unawaited, so asynchronous rejection is outside synchronous catch; GET failure has no visible message. No change or ADR approved.

Bundled Mermaid heuristic passed (actual exit0); no Mermaid parser/browser render or visual legibility proof. mmdc probe is logged. Source diagram labels unknown wiring rather than claiming a full working request. The task asks Mermaid/checks only; full HTML shell not produced.''','source-diagram',['Route mount/server/body parser/auth/durability and runtime flow unknown; visual render unavailable.'])
(d/'README.md').write_text((EVID/'blueprint/artifact.md').read_text())
# Refresh final artifact hashes after README is written.
shutil.copytree(d,EVID/'blueprint/output/docs/architecture',dirs_exist_ok=True)
(EVID/'blueprint/output-hashes.json').write_text(json.dumps(hashes(EVID/'blueprint/output'),indent=2)+'\n')
# Friction source audit only: requested checkout/save are missing from actual fixture.
run('friction',['rg','-n','form|input|error|button|DELETE|addEventListener','index.html'],name='static-flow-inventory.txt')
report('friction','''Rung: static repository evidence only; audit, no edits or user walk. Actual fixture is signup + typed account deletion, not checkout or save. Provisional user jobs: create account from anonymous form; understand/recover generic error; confirm account deletion. Success for signup would be an account result, but endpoint handling is absent; success for delete would require an explicit server result, but no click handler/backend supplied. Checkout, payment and save/autosave do not exist in these files; their experience cannot be audited from this fixture.

| Concern/severity | Location | Source observation / impact hypothesis | Smallest intervention / verification |
| --- | --- | --- | --- |
| Accessibility/major | index.html:23–24,32 | Inputs have placeholders but no persistent label or association. Context disappears when typing; accessible names need browser/AT confirmation. | Add visible label-for pairs; walk keyboard/AT at same form. |
| Usability/major | index.html:25 | Always-present “Something went wrong” gives no reason or recovery action and is not field-associated. | Show an error only on actual failure, keep input, identify recovery and field; submit bad/corrected input with fake server fixture. |
| Usability/major | index.html:26 | “Submit” hides create-account outcome. | Label Create account; check novice understands completion in observed user walk. |
| Usability/major | index.html:20–27 | No supplied loading/success/data-preservation/error-handler evidence. | Backend/UX owner supplies fixture or response contract; then test failure/retry/back without losing entered work. This is an unknown, not confirmed data loss. |
| Destructive recovery/major unknown | index.html:30–39 | Consequence copy and exact DELETE enablement exist; no deletion action/result/recovery provided. | Preserve typed confirmation; verify real server authorization, exact consequence and state after fake deletion in isolated environment. Do not remove guard from static review. |

Novice/expert inspection is a source-based task hypothesis, not a real walk. Browser needed for tab/focus order, accessible names, validation messages, error/status announcement, disabled-button enablement, narrow-width reflow and target sizes. User evidence needed for comprehension/hesitation/backtracking and success feedback; no conversion, frequency, timing or completion rate measured. Assistive technology/accessibility conformance not certified. No live account or destructive action exercised. One safe future start command would serve this isolated fixture only after loopback-server permission exists; endpoint fixture still required.''','static-audit',['Checkout/save absent; browser/user/AT and server response evidence unavailable.'])
# Roadtest degraded rung; do not retry blocked server/browser.
(EVID/'roadtest/browser-policy.txt').write_text('cua.getState: in-app browser present. python3 -m http.server8769 --bind127.0.0.1 --directory owned work failed PermissionError [Errno1] Operation not permitted; raw trace http-server.log. cua.createBrowserTab(iab,file:///private/tmp/skills-forward/specialists/roadtest/work/index.html) rejected: URL protocol not allowed (http/https only). Policy explicitly forbids bypass/workaround; no retry, alternate browser, data URL, raw CDP or other server was attempted.\n')
with (EVID/'roadtest/commands.jsonl').open('a') as f:f.write(json.dumps({'kind':'capability-attempt','argv':['python3','-m','http.server','8769','--bind','127.0.0.1','--directory',str(BASE/'roadtest/work')],'exit_code':1,'raw':'http-server.log','browser_call':'cua.createBrowserTab iab file URL','browser_result':'policy-denied; no bypass'})+'\n')
run('roadtest',['rg','-n','checkout|alert|console|Promise|login|history','index.html','app.js'],name='static-evidence.txt')
report('roadtest','''Rung3: static only. Browser/HTTP could not run: loopback server PermissionError, then file URL policy denial. No retry/bypass after denial. UI journeys, console/network runtime and responsive screenshots are unverified. Owned source unchanged.

Charter: anonymous fake buyer on local fixture; happy checkout must submit charge/order and only then show confirmed order. Denial must show actionable failure and no successful charge/order. Fresh browser sessions would isolate each, but none was created successfully.

| Path | Result | Actual evidence |
| --- | --- | --- |
| Checkout happy | Source contradiction; browser outcome unverified | app.js:2–6 click callback logs error then alerts Order placed, with no charge submission or order persistence code. |
| Checkout denied payment/session | Not implemented in source; browser unverified | Same callback has no response/authorization branch; no payment or session provider supplied. |
| Initial session failure | Static concern, not captured console event | app.js:10 constructs rejected Promise with no handler. |
| Login | Unverified | index.html form POST/login; no backend supplied. |
| Order history | Unverified endpoint | index.html links/missing-page; file absent but no HTTP404 observed. |

Source semantic locator candidates are button role + Check out, and label Email/Password; no locator healing executed. Do not call an alert a transaction success. Next owner: implementation maintainer connects checkout contract and handles denial; browser QA reruns when authorized HTTP fixture is available, captures assertion screenshots, console/network and persistent result at declared viewports. No app fixes were requested here.''','static-degraded',['Browser/HTTP blocked; all runtime journeys/console/network/responsive behavior unverified.'])
# Referee bounded independent static review; full historical diff unavailable.
run('referee',['rg','-n','total\(|user_cap|override|audit|tax\(','billing.py','brief.md'],name='intent-source-search.txt')
run('referee',['python3','-c','import billing; print({"default":billing.total([{"price":100,"qty":1}]),"cap_5_percent":billing.total([{"price":100,"qty":1}],0.05),"negative_cap":billing.total([{"price":100,"qty":1}],-0.10)})'],name='read-only-examples.txt')
report('referee','''Review type: independent bounded source review within specialist agent; no author commentary or patch. A historical diff/baseline and consumers are unavailable, so criterion3 “no other behavior changes” cannot be adjudicated fully. Coverage: billing.py entire file + brief.md; source search; three local pure examples. No production/runtime integration, history or tests supplied.

Verdict: request changes for missing admin override/audit behavior in the supplied implementation scope.

| Severity | Location | Finding / intent consequence | Fix direction |
| --- | --- | --- | --- |
| Major | billing.py:4–7; brief.md:4 | Criterion2 requires admin override with audit-log entry, but supplied total exposes only user_cap and fixed10% discount; file contains neither admin authorization nor audit emission. Source-only scope cannot exclude an external wrapper, which was not supplied. | Provide actual override enforcement and audit boundary or missing wrapper/caller evidence; protect permitted override + denied non-admin + emitted audit in tests. |
| Major | billing.py:6 | Negative user_cap makes d negative; local $100 example returns$110, a surcharge rather than a discount cap. Whether callers sanitize is unknown because none supplied. | Validate cap range at owning boundary (finite0..1) or document/enforce a prevalidated input contract, then test invalid caps and permitted cases. |

Intent1 is partially evidenced: default cap parameter15% and min enforce an upper bound on the currently fixed10% discount; supplied5% cap yields95. There is no requested-discount input, so adjustable discount policy beyond fixed10% remains unclear. Criterion2 missing in reviewed file; criterion3 unverified due to missing before-code/diff. tax refactor comment signals unrelated change but actual prior behavior is absent, so no invented tax regression finding. User-cap mutability alone does not prove privilege bypass; authorization boundary/callers need evidence. Scope verdict does not certify unreviewed application behavior.''','request-changes',['Historical diff/baseline, callers, external override wrapper and tests unavailable.'])
