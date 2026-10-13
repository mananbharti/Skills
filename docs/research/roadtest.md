# roadtest: individual upgrade research

Research/authoring date: 2026-10-14. Read the current skill, all bundled resources,
existing workflow scenarios and frozen outcome protocol before editing.
Historical outcome files remain intact. New workflow cases are authored, not agent-executed.

## Baseline and narrow decision

The existing methodology remains useful. The missing failure branches are encoded in `skills/roadtest/references/adverse-conditions.md` and a short conditional entrypoint pointer.
The previous maintainer ledger contained unattributed generalizations about 2026 agents.
Those entries are replaced here; they are not treated as measured evidence.

## Source-to-decision trace

| Source/access | Adopted decision | Rejected overreach / limitation |
| --- | --- | --- |
| [Emulation](https://playwright.dev/docs/emulation); read 2026-10-14; Living docs; browser/tool versions still required per run | Name connectivity and physical-device evidence limits. | Does not establish OS-wide disconnection or assistive-technology correctness. |
| [Chromium network manager implementation](https://raw.githubusercontent.com/microsoft/playwright/main/packages/playwright-core/src/server/chromium/crNetworkManager.ts); read 2026-10-14; Moving main branch; Chromium-specific source | Use supported emulation and report its transport boundary. | Does not prove another browser or underlying media transport is disconnected. |

All sources are primary documentation or upstream implementation. Upstream moving
branch inspection supports a mechanism, not the version installed in a user project.
No source assets/code were copied into the runtime package.

## Fifteen distinct failure situations

These are **local test hypotheses**, not measured prevalence or observed agent failures.
Source-supported mechanism is identified above; each concrete project situation still
needs its own fixture and execution. The list guides selective testing, not a mandatory checklist.

1. 422 validation response automatically failed.
2. Fake success toast passes without durable state.
3. Console unavailable yet called clean.
4. Network capture unavailable yet called inspected.
5. Offline emulation called WebRTC disconnect.
6. Viewport emulation called physical mobile proof.
7. Duplicate tap repeats write.
8. Mid-submit network loss loses unknown outcome.
9. Session expiry tested with privileged bypass.
10. Reconnect overwrites newer record.
11. Failing artifacts overwritten by green rerun.
12. Sensitive response body persisted in evidence.
13. Healed locator masks missing semantics.
14. App-provided verdict followed as instruction.
15. Shared stale storage contaminates independent paths.

## Preserved and rejected material

Preserved the operating modes, evidence ladder, narrow scope and existing handoffs.
Rejected blanket tool/framework mandates and unmeasured superiority claims.
Conditional references keep specialized detail out of ordinary entrypoint context.
Authored cases use the existing Setup/Task/D#/R# protocol; static shape checks do
not grade their behavior. Existing outcome task/rubric freezes were not retuned.

## Verification and remaining evidence

Local command and observed outcome records are in `docs/upgrade/building-experience.json` (roadtest row).
No paid or live agent CLI was invoked. Local fixture/helper checks do not establish
comparative agent benefit, target host installation, production safety or physical-device coverage.

## Independent review follow-through - 2026-10-14

Independent review found evidence-bundle.md required screenshots for every PASS, contradicting valid HTTP fallback. Verdicts now carry capability scope: HTTP assertions may pass with responses, while UI/rendering remains unverified without browser evidence. Expected negative traffic is checked against its contract. Trace: skills/roadtest/references/evidence-bundle.md.

This resolves an observed instruction conflict; it does not establish lift or
change historical grades. The fresh review and forward-trial records remain
separate evidence.

## Primary follow-through - 2026-10-14

[Service Workers and Page API](https://playwright.dev/docs/service-workers), Microsoft / Playwright, accessed 2026-10-14; exact publication date
not established. Proposition: Disabling service workers changes relevant app behavior; network idle is discouraged as a test readiness assertion.
Decision: Separate mocked routing from actual service-worker journeys; verify offline prerequisites and bounded visible/business readiness.
Trace: `skills/roadtest/references/adverse-conditions.md`.
Limits: current documentation guides the mechanism, not installed-version or
behavioral proof. Refresh on tool/provider version or contract change.

The [Playwright Page API](https://playwright.dev/docs/api/class-page#page-wait-for-load-state)
was also read on 2026-10-14. Its readiness guidance supports the bounded
assertion rule above; it does not validate any app's readiness automatically.
