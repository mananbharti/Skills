Mode: hypothetical supply-chain triage, report only. Scope is the supplied scanner claim; no packages, lockfile, advisory IDs, versions or deployed configuration were supplied. Assets include application data/availability and build credentials; relevant boundaries are untrusted runtime inputs and dependency installation/build execution.

| Signal | Evidence class | Decision | Next evidence/owner |
| --- | --- | --- | --- |
| Every outdated dependency labeled Critical | Reported hypothetical scanner output | Outdated is not proof of vulnerability or system severity. Preserve labels as raw signal; do not inherit them as findings. | Maintainer obtains package+resolved version+advisory+affected range and scanner method. |
| No reachable path | Supplied hypothetical condition, not independently established | If substantiated, lower runtime exposure priority; do not label fixed or universally safe. | Trace shipped artifact/imports/config to affected sink, including dynamic paths and build/CI use. |
| Residual supply-chain/build risk | Unknown | Runtime unreachability does not prove absence of install/build exposure or future reconfiguration risk. | Check installation/build hooks, transitive use, credentials and artifact contents without running untrusted code. |

For each real candidate capture attack precondition, entry -> affected code -> asset impact, reachability evidence, plausible severity and separate confidence. No evidence-backed vulnerability severity can be assigned to this unnamed report. A confirmed reachable issue with material impact takes priority over an unsupported Critical badge.

Keep unreachable candidates in a maintenance queue with owner, exposure condition and re-review trigger (artifact/config/dependency change); risk has not been accepted by a human. Upgrade in an isolated branch only once compatibility and affected behavior can be retested, or remove a dependency only after use is disproved. No upgrades, scanning, network requests, exploitation or closure claims executed. This is not a security guarantee.
