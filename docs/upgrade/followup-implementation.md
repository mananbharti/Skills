# Follow-up implementation record (opencode, on top of `codex/deep-skills-v2`)

Branch: `feat/godlevel-no-lift-repair`. This file is additive: it does not
rewrite any historical verdict, tally, or evidence in `docs/benchmarks/`,
`docs/claims.md` (except the living C-009 footprint), or `docs/upgrade/`.
All work below is local and offline; no agent trial ran, so no comparative
lift is claimed anywhere.

## Commits

- `279f7c3` — NO LIFT repairs: `distill` marker floor + auth-bites rule,
  `masterplan` Slice vocabulary + path labels, `pilot` denial-safe config
  + `verified` report token; grader exempts declared outputs,
  fixture-quoted strings, negated denials.
- `27c2188` — MIXED repairs: `recall` `memory:` marker, `proof` literal
  `boundary`, `spelunk` denial-safe discovery, concierge C1
  `order_insensitive`, negation-aware contaminant gate, tech-name and
  shell-probe exemptions, workdir-strip hardening.
- `62ec070` — marker-contract audit (all 87 tasks vs all 28 SKILL.md):
  one gap found, `referee` override rule + template line.
- `dac9faf` — blueprint grader parity (shared quote helper, same
  exemptions, negation-aware infra check) + FrozenTaskPassability guard
  (87/87 tasks passable by contract-following output).
- `778e34a` — frontmatter word ownership: pilot/backend yield standalone
  `review` to `referee`, polish yields reference recreation to `ditto`;
  TriggerDiscipline guards; C-009 footprint updated.
- `cb05466` — verified primary-source encodes (each fetched and read
  before encoding): EARS (`distill`), WCAG 2.2 SC 2.5.8 + INP/LCP p75
  (`polish`, `hotpath`), SC 3.3.8/F109 (`friction`), bisect 0/1-127/125
  (`proof`, `sleuth`), Knight Capital/SEC 2013-222 (`sleuth`,
  `handsfree`, `cleared`), Playwright locators (`ditto`, `roadtest`);
  honesty fixes (`ditto` legal line, concierge handoff claim, `hotseat`
  horizon label, `referee` ladder); ResearchAnchors guards.

Three in-session research workstreams (build, experience-proof,
intelligence-ship families) supplied findings; two candidate findings
were voided on verification (`janitor` already uses `filter-repo`;
backend RLS already requires app-role writes).

## Verification executed on this branch

- `scripts/validate-skills`, `check-names`, `check-links`,
  `check-claims`, `check-readme-sync`, `git diff --check`: PASS.
- `scripts/test-regressions`: 51/51 PASS (includes FrozenTaskPassability
  over all 87 frozen tasks and all grader exemption matrices).
- `scripts/test-upgrade`: 33/33 PASS (includes NoLift/Mixed/Trigger/
  ResearchAnchors floor guards).
- `scripts/run-evals`, `test-archetypes`, `check-demos`,
  `check-packages` (offline path): PASS per prior runs on this branch.
- 18 synthetic grader probes + keyword-overlap audit (267 cases, 2
  genuine findings fixed, rest triaged as artifacts/ambiguity).

## Not done (unchanged)

- Controlled current-model lift for any changed skill: UNVERIFIED.
  Needs a pinned, human-authorized trial campaign with both paid keys;
  none were set and no paid CLI was invoked.
- Native host activation, browser/device/PostgreSQL/staging proof:
  UNVERIFIED / unavailable in this environment.
- Deferred source verifications: Fowler ParallelChange, XZ backdoor,
  Google review-demo guidance, canonical-hint specifics, cache-prefix
  specifics, Conventional Commits citation, test-pyramid citation,
  CrowdStrike details, CLS threshold. Skills stand without them.
- Independent review of these six commits: self-reviewed only.
- Branch is local and unpushed; no PR, push, deployment, or release.
