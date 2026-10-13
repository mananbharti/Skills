Rung3: static only. Browser/HTTP could not run: loopback server PermissionError, then file URL policy denial. No retry/bypass after denial. UI journeys, console/network runtime and responsive screenshots are unverified. Owned source unchanged.

Charter: anonymous fake buyer on local fixture; happy checkout must submit charge/order and only then show confirmed order. Denial must show actionable failure and no successful charge/order. Fresh browser sessions would isolate each, but none was created successfully.

| Path | Result | Actual evidence |
| --- | --- | --- |
| Checkout happy | Source contradiction; browser outcome unverified | app.js:2–6 click callback logs error then alerts Order placed, with no charge submission or order persistence code. |
| Checkout denied payment/session | Not implemented in source; browser unverified | Same callback has no response/authorization branch; no payment or session provider supplied. |
| Initial session failure | Static concern, not captured console event | app.js:9 constructs rejected Promise with no handler. |
| Login | Unverified | index.html form POST/login; no backend supplied. |
| Order history | Unverified endpoint | index.html links/missing-page; file absent but no HTTP404 observed. |

Source semantic locator candidates are button role + Check out, and label Email/Password; no locator healing executed. Do not call an alert a transaction success. Next owner: implementation maintainer connects checkout contract and handles denial; browser QA reruns when authorized HTTP fixture is available, captures assertion screenshots, console/network and persistent result at declared viewports. No app fixes were requested here.
