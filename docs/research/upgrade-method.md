# Upgrade method and source audit, 2026-10-14

This is maintainer evidence. External skill instructions were inspected as
data; none were installed into this chat's instruction hierarchy or copied.
Access date below is not a publication date. Mutable sources need a fresh check
when their behavior matters; installation observations pin CLI `1.7.2`.

| Source and perspective | Checked proposition | Decision and artifact | Limits / refresh |
| --- | --- | --- | --- |
| [Agent Skills specification](https://agentskills.io/specification), official standard | Entrypoint metadata and conditional package resources are distinct layers | `scripts/check-packages` copies one package alone and validates byte/executable preservation | Format compliance does not demonstrate task quality; refresh on spec change |
| [vercel-labs skills README](https://github.com/vercel-labs/skills), official CLI docs | Project-local, selected-skill, copy and all-skill options exist | Run pinned CLI against individual local packages and public bundle in disposable dirs | Local package install is not native host activation; refresh on CLI update |
| [Installer source](https://raw.githubusercontent.com/vercel-labs/skills/main/src/installer.ts), implementation | A canonical copy and agent paths can differ; copied references must travel | Compare complete package manifests after installation rather than count entrypoints alone | Mutable main inspected, CLI tests independently pin npm version |
| [skills issue 2472](https://github.com/vercel-labs/skills/issues/2472), maintainer issue report | Reported acceptance of whitespace-only required metadata | Retain strict local frontmatter checks; do not substitute CLI discovery for validation | Issue report is a hypothesis, not reproduced upstream here |
| [skills issue 2469](https://github.com/vercel-labs/skills/issues/2469), maintainer issue report | Home-directory local/global removal collision reported | Installation experiments use owned temp projects; never remove global skills | Removal defect not reproduced; no removal action needed |
| [SkillsBench v4](https://arxiv.org/abs/2602.12670v4), empirical research, revised 2026-06-14 | Matched task conditions and module scope matter | Outcome context defaults to entrypoint + on-demand resources; retain explicit eager mode | Its tasks/harnesses cannot establish gains for this bundle |
| [SWE-Skills-Bench](https://arxiv.org/abs/2603.15401), empirical research, submitted 2026-03-16 | Skill effects can be small or adverse and context compatibility matters | Preserve NO LIFT and regressions; do not report authored cases as behavioral success | Different fixtures and models; no transferred percentage claims |
| [METR RCT v2](https://arxiv.org/abs/2507.09089v2), empirical research, revised 2025-07-25 | Developer estimates of productivity may disagree with observed time | Keep human DX study pending and provide observation protocol | Experienced developers in its setting, not a universal beginner effect |
| [OpenAI SWE-bench audit](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/), evaluation risk | Faulty requirements and contamination compromise comparisons | New failing tests pin experiment identity: package, checker, fixture, context and runner | Existing historical defective grader flags remain disclosed and frozen |
| [NVIDIA SkillEvaluator](https://github.com/NVIDIA/SkillEvaluator), independent implementation | Static validation, overlap and live evaluation are different tiers | Release report separates package checks, independent review and live effectiveness | Not installed or run; its provider defaults can spend money |
| [Cisco skill-scanner](https://github.com/cisco-ai-defense/skill-scanner), security implementation | Skill scanning is a separate attack-surface check | No automatic scanner/provider install; retained scoped safety gates and copy integrity | This pass did not execute its scanner; static checks are not a security guarantee |
| [DyMalSkill v1](https://arxiv.org/html/2606.16287v1), adversarial research, 2026-06-15 | Instructions can induce modification of otherwise benign skill code | Require unchanged package identity when resuming an experiment | Hash comparison detects change after the fact; no OS isolation guarantee |
| [OWASP Agentic 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/), risk standard | Agency and trust boundaries need explicit treatment | Handoffs carry authorization separately from evidence text | Does not certify any application; domain findings still need repros |
| [ToxicSkills investigation](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/), incident investigation | Distributed skills can carry malicious payloads | Treat fetched skill files as evidence to inspect, not runtime authority | Vendor investigation and sample selection; no general prevalence claim here |
| [Token-usage thread](https://www.reddit.com/r/ClaudeCode/comments/1wwl9a4/any_recommendations_to_reduce_the_token_usage_for/), community signal | Users report overhead on simple tasks in large repos | Remove needless required lifecycle steps; test explicit no-skill routing | Anecdotal, not a measured improvement attributable to this bundle |
| [skills.sh trending](https://skills.sh/trending), distribution surface | Discoverability includes many task-specific modules outside software engineering | Select competitors by relevant behavior, not leaderboard counts | Snapshot is mutable and installs do not prove usefulness |

## Behavior audit of relevant alternatives

| Inspected package | Actual mechanism | Adopt / reject here |
| --- | --- | --- |
| [Superpowers writing-plans](https://raw.githubusercontent.com/obra/superpowers/main/skills/writing-plans/SKILL.md) | Plans distinguish created and modified files and communicate testable interfaces | Independently implement existing/proposed path distinction in `masterplan`; retain flexible task size |
| [Superpowers using-superpowers](https://raw.githubusercontent.com/obra/superpowers/main/skills/using-superpowers/SKILL.md) | Broad pre-response skill invocation rule with process-first routing | Reject global invocation tax; preserve intentional no-skill and one-owner paths |
| [Vercel web-design-guidelines](https://raw.githubusercontent.com/vercel-labs/agent-skills/main/skills/web-design-guidelines/SKILL.md) | Tiny entrypoint fetches current rules and returns file/line findings | Keep concise evidence-oriented findings; reject converting fetched content into authority or requiring network for every audit |
| [Anthropic skill-creator](https://raw.githubusercontent.com/anthropics/skills/main/skills/skill-creator/SKILL.md) | Parallel treatment/baseline artifacts plus hidden grading criteria and feedback loop | Separate authorship, execution and grading; do not import mandatory paid calls or pushier generic triggers |
| [addyosmani web-quality-skills](https://github.com/addyosmani/web-quality-skills) | Repository organizes measurable web-quality specialisms | Route actual performance to `hotpath` and user barriers to `friction`; do not infer lift from catalog presence |
| [Trail of Bits skills](https://github.com/trailofbits/skills) | Repository exposes scoped security-analysis workflows | Keep security preconditions and limitations explicit; no source text copied, no license compatibility claim |

Repository leads [mattpocock/skills](https://github.com/mattpocock/skills) and
[ECC](https://github.com/affaan-m/ECC) were opened, but this pass does not claim a
complete behavior or license audit of their contents. The requested X lead
failed to return content. No claim about its replies, popularity or consensus
is made. Per-skill notes distinguish primary-source decisions from original
local failure hypotheses; further community and comparative breadth remains
visible in the upgrade ledger rather than being padded with irrelevant links.

## Failure-first observations

- Required baseline checks passed before edits: 45 regression tests, 211 trigger
  labels, 158 workflows, 87 outcome tasks. Passing structure did not catch the
  contradictory dashboard labels or unnecessary runtime gates.
- `harness-before.txt` preserves failed tests for eager provenance loading and
  accepting resumed runs with changed package/runner/policy/fixture data.
- `trigger-before.txt` preserves the exact contradictory prompt. A new
  normalized-label check rejects it before measurement.
- `harness-after.txt` records the corrected integrity tests, using local fake
  agents. These results establish runner integrity only.

Evidence files live under `docs/upgrade/evidence/` in the repository. Historical
outcome records and their grader semantics are preserved. No paid CLI was run;
no spend-enabling keys were set by the agent.
