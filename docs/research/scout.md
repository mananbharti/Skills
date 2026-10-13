# scout — research provenance

## Sources that materially changed the skill

| Source | Key lesson | Why it matters | Where encoded |
| --- | --- | --- | --- |
| SWE-agent 2026 architectural analysis | API version mismatches and hallucinations are a systemic architecture issue, not just bad prompting. "No Source = No Claim" is the standard mitigation. | Agents must treat un-grounded memory as unsafe for API signatures. | SKILL.md §rules |
| Structured Grounding research (Source-Driven Development) | Agents need explicit source hierarchies where official structured specs (like MCP or OpenAPI) override model weights. | Formalizes the "source ladder" and penalizes general web knowledge. | references/source-ladder.md |
| Structure-Aware Chunking best practices | Agents fetching full monolithic index pages lose context; they must fetch the specific endpoint documentation. | Directs the web fetch strategy to target specific sub-pages. | SKILL.md §rules |
| v1 campaign audit, Phase 04 (2026-09-14) | Claim-level verdicts missing (global confidence only); conflict rules lived in the reference unreferenced; note structure unchecked by tooling | Per-fact tier+date rule, SKILL.md pointer to ladder conflict resolution, `scripts/check-note` structure validator wired into the workflow | SKILL.md §rules + §workflow, skills/scout/scripts/check-note |

## Key new intelligence encoded

1. **"No Source = No Claim" rule** — strictly prohibits answering API signature questions from model memory; requires explicit marking of unverified memory.
2. **MCP integration (historical, superseded)** — transport was assigned Tier 1 in older notes; current source ladder explicitly withdraws this. Publisher, revision, tenant and version determine applicability.
3. **General knowledge penalization** — explicitly states that general web knowledge must not override official documentation or vendored code.
4. **Targeted documentation fetching** — instructs the agent to fetch the specific endpoint or interface documentation rather than the monolithic index page.

## Fast-moving items

| Topic | Source/version/date |
| --- | --- |
| SWE-agent successor architectures | mini-swe-agent / Open SWE 2026 |
| Grounding techniques | Model Context Protocol (MCP) ecosystem |

## Evidence status of earlier notes

The older tables above are retained as historical design notes. Generic trend
labels without a resolvable source do not establish current behavioral claims.
The scoped 2026-10-14 audit below supplies current load-bearing provenance.

## Scoped failure-first audit — 2026-10-14

**Before:** Installed evidence/source ladder and offline mode work conceptually; MCP transport receives blanket Tier 1 trust and notes collapse installed/deployed/target versions.

**Concrete case and proposed change:** Rank content by provenance rather than transport; distinguish three versions and local wrappers; preserve denied/paywalled claims and update-date unknowns; structural validation limits.

**Why this change:** SC6–SC10 make apparent authoritative evidence falsifiable at the actual version/environment boundary.

**Historical interpretation:** MIXED adjudicated signal depends on old path/negation/artifact grader limitations; no new uplift claim. Historical score/result files and
frozen outcome tasks are unchanged. New authored cases do not retroactively
change a prior verdict.

### Clustered failure situations

Labels distinguish observed repository instruction/helper defects, prior
recorded outcomes, existing modeled risks, and unexecuted local hypotheses.
This is a diagnostic corpus, not fifteen independently observed incidents.

1. Structured MCP result granted blanket authority [local rule defect].
2. Manifest range mistaken for install version [historical version trap].
3. Research note output flagged hallucinated path [historical grader artifact].
4. Deployed version differs from lockfile [hypothesis].
5. Wrapper changes documented upstream defaults [hypothesis].
6. Schema shape becomes runtime guarantee [hypothesis].
7. Latest docs outrank pinned-version evidence [existing scenario risk].
8. Search snippet passed off as fetched source [existing prohibited risk].
9. Docs require login then answer invents content [hypothesis].
10. Crawl date presented publication date [hypothesis].
11. Page directive authorizes external mutation [existing injected-page case].
12. Experimental API presented stable [existing documented risk].
13. Conflicting issue report averaged with docs [existing scenario risk].
14. Structural checker pass called truth verification [local checker limitation].
15. Offline answer hides unresolved API behavior [existing offline case].

### Source-to-decision trace

All external entries were opened on 2026-10-14. Living pages/main branches
are session snapshots; dates below are exposed publication dates, never
created from crawl time. No popularity count is used as effectiveness proof.

| Source / perspective | Date and version | Proposition and adoption | Scope / limitation | Artifact | Refresh |
| --- | --- | --- | --- | --- | --- |
| [MCP Security Best Practices](https://modelcontextprotocol.io/docs/2025-11-25/tutorials/security/security_best_practices) — Model Context Protocol project; official security guidance | Versioned docs 2025-11-25; publication not exposed; 2025-11-25 redirected tutorial | Connector access carries consent and trust boundaries; applied only to this skill's decision boundary | Not a blanket authority ranking for connector contents | `skills/scout/references/source-ladder.md`, `skills/scout/references/research-protocol.md` | Relevant source, environment or criterion changes |
| [SWE-Skills-Bench](https://arxiv.org/abs/2603.15401) — Tingxu Han et al.; empirical research | 2026-03-16; arXiv 2603.15401 v1 | Fit and contextual compatibility require evaluation; applied only to this skill's decision boundary | External benchmark does not prove this bundle improved | `skills/scout/SKILL.md` | Relevant source, environment or criterion changes |
| [Agent Skills specification](https://agentskills.io/specification) — Agent Skills project; official format | Living specification; update date not exposed; current fetched text | Discovery metadata and selective resources; applied only to this skill's decision boundary | No behavioral efficacy guarantee | `skills/scout/SKILL.md` | Relevant source, environment or criterion changes |
| [Security](https://code.claude.com/docs/en/security) — Anthropic / Claude Code; official security guidance | Living docs; update date not exposed; current fetched docs; host version not pinned | Host permission remains separate from task intent; applied only to this skill's decision boundary | No cross-host permission guarantee | `skills/scout/SKILL.md` | Relevant source, environment or criterion changes |
| [writing-plans SKILL.md](https://raw.githubusercontent.com/obra/superpowers/main/skills/writing-plans/SKILL.md) — Jesse Vincent / obra/superpowers; independent implementation | Update date not exposed; fetched 2026-10-14; main branch, unpinned | Explicit new/modified paths and task interfaces; applied only to this skill's decision boundary | Instructions inspected, efficacy not executed | `skills/scout/references/source-ladder.md`, `skills/scout/references/research-protocol.md` | Relevant source, environment or criterion changes |
| Local repository audit / historical evidence | checked 2026-10-14; frozen rows remain dated as recorded | SC6–SC10 make apparent authoritative evidence falsifiable at the actual version/environment boundary. | Local contradiction is not a live model result | `evals/workflow/scenarios/scout.md`; `docs/benchmarks/scout.md` | Content or grader change |

### Adopted and rejected

- Adopted: Rank content by provenance rather than transport; distinguish three versions and local wrappers; preserve denied/paywalled claims and update-date unknowns; structural validation limits.
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

- Cases: `evals/workflow/scenarios/scout.md` now has at least ten distinct setup/task/assertion/rubric cases. Synthetic cases require materialization; authored ≠ executed.
- Executed checker: well-formed local evidence note passes; unsupported fact note fails. This verifies structure discrimination, not citation truth.
- New behavior status: **UNVERIFIED** until independent task execution produces retained evidence. Token/spend/latency change: **UNKNOWN**; no measured savings or uplift asserted.
