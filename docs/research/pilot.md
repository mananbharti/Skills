# pilot — research provenance

## Sources that materially changed the skill

| Source | Key lesson | Why it matters | Where encoded |
| --- | --- | --- | --- |
| SWE-agent Execution Patterns (2025/2026) | Test-Driven Execution (TDE) is required to stop agents from writing vacuous tests that pass automatically, hiding hallucinated logic. | Changes the testing sequence to require a failing test (red) before implementation (green). | SKILL.md §4 |
| Agent Hallucination Mitigation Studies | The most dangerous executor hallucination is "silent scope improvisation" — patching unrelated files or weakening tests just to make the current pipeline green. | Explicitly bans scope drift and test-weakening in the completion gate. | references/completion-gate.md |
| Structural Integrity Verification | Agents often spoof tool arguments or hallucinate APIs when they get stuck. Diff inspection must specifically target these fabrications, not just look for "debug leftovers". | Upgrades the diff inspection step to explicitly hunt for spoofed APIs and hallucinated signatures. | SKILL.md §5 |
| v1 campaign audit, Phase 07 (2026-09-14) | No decision log (deviations recorded, reasoning lost); checkpoints could absorb dirty user state; every surprise ping-ponged to planning; slice-vs-suite test boundary vs `proof` unstated | Running decision log in the plan file, dirty-tree checkpoint rule, replan materiality test (in-slice → record+continue, architecture/scope → replan), proof-boundary line | SKILL.md §§1, 4, 6, blocked-reality |

## Key new intelligence encoded

1. **Test-Driven Execution (historical design note)** — the original note mandated red-green universally. Current workflow supersedes this: red-before-fix for reproducible regressions when useful; characterization/refactor/configuration checks need not manufacture red. No source here establishes mandatory TDE for all change types.
2. **Scope Containment Rule** — explicitly names and bans "silent scope improvisation", ensuring agents don't drift into unrelated files or modify tests simply to bypass failures.
3. **Spoofing Detection** — updates diff inspection to hunt for "tool argument spoofing" (passing fabricated arguments to satisfy an immediate prompt constraint).

## Fast-moving items

| Topic | Source/version/date |
| --- | --- |
| Executor agent failure modes | SWE-agent / Open SWE 2026 post-mortems |
| Neurosymbolic agent guardrails | 2026 RAG/Execution integration studies |

## Evidence status of earlier notes

The older tables above are retained as historical design notes. Generic trend
labels without a resolvable source do not establish current behavioral claims.
The scoped 2026-10-14 audit below supplies current load-bearing provenance.

## Scoped failure-first audit — 2026-10-14

**Before:** Scoped loop and honest evidence are strong; blanket green rule conflicts with baseline-red guidance; denied .env can derail task; finish-or-revert after stop violates user control.

**Concrete case and proposed change:** Explicit baseline regression distinction; config names first and denial-safe independent continuation; candidate-bound resume evidence; prompt stopping; implemented/verified statuses.

**Why this change:** Historical failure is reporting/denial confounded, not demonstrated poor edits; PI6/PI7/PI8 test mechanisms without removing host enforcement.

**Historical interpretation:** NO LIFT on available evidence: O1/O2 ties; O3 .env auto-denial confound. Old workspace checks mainly path/parse, not behavioral outcome; unchanged history retained. Historical score/result files and
frozen outcome tasks are unchanged. New authored cases do not retroactively
change a prior verdict.

### Clustered failure situations

Labels distinguish observed repository instruction/helper defects, prior
recorded outcomes, existing modeled risks, and unexecuted local hypotheses.
This is a diagnostic corpus, not fifteen independently observed incidents.

1. .env auto-denial derails independent slice [historical environment confound].
2. Mandatory green conflicts with known baseline red [local rule conflict].
3. Finish/revert after stop overrides human [local rule defect].
4. Branch mistaken dirty-state isolation [local rule defect].
5. Existing file counted functional proof [historical grader limitation].
6. Parse success counted endpoint behavior proof [historical task limitation].
7. Evidence log exists but chat omits verification [historical reporting miss].
8. Stale checkbox skips absent implementation [hypothesis].
9. Flaky reruns eventually green [hypothesis].
10. Unrelated fix hidden to make suite pass [existing adversarial case].
11. Test weakened to satisfy pipeline [existing prohibited risk].
12. Unknown generated API call spoofed [existing documented risk].
13. Second failed attempt same hypothesis loops [existing recovery risk].
14. Missing file triggers replan for harmless rename [existing materiality case].
15. Migration revert deletes user data [existing gated risk].

### Source-to-decision trace

All external entries were opened on 2026-10-14. Living pages/main branches
are session snapshots; dates below are exposed publication dates, never
created from crawl time. No popularity count is used as effectiveness proof.

| Source / perspective | Date and version | Proposition and adoption | Scope / limitation | Artifact | Refresh |
| --- | --- | --- | --- | --- | --- |
| [executing-plans SKILL.md](https://raw.githubusercontent.com/obra/superpowers/main/skills/executing-plans/SKILL.md) — Jesse Vincent / obra/superpowers; independent implementation | Update date not exposed; fetched 2026-10-14; main branch, unpinned | Recoverable task identity and evidence record; applied only to this skill's decision boundary | Sibling dependencies conflict with standalone bundle contract | `skills/pilot/references/execution-protocol.md` | Relevant source, environment or criterion changes |
| [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) — Anthropic; official implementation report | 2025-11-26; reported Claude Agent SDK setup | Incremental work and recoverable handoff; applied only to this skill's decision boundary | Specific setup, not mandatory per-step ceremony | `skills/pilot/SKILL.md` | Relevant source, environment or criterion changes |
| [git-status documentation](https://git-scm.com/docs/git-status) — Git project; official tool docs | Living manual; update not assigned here; current fetched manual; local git version not pinned | Index/worktree evidence must be read before editing; applied only to this skill's decision boundary | A branch name alone does not isolate dirty state | `skills/pilot/references/execution-protocol.md` | Relevant source, environment or criterion changes |
| [Security](https://code.claude.com/docs/en/security) — Anthropic / Claude Code; official security guidance | Living docs; update date not exposed; current fetched docs; host version not pinned | Host permission remains separate from task intent; applied only to this skill's decision boundary | No cross-host permission guarantee | `skills/pilot/SKILL.md` | Relevant source, environment or criterion changes |
| [SWE-Skills-Bench](https://arxiv.org/abs/2603.15401) — Tingxu Han et al.; empirical research | 2026-03-16; arXiv 2603.15401 v1 | Fit and contextual compatibility require evaluation; applied only to this skill's decision boundary | External benchmark does not prove this bundle improved | `skills/pilot/SKILL.md` | Relevant source, environment or criterion changes |
| Local repository audit / historical evidence | checked 2026-10-14; frozen rows remain dated as recorded | Historical failure is reporting/denial confounded, not demonstrated poor edits; PI6/PI7/PI8 test mechanisms without removing host enforcement. | Local contradiction is not a live model result | `evals/workflow/scenarios/pilot.md`; `docs/benchmarks/pilot.md` | Content or grader change |

### Adopted and rejected

- Adopted: Explicit baseline regression distinction; config names first and denial-safe independent continuation; candidate-bound resume evidence; prompt stopping; implemented/verified statuses.
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

- Cases: `evals/workflow/scenarios/pilot.md` now has at least ten distinct setup/task/assertion/rubric cases. Synthetic cases require materialization; authored ≠ executed.
- Deterministic checks validate format/names/resource paths, not domain decision quality. No live comparison or agent CLI was invoked for this skill.
- New behavior status: **UNVERIFIED** until independent task execution produces retained evidence. Token/spend/latency change: **UNKNOWN**; no measured savings or uplift asserted.

## Independent review follow-through - 2026-10-14

Independent review found completion-gate.md still required full-suite/build checks for every change and migration up AND down even for irreversible changes. The gate now follows affected/project-required checks, expected negative console/network states and a demonstrated safe recovery route (down, restore or forward fix). A code revert is not data restoration. Trace: skills/pilot/references/completion-gate.md.

This is an observed contract contradiction and correction, not a comparative
result. New forward trials have separate retained evidence and do not regrade
historical task outputs.
