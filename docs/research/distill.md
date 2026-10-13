# distill — research provenance

## Sources that materially changed the skill

| Source | Key lesson | Why it matters | Where encoded |
| --- | --- | --- | --- |
| Requirements Engineering for LLMs (2025/2026 research) | LLMs are capable of proactive ambiguity detection (semantic, linguistic, functional) rather than just passive transcription. | Replaces "gap check" with active "ambiguity detection" targeting specific requirement failures. | SKILL.md §2 |
| BDD evolution / Executable Specifications (2026 trends) | Industry is moving away from brittle manual Gherkin (Given/When/Then) toward AI-native "agent-executable specifications" where the requirement itself is verifiable by a downstream agent. | Replaces "Acceptance criteria" with "Agent-executable specifications" to signal the shift in audience (agent, not just human QA). | SKILL.md, references/brief-template.md |
| Less is More (Agentic framework research) | High-quality, structurally precise requirements are critical for successful distillation into coding tasks. | The template requires actionable, verifiable facts over product philosophy. | references/brief-template.md |
| v1 campaign audit, Phase 05 (2026-09-14) | Repo grounding ran after question drafting, so questions could target nonexistent surfaces; no materiality test separated questions from assumptions | Ground-first reorder + per-question materiality test (name both answers and what each changes, else it is an assumption) | SKILL.md §workflow steps 2–3 |

## Key new intelligence encoded

1. **Active Ambiguity Detection** — formalized the gap check to specifically look for undefined boundaries, contradictory constraints, and missing definitions of "good".
2. **Agent-Executable Specifications** — deprecated standard "Acceptance criteria" in favor of criteria written explicitly for a downstream agent to verify without human judgment.
3. **Audience shift** — explicitly grounds the brief as an interface between agents (distiller → planner/implementer) rather than just a human-readable document.

## Fast-moving items

| Topic | Source/version/date |
| --- | --- |
| AI-native BDD alternatives | 2025–2026 software testing frameworks (TestMu, etc.) |
| LLM Requirements Engineering | NLP requirements ambiguity research |

## Evidence status of earlier notes

The older tables above are retained as historical design notes. Generic trend
labels without a resolvable source do not establish current behavioral claims.
The scoped 2026-10-14 audit below supplies current load-bearing provenance.

## Scoped failure-first audit — 2026-10-14

**Before:** Materiality test and repository grounding are sound; mandatory critique/confirmation can block authorized work; nontrivial compact output can omit boundaries and ownership.

**Concrete case and proposed change:** Optional critique by decision intent; respect implementation authorization; risk-bearing feature minimum preserves non-goals/A assumptions and actor/resource denial oracle.

**Why this change:** Historical O1 misses non-goal/assumption markers; heldout login misses boundaries/auth; new DI6 acceptance targets tenant behavior instead of adding document length.

**Historical interpretation:** NO LIFT: O1 treatment marker miss, O2 ceiling tie, O3 both miss required boundaries/auth. Small marker tasks do not measure downstream implementation success. Historical score/result files and
frozen outcome tasks are unchanged. New authored cases do not retroactively
change a prior verdict.

### Clustered failure situations

Labels distinguish observed repository instruction/helper defects, prior
recorded outcomes, existing modeled risks, and unexecuted local hypotheses.
This is a diagnostic corpus, not fifteen independently observed incidents.

1. Compact feature drops non-goals/assumptions [historical O1 miss].
2. Auth brief lacks actor/resource/security boundary [historical O3 miss].
3. Uncritiqued idea forces hotseat [local trigger defect].
4. Settled brief becomes duplicate approval gate [local rule defect].
5. Precise request automatically goes planning [local routing defect].
6. Client-only order filtering considered isolation [hypothesis].
7. Midnight has two valid timezone meanings [hypothesis].
8. Multiplayer reconnect lacks conflict owner [hypothesis].
9. Offline requirement silently assumes connectivity [hypothesis].
10. Absent analytics surface treated existing [existing missing-surface case].
11. Contradictory instant checkout/confirmation resolved silently [existing conflict case].
12. Explicit additional request mistaken scope smuggling [authored scenario defect].
13. Vague fast criterion assigned made-up target [existing requirement risk].
14. Build test called proof of authorization [hypothesis].
15. Question answered by repository asks human anyway [existing materiality risk].

### Source-to-decision trace

All external entries were opened on 2026-10-14. Living pages/main branches
are session snapshots; dates below are exposed publication dates, never
created from crawl time. No popularity count is used as effectiveness proof.

| Source / perspective | Date and version | Proposition and adoption | Scope / limitation | Artifact | Refresh |
| --- | --- | --- | --- | --- | --- |
| [Writing better Gherkin](https://cucumber.io/docs/bdd/better-gherkin/) — Cucumber project; official testing guidance | Living docs; update date not exposed; current fetched documentation | Acceptance describes behavior, not implementation trivia; applied only to this skill's decision boundary | Syntax cannot resolve stakeholder disagreement | `skills/distill/references/brief-template.md` | Relevant source, environment or criterion changes |
| [brainstorming SKILL.md](https://raw.githubusercontent.com/obra/superpowers/main/skills/brainstorming/SKILL.md) — Jesse Vincent / obra/superpowers; independent implementation | Update date not exposed; fetched 2026-10-14; main branch, unpinned | Distinguish settled work from missing product choices; applied only to this skill's decision boundary | Broad trigger/approval gate is not adopted | `skills/distill/SKILL.md` | Relevant source, environment or criterion changes |
| [SWE-Skills-Bench](https://arxiv.org/abs/2603.15401) — Tingxu Han et al.; empirical research | 2026-03-16; arXiv 2603.15401 v1 | Fit and contextual compatibility require evaluation; applied only to this skill's decision boundary | External benchmark does not prove this bundle improved | `skills/distill/SKILL.md` | Relevant source, environment or criterion changes |
| [Security](https://code.claude.com/docs/en/security) — Anthropic / Claude Code; official security guidance | Living docs; update date not exposed; current fetched docs; host version not pinned | Host permission remains separate from task intent; applied only to this skill's decision boundary | No cross-host permission guarantee | `skills/distill/SKILL.md` | Relevant source, environment or criterion changes |
| [writing-plans SKILL.md](https://raw.githubusercontent.com/obra/superpowers/main/skills/writing-plans/SKILL.md) — Jesse Vincent / obra/superpowers; independent implementation | Update date not exposed; fetched 2026-10-14; main branch, unpinned | Explicit new/modified paths and task interfaces; applied only to this skill's decision boundary | Instructions inspected, efficacy not executed | `skills/distill/references/brief-template.md` | Relevant source, environment or criterion changes |
| Local repository audit / historical evidence | checked 2026-10-14; frozen rows remain dated as recorded | Historical O1 misses non-goal/assumption markers; heldout login misses boundaries/auth; new DI6 acceptance targets tenant behavior instead of adding document length. | Local contradiction is not a live model result | `evals/workflow/scenarios/distill.md`; `docs/benchmarks/distill.md` | Content or grader change |

### Adopted and rejected

- Adopted: Optional critique by decision intent; respect implementation authorization; risk-bearing feature minimum preserves non-goals/A assumptions and actor/resource denial oracle.
- Preserved: existing workflow, valuable references and historical outcomes; narrow additions load only at relevant boundaries.
- Rejected: mandatory broad workflows, fixed counts, unscoped transport trust or stronger performance claims unsupported by task evidence.
- Competitor behavior inspected: superpowers planning/inline execution and brainstorming expose concrete interfaces and progress identity, but also mandatory subskills, per-task TDD or approval ceremonies. Adopt the useful evidence boundary; reject sibling-file dependence and unconditional ceremony. MIT license checked; no instruction text copied. skills.sh entry is discovery metadata, not a behavioral benchmark.

### Access and research limits

The skills.sh writing-plans listing and upstream SKILL.md were read; listing
summary and current upstream instructions differ, so behavior comes from the
upstream file. The GitHub issue query and supplied X post returned access
errors. A candidate mattpocock grill-me raw path returned 404; no behavior or
license claim is inferred. The initial MCP security URLs errored; the older
versioned URL redirected to the fetched 2025-11-25 security tutorial. Reddit
post and one visible reply supply anecdote only, with exact post date unknown.

This pass has focused sources and local failures. It does not complete eight
to fifteen high-quality sources or independent issue/community triangulation
for every skill. Non-English, mobile/game and long-running concurrency cases
are authored hypotheses until fixtures/runs exist. Refresh those gaps before
release claims rather than padding the bibliography.

### Verification and remaining outcome gap

- Cases: `evals/workflow/scenarios/distill.md` now has at least ten distinct setup/task/assertion/rubric cases. Synthetic cases require materialization; authored ≠ executed.
- Deterministic checks validate format/names/resource paths, not domain decision quality. No live comparison or agent CLI was invoked for this skill.
- New behavior status: **UNVERIFIED** until independent task execution produces retained evidence. Token/spend/latency change: **UNKNOWN**; no measured savings or uplift asserted.
