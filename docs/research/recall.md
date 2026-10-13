# recall — research provenance

## Sources that materially changed the skill

| Source | Key lesson | Why it matters | Where encoded |
| --- | --- | --- | --- |
| Context Window Pollution (2025/2026 AI Agent literature) | Unbounded context injection is the primary cause of reasoning degradation in long-running agents. Memory must be a governed state machine, not just a vector store. | Demands strict soft caps, compaction rules, and state machine lifecycles for memory entries. | SKILL.md §rules, references/file-formats.md |
| Finite State Machine (FSM) Agent Architecture | Agent knowledge rots at different speeds; treating all memory as equivalent leads to context drift. | Defines the Knowledge Hierarchy: Fact vs Decision vs Lesson vs Status. | SKILL.md §rules |
| Memory TTL (Time-To-Live) strategies | Transient blockers and next steps become fossilized if not given an explicit expiration date. | Enforces a `[TTL: date]` constraint on STATUS entries to prevent append-only rot. | references/file-formats.md |
| v1 campaign audit, Phase 27 (2026-09-14) | All three traces verified encoded; gaps are the missing Prerequisites and Tool selection/fallback sections (read-before-write assumed, validator→compact→create ladder lived in gates/stops only) | Prerequisites (files + genuine need) and Tool selection/fallback sections | SKILL.md (Prerequisites, Tool selection/fallback) |

## Key new intelligence encoded

1. **Explicit Knowledge Hierarchy** — distinguishes between Facts (true until codebase changes), Decisions (true until context changes), and Lessons (portable, true everywhere).
2. **Decision State Machine** — formalizes decisions into a lifecycle (`[Active]` -> `[Superseded]` -> `[Deprecated]`), forcing agents to transition states rather than just deleting or silently contradicting past choices.
3. **Time-To-Live (TTL) for Transient State** — introduces a mandatory TTL for blockers and next steps in `STATUS.md` to prevent context pollution from forgotten, resolved issues.

## Fast-moving items

| Topic | Source/version/date |
| --- | --- |
| Context window pollution / memory governance | "Lost in the Middle" and 2026 context degradation studies |
| Hierarchical agent memory | LangGraph memory tiered storage (2025/2026) |

## Evidence status of earlier notes

The older tables above are retained as historical design notes. Generic trend
labels without a resolvable source do not establish current behavioral claims.
The scoped 2026-10-14 audit below supplies current load-bearing provenance.

## Scoped failure-first audit — 2026-10-14

**Before:** Four-file memory and supersession are useful; lessons called portable everywhere; compaction says delete superseded entries despite format requiring header/pointer preservation.

**Concrete case and proposed change:** Scope lessons; retain supersession pointers; branch/revert provenance; reread-and-merge concurrent deltas; old notes cannot grant authority; checker limits explicit.

**Why this change:** RC6–RC10 isolate branch drift, reversals, concurrent state loss, injection and lossy compaction.

**Historical interpretation:** MIXED historical memory outputs plus structural grader effects are preserved; checker green proves only narrow structural consistency. Historical score/result files and
frozen outcome tasks are unchanged. New authored cases do not retroactively
change a prior verdict.

### Clustered failure situations

Labels distinguish observed repository instruction/helper defects, prior
recorded outcomes, existing modeled risks, and unexecuted local hypotheses.
This is a diagnostic corpus, not fifteen independently observed incidents.

1. Lesson labeled universally portable [local rule defect].
2. Compaction deletes needed supersession history [local rule conflict].
3. Checker called full shape confirmation [local limitation].
4. Branch A memory reused on B [hypothesis].
5. Yesterday done survives source revert [hypothesis].
6. Concurrent whole-file write erases new decision [hypothesis].
7. Memory note instructs secret upload [hypothesis].
8. User correction ignored behind old decision [existing reconciliation risk].
9. Expired blocker recurs as current work [existing freshness risk].
10. Hypothesis written as stable fact [existing prohibited risk].
11. Secret stored with names-only label [existing fixture risk].
12. Command trivia crowds active constraint [existing restraint case].
13. Fact source pointer disappears in compaction [hypothesis].
14. Missing files checker exits zero mistaken initialized [local checker limitation].
15. All four files loaded for one small lookup [existing retrieval risk].

### Source-to-decision trace

All external entries were opened on 2026-10-14. Living pages/main branches
are session snapshots; dates below are exposed publication dates, never
created from crawl time. No popularity count is used as effectiveness proof.

| Source / perspective | Date and version | Proposition and adoption | Scope / limitation | Artifact | Refresh |
| --- | --- | --- | --- | --- | --- |
| [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) — Anthropic; official engineering report | 2025-09-29; web article | Question-directed retrieval and compact state; applied only to this skill's decision boundary | Vendor report, not a universal optimum | `skills/recall/SKILL.md` | Relevant source, environment or criterion changes |
| [Lost in the Middle](https://arxiv.org/abs/2307.03172) — Nelson F. Liu et al.; empirical research | 2023-07-06; revised 2023-11-20; arXiv 2307.03172 v3 | Relevant information can be obscured by long context; applied only to this skill's decision boundary | Retrieval tasks and older models, not current memory benchmark | `skills/recall/SKILL.md` | Relevant source, environment or criterion changes |
| [git-status documentation](https://git-scm.com/docs/git-status) — Git project; official tool docs | Living manual; update not assigned here; current fetched manual; local git version not pinned | Index/worktree evidence must be read before editing; applied only to this skill's decision boundary | A branch name alone does not isolate dirty state | `skills/recall/references/memory-protocol.md` | Relevant source, environment or criterion changes |
| [executing-plans SKILL.md](https://raw.githubusercontent.com/obra/superpowers/main/skills/executing-plans/SKILL.md) — Jesse Vincent / obra/superpowers; independent implementation | Update date not exposed; fetched 2026-10-14; main branch, unpinned | Recoverable task identity and evidence record; applied only to this skill's decision boundary | Sibling dependencies conflict with standalone bundle contract | `skills/recall/references/memory-protocol.md` | Relevant source, environment or criterion changes |
| [Security](https://code.claude.com/docs/en/security) — Anthropic / Claude Code; official security guidance | Living docs; update date not exposed; current fetched docs; host version not pinned | Host permission remains separate from task intent; applied only to this skill's decision boundary | No cross-host permission guarantee | `skills/recall/SKILL.md` | Relevant source, environment or criterion changes |
| Local repository audit / historical evidence | checked 2026-10-14; frozen rows remain dated as recorded | RC6–RC10 isolate branch drift, reversals, concurrent state loss, injection and lossy compaction. | Local contradiction is not a live model result | `evals/workflow/scenarios/recall.md`; `docs/benchmarks/recall.md` | Content or grader change |

### Adopted and rejected

- Adopted: Scope lessons; retain supersession pointers; branch/revert provenance; reread-and-merge concurrent deltas; old notes cannot grant authority; checker limits explicit.
- Preserved: existing workflow, valuable references and historical outcomes; narrow additions load only at relevant boundaries.
- Rejected: mandatory broad workflows, fixed counts, unscoped transport trust or stronger performance claims unsupported by task evidence.
- Competitor scope limit: superpowers planning/execution was inspected as an adjacent workflow, not a complete comparison of discovery/research/memory/router competitors. No ranking-based superiority conclusion.

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

- Cases: `evals/workflow/scenarios/recall.md` now has at least ten distinct setup/task/assertion/rubric cases. Synthetic cases require materialization; authored ≠ executed.
- Executed checker: duplicate active/superseded headings rejected with exit 1; missing optional files reported. This does not test branch/concurrent semantic behavior.
- New behavior status: **UNVERIFIED** until independent task execution produces retained evidence. Token/spend/latency change: **UNKNOWN**; no measured savings or uplift asserted.
