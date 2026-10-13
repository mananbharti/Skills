# spelunk — research provenance

## Sources that materially changed the skill

| Source | Key lesson | Why it matters | Where encoded |
| --- | --- | --- | --- |
| Behavioral code analysis (2025 engineering blogs) | Technical debt isn't just "bad code" — it's code that actively causes friction. Churn × complexity quadrant pinpoints it. | Maps discovery to organizational impact rather than just static analysis. | SKILL.md risk-map mode, discovery-map.md hotspots |
| Cognitive debt discussions (2025 tech leadership) | The gap between implementation and team understanding is as dangerous as tech debt. | Adds a new failure mode to hunt for during discovery. | SKILL.md risk-map mode |
| Outside-in discovery patterns | Starting with the request lifecycle grounds exploration in real-world behavior, not abstract architecture. | Makes "teach" mode concrete rather than hand-wavy. | SKILL.md teach mode |
| v1 campaign audit, Phase 03 (2026-09-14) | Discovery order never required tracing a path before broadening; symbol lookup had no precision ladder; deep maps lacked commit/dirty provenance; inventory missed manifests + generated/vendor candidates and leaked repo-wide churn into subdir scans | Trace-one-path-early step, precise-symbols-before-grep rung, commit/dirty provenance header, inventory manifests + generated/vendor sections, `-- .` churn scoping | SKILL.md discovery order + deep output, scripts/inventory |

## Key new intelligence encoded

1. **Churn × Complexity quadrant** — formalizes the behavioral analysis of the codebase, distinguishing active friction zones from stable landmines.
2. **Cognitive debt tracking** — explicitly looks for signs that the codebase has outgrown the team's mental model (stale comments, TODO-in-prod).
3. **Trust-boundary surfacing in quick mode** — ensures that even fast answers highlight critical security/auth/PII boundaries if they are in play.
4. **Concrete request lifecycle narrative** — requires naming real symbols and paths in teach mode, rather than just abstract descriptions.

## Fast-moving items

| Topic | Source/version/date |
| --- | --- |
| Behavioral code analysis | CodeScene and related 2025 methodologies |
| Cognitive debt in engineering | Modern tech leadership discourse |

## Evidence status of earlier notes

The older tables above are retained as historical design notes. Generic trend
labels without a resolvable source do not establish current behavioral claims.
The scoped 2026-10-14 audit below supplies current load-bearing provenance.

## Scoped failure-first audit — 2026-10-14

**Before:** Question-led mapping, trace-first discovery and inventory exist; scanner excludes .venv in one section but counts/scans it elsewhere; dynamic/generated ownership needs sharper evidence.

**Concrete case and proposed change:** Consistent scanner exclusions for cache/vendor/generated trees; current-source check on memory; conditional runtime registration/source-generator ownership evidence.

**Why this change:** SP9 deterministic reproduction shows baseline six sources versus one first-party source; SP6/SP7 prevent owner assignment from name matches.

**Historical interpretation:** MIXED plus later grader-dominated negated-path artifacts are preserved; mapping efficiency remains unknown. Historical score/result files and
frozen outcome tasks are unchanged. New authored cases do not retroactively
change a prior verdict.

### Clustered failure situations

Labels distinguish observed repository instruction/helper defects, prior
recorded outcomes, existing modeled risks, and unexecuted local hypotheses.
This is a diagnostic corpus, not fifteen independently observed incidents.

1. Vendor/cache files inflate source count [executed local defect].
2. Debt/largest scans use different ignore boundary [executed local defect].
3. Churn reference command omits --since flag [local command defect].
4. Defined plugin mistaken for registered owner [hypothesis].
5. Generated client mistaken for source of truth [hypothesis].
6. Root package commands assigned to sibling app [existing scenario risk].
7. README architecture contradicts code [existing fixture case].
8. Recent map survives branch switch incorrectly [hypothesis].
9. Lockfile presence becomes deployed-version proof [hypothesis].
10. Environment values copied into report [existing prohibited risk].
11. No manifests produces invented test command [existing scenario risk].
12. Giant repository triggers recursive full read [existing budget risk].
13. Churn alone labeled defect [existing documented risk].
14. Negated missing paths fail historical grader [historical grader artifact].
15. Runtime inferred edge presented observed [hypothesis].

### Source-to-decision trace

All external entries were opened on 2026-10-14. Living pages/main branches
are session snapshots; dates below are exposed publication dates, never
created from crawl time. No popularity count is used as effectiveness proof.

| Source / perspective | Date and version | Proposition and adoption | Scope / limitation | Artifact | Refresh |
| --- | --- | --- | --- | --- | --- |
| [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) — Anthropic; official engineering report | 2025-09-29; web article | Question-directed retrieval and compact state; applied only to this skill's decision boundary | Vendor report, not a universal optimum | `skills/spelunk/SKILL.md` | Relevant source, environment or criterion changes |
| [git-status documentation](https://git-scm.com/docs/git-status) — Git project; official tool docs | Living manual; update not assigned here; current fetched manual; local git version not pinned | Index/worktree evidence must be read before editing; applied only to this skill's decision boundary | A branch name alone does not isolate dirty state | `skills/spelunk/references/evidence-protocol.md` | Relevant source, environment or criterion changes |
| [SWE-Skills-Bench](https://arxiv.org/abs/2603.15401) — Tingxu Han et al.; empirical research | 2026-03-16; arXiv 2603.15401 v1 | Fit and contextual compatibility require evaluation; applied only to this skill's decision boundary | External benchmark does not prove this bundle improved | `skills/spelunk/SKILL.md` | Relevant source, environment or criterion changes |
| [Security](https://code.claude.com/docs/en/security) — Anthropic / Claude Code; official security guidance | Living docs; update date not exposed; current fetched docs; host version not pinned | Host permission remains separate from task intent; applied only to this skill's decision boundary | No cross-host permission guarantee | `skills/spelunk/SKILL.md` | Relevant source, environment or criterion changes |
| [writing-plans SKILL.md](https://raw.githubusercontent.com/obra/superpowers/main/skills/writing-plans/SKILL.md) — Jesse Vincent / obra/superpowers; independent implementation | Update date not exposed; fetched 2026-10-14; main branch, unpinned | Explicit new/modified paths and task interfaces; applied only to this skill's decision boundary | Instructions inspected, efficacy not executed | `skills/spelunk/references/evidence-protocol.md` | Relevant source, environment or criterion changes |
| Local repository audit / historical evidence | checked 2026-10-14; frozen rows remain dated as recorded | SP9 deterministic reproduction shows baseline six sources versus one first-party source; SP6/SP7 prevent owner assignment from name matches. | Local contradiction is not a live model result | `evals/workflow/scenarios/spelunk.md`; `docs/benchmarks/spelunk.md` | Content or grader change |

### Adopted and rejected

- Adopted: Consistent scanner exclusions for cache/vendor/generated trees; current-source check on memory; conditional runtime registration/source-generator ownership evidence.
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

- Cases: `evals/workflow/scenarios/spelunk.md` now has at least ten distinct setup/task/assertion/rubric cases. Synthetic cases require materialization; authored ≠ executed.
- Executed deterministic reproduction: temporary first-party/cache/vendor/generated tree; old scanner reported 6 sources versus expected 1; current scanner reports 1 source, 1 test, excludes noise from debt/largest reports; JSON parsed. First edit failed shell continuation handling; repaired and rerun passed.
- New behavior status: **UNVERIFIED** until independent task execution produces retained evidence. Token/spend/latency change: **UNKNOWN**; no measured savings or uplift asserted.
