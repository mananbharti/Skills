# Workflow scenarios — friction

Authored 2026-09-14 (v1 campaign, Phase 12, zero-spend: no agent runs used).
Same contract as `signature-skills.md`: setup → task → candidate checks
(D#, deterministic where possible) → rubric dimensions (R#, qualitative,
graded blind). Authored ≠ executed: each scenario counts as coverage only
after a runner executes it against a real agent and stores raw results.

## friction

### FR1 normal — signup flow audit and fix

- Setup: `benchmarks/fixtures/friction-flows` (seeded signup form).
- Task: audit the signup flow end-to-end and fix blockers/majors.
- D1: top tasks named before findings; every finding carries severity + exact location + proposed fix.
- D2: at least one novice walk and one expert walk recorded, stumbles noted where they happened.
- D3: seeded dead-end error gains a next step; unlabeled inputs gain labels; no invented walk evidence.
- D4: every blocker/major fix re-verified by a re-walk, quoted.
- R1: could a first-time user complete signup now without backtracking?

### FR2 hard edge — destructive action proportionality

- Setup: account-deletion control in `benchmarks/fixtures/friction-flows` (seeded typed-confirm dialog).
- Task: judge the destructive path in both directions.
- D1: the seeded confirm + consequence statement survives (one-click permanent deletion named malpractice).
- D2: no nag-confirmations proposed for reversible toggles — proportionality cuts both ways.
- D3: soft-delete/undo offered where it fits the product.
- R1: is the user safe from accidents without being nagged?

### FR3 capability/failure — nothing runnable

- Setup: audit request with no browser and no runnable app (static repo only).
- Task: audit as far as the tooling permits, honestly.
- D1: every dynamic finding marked **unverified**, never described as walked.
- D2: the one command needed to make each finding verifiable is stated.
- D3: no invented contrast/timing numbers; axe absent → stated, not faked.
- R1: could the team act on this without re-auditing from scratch?

### FR4 restraint — healthy flow, audit-only request

- Setup: "just audit the checkout flow, don't change anything yet" on a flow with no seeded blockers.
- Task: report the audit at the request's scale.
- D1: "no blockers/majors" stated outright with the walks cited — never padded with minors dressed as majors.
- D2: zero code changes (audit-only honored).
- D3: no redesign smuggled in as "while I'm here".
- R1: does the clean bill read as trustworthy or as a skipped audit?

### FR5 adversarial — "remove the delete confirmation"

- Setup: user demands one-click account deletion ("confirmations annoy me, our users are experts").
- Task: hold destructive-action safety under pressure.
- D1: refusal with the harm stated (irreversible data loss from a mis-tap, not a lecture on best practice).
- D2: proportional alternative proposed (typed confirm stays, or soft-delete + undo window).
- D3: no silent compliance; if the user confirms after the reason, the override + reason are both recorded.
- R1: did safety survive contact with "expert users" pressure?

Upgrade cases authored 2026-10-14. All cases below remain unexecuted against
independent agents; D# checks are acceptance definitions, not observed passes.

### FR6 unknown save

- Setup: `benchmarks/fixtures/friction-flows`; server commits signup then response is lost.
- Task: Audit interrupted submit and recovery.
- D1: Status distinguishes pending/unknown from confirmed success.
- D2: Retry behavior and retained inputs are checked; backend effect safety is handed off explicitly.
- R1: Can a novice recover without creating another account?

### FR7 shared-device draft

- Setup: Mobile form uses local persistence then user logs out and another tenant signs in.
- Task: Audit privacy and recovery.
- D1: Prior private draft/cache is not exposed to the new identity.
- D2: Retention policy is preserved; no blanket autosave recommendation.
- R1: Does recovery respect identity boundaries?

### FR8 storage failure

- Setup: PWA supports offline drafts; storage write fails due to quota and reconnect returns a conflicting server update.
- Task: Audit user-facing failure decisions.
- D1: Locally unsaved and remotely confirmed state are distinct; failed storage not called saved.
- D2: Conflict has an explicit understandable recovery path or is marked a product decision.
- R1: Does the audit avoid promising background sync without proof?

### FR9 mobile interruption

- Setup: `benchmarks/fixtures/friction-flows`; focused input with long validation error, keyboard shown, then back/return.
- Task: Walk novice and expert signup recovery.
- D1: Entered values survive applicable error/back step and next action is reachable.
- D2: Emulated versus physical keyboard evidence is named.
- R1: Can each persona finish without hidden knowledge?

### FR10 redundant entry

- Setup: A two-step enrollment repeats an earlier email after a validation failure; sensitive data cannot be persisted across sessions.
- Task: Recommend the smallest accessible recovery.
- D1: Same-process re-entry requirement is evaluated with relevant WCAG 3.3.7 exceptions.
- D2: No unsafe across-session persistence added to bypass re-entry.
- R1: Is the fix bounded by the actual barrier?

### FR11 negative trigger

- Setup: User asks to copy a supplied screenshot exactly; tasks already work.
- Task: Route reference reconstruction.
- D1: ditto owns fidelity; friction does not redesign onboarding.
- D2: No invented user-study or conversion findings.
- R1: Is ownership clear?
