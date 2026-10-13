# masterplan — research provenance

## Sources that materially changed the skill

| Source | Key lesson | Why it matters | Where encoded |
| --- | --- | --- | --- |
| "Plan-Then-Execute" Agent Architecture (2025/2026) | Separating planning from execution dramatically reduces agent hallucination and looping. Plans must be written for the *executor agent*, not just humans. | Frames `masterplan` explicitly as the Planner creating an "Executable Plan" for `pilot`. | SKILL.md §introduction |
| Machine-Readable Task Structures (MCP / Open SWE) | Loose task descriptions ("delivers X") confuse executor agents. Tasks must be verb-led actions with measurable validation criteria. | Replaced vague slice deliverables with strict Action + Validation Criteria fields. | references/plan-template.md |
| AgDR (Agent Decision Records) | Standard ADRs are too slow for agent loops, but architecture choices still need rationale tracking in case the agent guesses wrong. | Embedded the AgDR structure into the Decisions section of the plan. | SKILL.md §3 |
| v1 campaign audit, Phase 06 (2026-09-14) | Paths lacked epistemic status (verified-or-nothing hid uncertainty); no ordering rule put unknown-resolving work first; irreversible steps had no explicit marking | confirmed/probable/to-discover path labels, uncertainty-collapses-first sequencing, IRREVERSIBLE slice marking with user checkpoint | SKILL.md §workflow steps 2+4, §quality gates |

## Key new intelligence encoded

1. **Planner/Executor Separation** — formally acknowledges that `masterplan` writes plans intended for `pilot` to execute systematically, shifting the audience from human developer to downstream agent.
2. **Verb-Led Executable Slices** — slices now require a specific Action instruction rather than a passive outcome description.
3. **Agent Decision Records (AgDR)** — architecture decisions made during planning are explicitly recorded with their alternatives and failure conditions to provide durable context for the executor.

## Fast-moving items

| Topic | Source/version/date |
| --- | --- |
| Agentic software documentation | "Shift Left" documentation trends (2025/2026) |
| Planner-Executor architectures | LangGraph / SWE-agent multi-agent patterns |

## Evidence status of earlier notes

The older tables above are retained as historical design notes. Generic trend
labels without a resolvable source do not establish current behavioral claims.
The scoped 2026-10-14 audit below supplies current load-bearing provenance.

## Scoped failure-first audit — 2026-10-14

**Before:** Slice contracts, invariants and uncertainty-first are valuable; paths must all preexist; absence of unknowns is called dishonest; fixed minimum slices produces ceremony.

**Concrete case and proposed change:** Existing/read versus proposed/new versus discovery; no artificial uncertainty/count minimum; criterion-to-slice coverage and honest data restoration boundary.

**Why this change:** Historical false-positive proposed/self-authored paths are separate from real slice-vocabulary misses; new MP6/MP7 target planning contradictions without changing frozen grading.

**Historical interpretation:** NO LIFT after historical adjudication; proposed/self-authored paths caused grader artifacts while two treatment outputs missed slice vocabulary. New path semantics need fresh blind execution. Historical score/result files and
frozen outcome tasks are unchanged. New authored cases do not retroactively
change a prior verdict.

### Clustered failure situations

Labels distinguish observed repository instruction/helper defects, prior
recorded outcomes, existing modeled risks, and unexecuted local hypotheses.
This is a diagnostic corpus, not fifteen independently observed incidents.

1. New component disallowed because never read [local rule defect].
2. Resolved unknowns must be reinvented [local rule defect].
3. Serious task forced into 5–12 slices [local rule defect].
4. Output artifact marked hallucination [historical grader artifact].
5. Slice vocabulary missing despite coherent prose [historical marker miss].
6. Public API callers omitted from coverage [hypothesis].
7. Parallel outcomes share schema file [existing concurrency risk].
8. Revert code claimed restore post-cutover data [hypothesis].
9. Backfill begins before compatible reader exists [hypothesis].
10. Auth denial criterion has no owning slice [hypothesis].
11. Discovery has no stop predicate [existing documented risk].
12. Migration hidden inside UI slice [existing risk case].
13. Speculative infrastructure inserted for imagined scale [existing prohibited risk].
14. Plan-only request implements code [existing authority boundary].
15. Current plan carries stale deployment assumptions [hypothesis].

### Source-to-decision trace

All external entries were opened on 2026-10-14. Living pages/main branches
are session snapshots; dates below are exposed publication dates, never
created from crawl time. No popularity count is used as effectiveness proof.

| Source / perspective | Date and version | Proposition and adoption | Scope / limitation | Artifact | Refresh |
| --- | --- | --- | --- | --- | --- |
| [writing-plans SKILL.md](https://raw.githubusercontent.com/obra/superpowers/main/skills/writing-plans/SKILL.md) — Jesse Vincent / obra/superpowers; independent implementation | Update date not exposed; fetched 2026-10-14; main branch, unpinned | Explicit new/modified paths and task interfaces; applied only to this skill's decision boundary | Instructions inspected, efficacy not executed | `skills/masterplan/references/planning-protocol.md`, `skills/masterplan/references/plan-template.md` | Relevant source, environment or criterion changes |
| [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) — Anthropic; official implementation report | 2025-11-26; reported Claude Agent SDK setup | Incremental work and recoverable handoff; applied only to this skill's decision boundary | Specific setup, not mandatory per-step ceremony | `skills/masterplan/SKILL.md` | Relevant source, environment or criterion changes |
| [Strangler Fig](https://martinfowler.com/bliki/StranglerFigApplication.html) — Martin Fowler; primary engineering guidance | 2024-08-22; web article | Incremental replacement has independent value; applied only to this skill's decision boundary | No universal decomposition or rollback guarantee | `skills/masterplan/SKILL.md` | Relevant source, environment or criterion changes |
| [SWE-Skills-Bench](https://arxiv.org/abs/2603.15401) — Tingxu Han et al.; empirical research | 2026-03-16; arXiv 2603.15401 v1 | Fit and contextual compatibility require evaluation; applied only to this skill's decision boundary | External benchmark does not prove this bundle improved | `skills/masterplan/SKILL.md` | Relevant source, environment or criterion changes |
| [git-status documentation](https://git-scm.com/docs/git-status) — Git project; official tool docs | Living manual; update not assigned here; current fetched manual; local git version not pinned | Index/worktree evidence must be read before editing; applied only to this skill's decision boundary | A branch name alone does not isolate dirty state | `skills/masterplan/references/planning-protocol.md`, `skills/masterplan/references/plan-template.md` | Relevant source, environment or criterion changes |
| Local repository audit / historical evidence | checked 2026-10-14; frozen rows remain dated as recorded | Historical false-positive proposed/self-authored paths are separate from real slice-vocabulary misses; new MP6/MP7 target planning contradictions without changing frozen grading. | Local contradiction is not a live model result | `evals/workflow/scenarios/masterplan.md`; `docs/benchmarks/masterplan.md` | Content or grader change |

### Adopted and rejected

- Adopted: Existing/read versus proposed/new versus discovery; no artificial uncertainty/count minimum; criterion-to-slice coverage and honest data restoration boundary.
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

- Cases: `evals/workflow/scenarios/masterplan.md` now has at least ten distinct setup/task/assertion/rubric cases. Synthetic cases require materialization; authored ≠ executed.
- Deterministic checks validate format/names/resource paths, not domain decision quality. No live comparison or agent CLI was invoked for this skill.
- New behavior status: **UNVERIFIED** until independent task execution produces retained evidence. Token/spend/latency change: **UNKNOWN**; no measured savings or uplift asserted.

## Independent review follow-through - 2026-10-14

Independent review found the quality gate contradicted its own irreversible-slice workflow by requiring a down path for all migrations. It now requires appropriate demonstrated recovery and states the loss/authorization boundary when reversal is impossible. Trace: skills/masterplan/SKILL.md Quality gates and references/planning-protocol.md recovery contract.

This is an observed contract contradiction and correction, not a comparative
result. New forward trials have separate retained evidence and do not regrade
historical task outputs.
