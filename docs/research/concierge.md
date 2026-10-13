# concierge — research provenance

## Sources that materially changed the skill

| Source | Key lesson | Why it matters | Where encoded |
| --- | --- | --- | --- |
| Anthropic, Effective context engineering for AI agents (Sep 2025) | Context is finite; harness rules encode model weaknesses and age as models improve | Avoid brittle micro-chains; prefer invariants | SKILL.md §5, routing.md rules |
| Research synthesis on over-routing failures (2026) | Each unnecessary handoff adds a seam where information can degrade | Explicit "smallest chain" rule strengthened | SKILL.md intro, routing.md rule 1 |
| "Route by uncertainty source" pattern (2025–2026 deficit-led routing) | Same noun routes to different specialists depending on what's missing | New "what is missing?" decision table | SKILL.md §5, routing.md §Step 0 |
| OpenAI Agents SDK orchestration docs | Manager vs handoff: keep ownership for bounded subtasks; full handoff when the specialist domain becomes the task | Specialist completion predicates | routing.md completion predicates table |
| Simon Smith on skill-library duplication/discovery | Skill libraries scale into overlap and confusion | Routing should operate from compact manifest, not rediscover skills | SKILL.md notes, routing.md rule 5 |
| v1 campaign audit, Phase 01 (2026-09-14) | Predicate table covered 10/28 skills; `handsfree` had no pattern row; no loop ceiling existed | Router could not tell when 18 specialists were done, misrouted autonomy complaints, and could re-dispatch forever | routing.md completion predicates (28/28), handsfree + direct + none pattern rows, rule 7 loop detection |

## Key new intelligence encoded

1. **Uncertainty-source routing** — "What is missing that blocks correct next action?" table replaces
   topic-noun matching for non-obvious cases
2. **Evidence reuse table** — concrete examples of when to skip re-running a skill
3. **Completion predicates** — each specialist has a defined return condition
4. **Capability rungs** — `capability-degradation.md` gives explicit fallback tiers with disclosure rules
5. **Harness aging note** — skill explicitly avoids brittle if/then chains that become stale
6. **Loop ceiling** — same domain dispatched at most twice per task; the third dispatch is defined as failure
7. **Direct/none as first-class routes** — micro-changes and non-repo requests terminate in concierge instead of entering a chain

## Rejected / weak ideas

| Idea | Why not adopted |
| --- | --- |
| Static route scores (numeric formula) | Adds complexity without evidence of better decisions; model judgment is flexible |
| Skill manifest generation script | Useful but belongs in separate tooling, not runtime routing |
| Hardcoded "always plan before coding" rule | Contradicted by Anthropic guidance on harness aging |

## Fast-moving items

| Topic | Source/version/date |
| --- | --- |
| OpenAI Agents SDK orchestration patterns | openai.github.io/openai-agents-python — 2025 |
| Anthropic context engineering | anthropic.com/engineering — Sep 29, 2025 |
| Over-routing error amplification research | Field research synthesis, 2026 |

## Evidence status of earlier notes

The older tables above are retained as historical design notes. Generic trend
labels without a resolvable source do not establish current behavioral claims.
The scoped 2026-10-14 audit below supplies current load-bearing provenance.

## Scoped failure-first audit — 2026-10-14

**Before:** Router has direct/none rows and a loop ceiling, but initial workflow still inventories first, dates imply freshness, user messages lose authority, and auth/money topics imply gates.

**Concrete case and proposed change:** Choose direct/none before discovery; restore current human authority; scope freshness to candidate/environment; handoff carries typed fields; repeat identity survives renaming; risk follows action.

**Why this change:** C6/C8/C9/C10 expose unnecessary work, stale verdict reuse, and loops without requiring another orchestrator.

**Historical interpretation:** MIXED historical routing; later C1 order contract contradicted audit-before-polish and remains defective-task evidence. Historical score/result files and
frozen outcome tasks are unchanged. New authored cases do not retroactively
change a prior verdict.

### Clustered failure situations

Labels distinguish observed repository instruction/helper defects, prior
recorded outcomes, existing modeled risks, and unexecuted local hypotheses.
This is a diagnostic corpus, not fifteen independently observed incidents.

1. Inventory before a direct answer [local rule conflict].
2. Recent verdict reused across candidate/environment [local rule gap].
3. Human request treated as incapable of granting authority [local rule defect].
4. Auth noun triggers unrelated full audit [local rule defect].
5. No-skill translated request over-routes [hypothesis].
6. Explicit skill re-enters concierge [hypothesis].
7. Same blocker renamed evades ceiling [hypothesis].
8. UI flow and surface fixes sequence incorrectly [historical task conflict].
9. Library metadata publication becomes deployment [hypothesis].
10. Missing specialist falsely claimed executed [existing documented risk].
11. Tool probe creates an external side effect [existing prohibited risk].
12. A new branch hides dirty-tree overlap [hypothesis].
13. Compound task loses accepted constraints at handoff [hypothesis].
14. Browser fallback is reported as browser proof [existing scenario risk].
15. Installed metadata routes differently from native activation [historical measurement limitation].

### Source-to-decision trace

All external entries were opened on 2026-10-14. Living pages/main branches
are session snapshots; dates below are exposed publication dates, never
created from crawl time. No popularity count is used as effectiveness proof.

| Source / perspective | Date and version | Proposition and adoption | Scope / limitation | Artifact | Refresh |
| --- | --- | --- | --- | --- | --- |
| [Agent Skills specification](https://agentskills.io/specification) — Agent Skills project; official format | Living specification; update date not exposed; current fetched text | Discovery metadata and selective resources; applied only to this skill's decision boundary | No behavioral efficacy guarantee | `skills/concierge/SKILL.md` | Relevant source, environment or criterion changes |
| [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) — Anthropic; official engineering report | 2025-09-29; web article | Question-directed retrieval and compact state; applied only to this skill's decision boundary | Vendor report, not a universal optimum | `skills/concierge/SKILL.md` | Relevant source, environment or criterion changes |
| [SkillsBench](https://arxiv.org/abs/2602.12670) — Xiangyi Li et al.; empirical research | 2026-02-13; revised 2026-06-14; arXiv 2602.12670 v4 | Focused skills warrant testing against broad bundles; applied only to this skill's decision boundary | Aggregate results do not establish this skill lift | `skills/concierge/SKILL.md` | Relevant source, environment or criterion changes |
| [MCP Security Best Practices](https://modelcontextprotocol.io/docs/2025-11-25/tutorials/security/security_best_practices) — Model Context Protocol project; official security guidance | Versioned docs 2025-11-25; publication not exposed; 2025-11-25 redirected tutorial | Connector access carries consent and trust boundaries; applied only to this skill's decision boundary | Not a blanket authority ranking for connector contents | `skills/concierge/references/routing.md` | Relevant source, environment or criterion changes |
| [Skills that never fire discussion](https://www.reddit.com/r/ClaudeAI/comments/1usls7m/anyone_else_has_a_graveyard_of_claude_code_skills/) — ProperAssociation322 and _suren on Reddit; community anecdote | Relative age only; exact date unverified; fetched post and one visible reply | Overlap and invocation count are different concerns; applied only to this skill's decision boundary | Selection bias; not measured activation evidence | `skills/concierge/SKILL.md` | Relevant source, environment or criterion changes |
| Local repository audit / historical evidence | checked 2026-10-14; frozen rows remain dated as recorded | C6/C8/C9/C10 expose unnecessary work, stale verdict reuse, and loops without requiring another orchestrator. | Local contradiction is not a live model result | `evals/workflow/scenarios/concierge.md`; `docs/benchmarks/concierge.md` | Content or grader change |

### Adopted and rejected

- Adopted: Choose direct/none before discovery; restore current human authority; scope freshness to candidate/environment; handoff carries typed fields; repeat identity survives renaming; risk follows action.
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

- Cases: `evals/workflow/scenarios/concierge.md` now has at least ten distinct setup/task/assertion/rubric cases. Synthetic cases require materialization; authored ≠ executed.
- Deterministic checks validate format/names/resource paths, not domain decision quality. No live comparison or agent CLI was invoked for this skill.
- New behavior status: **UNVERIFIED** until independent task execution produces retained evidence. Token/spend/latency change: **UNKNOWN**; no measured savings or uplift asserted.

## Independent review follow-through - 2026-10-14

Independent review found the browser capability probe hardcoded about:blank despite host URL restrictions. The probe now occurs on a task-appropriate permitted page and respects denied local-file access. Trace: skills/concierge/SKILL.md capability inventory.

This resolves an observed instruction conflict; it does not establish lift or
change historical grades. The fresh review and forward-trial records remain
separate evidence.

## Verification 2026-10-14

| Basis | Outcome |
| --- | --- |
| Local analysis + prior ledger; no new external source | Softened unsourced handoff-degradation claim to mechanism; gated gh probe on `command -v gh`. |
