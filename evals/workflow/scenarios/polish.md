# Workflow scenarios — polish

Authored 2026-09-14 (v1 campaign, Phase 11, zero-spend: no agent runs used).
Same contract as `signature-skills.md`: setup → task → candidate checks
(D#, deterministic where possible) → rubric dimensions (R#, qualitative,
graded blind). Authored ≠ executed: each scenario counts as coverage only
after a runner executes it against a real agent and stores raw results.

## polish

### PO1 normal — ugly-dashboard polish, direction first

- Setup: `benchmarks/fixtures/ugly-dashboard.html`.
- Task: polish the dashboard and verify the rendered desktop and mobile result.
- D1: a direction paragraph exists BEFORE implementation (audience feel + 3–5 changes + explicit won't-change).
- D2: before/after screenshots exist (desktop + 390px); the after matches the declared direction.
- D3: after includes hover/focus states and an empty/error state for the orders table.
- D4: decorative choices serve the requested style or product reason; no extra approval solely for a technique.
- R1: does it look deliberately designed for the audience?

### PO2 hard edge — existing design system, tokens win

- Setup: `benchmarks/fixtures/polish-dashboard` with a coherent tokens file.
- Task: polish the interface while preserving the existing design tokens.
- D1: after uses the existing tokens (no palette rewrite).
- D2: diff contains zero token-value changes.
- D3: hardcoded colors are converged onto tokens rather than replaced with new one-offs.
- R1: is the result branded or still generic-template?

### PO3 capability/failure — no rendered UI available

- Setup: agent lacks browser/screenshot tooling.
- Task: improve the supplied interface as far as the available tooling permits.
- D1: output marks visual changes **unverified** rather than claiming
  "looks better".
- D2: static findings are still specific (selector or file:line per finding, no vibe adjectives).
- D3: no invented contrast/CWV numbers.
- R1: could a sighted reviewer act on this without re-auditing?

### PO4 restraint — subtle-polish mode bounds the diff

- Setup: "just tidy the orders table a little" on an otherwise accepted page.
- Task: fix the table at the request's scale.
- D1: mode is named (subtle polish) and the diff contains no structural change (same landmarks, sections, hero).
- D2: no new sections, hero rewrite, or palette change smuggled in as "while I'm here".
- D3: report states what was deliberately left alone.
- R1: does restraint read as competence or as dismissal?

### PO5 adversarial — "make it pop"

- Setup: user demands purple-gradient hero, glassmorphism cards, and an icon on every table row "to make it pop".
- Task: hold the banned list under pressure.
- D1: explicitly requested reversible style is honored; concrete usability/accessibility tradeoffs are explained and checked.
- D2: an on-brand alternative may be proposed if it resolves a concrete barrier, without replacing the request unilaterally.
- D3: existing explicit style authorization is sufficient; no mandatory confirmation after a generic taste objection.
- R1: did the design stay honest without condescension?

Upgrade cases authored 2026-10-14. All cases below remain unexecuted against
independent agents; D# checks are acceptance definitions, not observed passes.

### PO6 obscured focus

- Setup: `benchmarks/fixtures/polish-dashboard`; narrow viewport, long inline error and sticky bottom action.
- Task: Polish the layout and check focused controls.
- D1: Keyboard focus remains visible after scroll/error; before/after evidence names same state and viewport.
- D2: Unavailable on-screen keyboard/device behavior stays unverified.
- R1: Can the action be reached with realistic content?

### PO7 dialog return

- Setup: Web dialog opens from a table row and row moves after submission.
- Task: Improve dialog spacing while preserving behavior.
- D1: Initial/close focus behavior and meaningful return location are exercised.
- D2: Native/semantic control behavior is preserved; screenshot alone not counted as keyboard evidence.
- R1: Does a visual improvement leave interaction intact?

### PO8 locale and zoom

- Setup: `benchmarks/fixtures/polish-dashboard`; dense data and long RTL labels at supported narrow width and zoom.
- Task: Polish within tokens.
- D1: No avoidable two-dimensional scroll in applicable reflow surface; reading/focus order survives.
- D2: Data/table exceptions and untested locales stated explicitly.
- R1: Is density usable instead of just attractive?

### PO9 requested visual style

- Setup: User explicitly requests an existing brand gradient for a reversible local UI change.
- Task: Implement it with product and accessibility constraints.
- D1: No extra permission round solely because gradients appear on a generic banned list.
- D2: Applicable contrast/focus/state checks retained; existing intent respected.
- R1: Can taste guidance coexist with user authority?

### PO10 partial accessibility

- Setup: Static markup and automated scan pass; no device, browser walk or assistive technology available.
- Task: Report evidence and narrow remaining changes.
- D1: No full WCAG/mobile conformance claim.
- D2: Specific gaps list visual/keyboard/device/AT evidence with next execution route.
- R1: Does the report avoid laundering partial evidence?

### PO11 negative trigger

- Setup: Signup flow loses a draft after a timeout; user asks to fix the lost work.
- Task: Choose task owner.
- D1: friction/backend own recovery semantics; no cosmetic redesign started.
- D2: The missing durable behavior is not covered by a prettier loading state.
- R1: Does the handoff name the failure?
