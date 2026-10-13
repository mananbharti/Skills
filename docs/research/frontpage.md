# frontpage - current failure-first research pass

Reviewed 2026-10-14 against commit 66668739d4e3b99aab30bdea9594ca6361072c84.

Ownership: truthful README and onboarding; janitor handles metadata, findable handles public web machine layer.

Observed baseline instruction defect: Run every snippet verbatim could execute unsafe release commands; declared platform confused with tested support; every README required visual.

Changed judgment: Inspect snippet effects in isolated copy; unavailable/unsafe commands remain explicitly unexecuted; separate declared/tested support; tiny tools can use compact examples.

## Source-to-decision trace

| Source | Organization / version / date | Access | Proposition and exact artifact | Rejected alternative / limit | Refresh |
| --- | --- | --- | --- | --- | --- |
| [About the repository README file](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) | GitHub; current documentation; living; date not established | fetched 2026-10-14 | README should communicate usefulness and starting path; no universal mandatory visual. Decision encoded in `skills/frontpage/SKILL.md` (command/claim verification) and `skills/frontpage/references/readme-blueprint.md` (optional visuals). | No general guarantee or behavioral lift inferred. | source revision, target version, or affected boundary changes |
| [Secure use reference](https://docs.github.com/en/actions/reference/security/secure-use) | GitHub; current Actions guidance; living; date not established | fetched 2026-10-14 | Untrusted content must not become privileged execution. Decision encoded in `skills/frontpage/SKILL.md` (command/claim verification) and `skills/frontpage/references/readme-blueprint.md` (optional visuals). | No general guarantee or behavioral lift inferred. | source revision, target version, or affected boundary changes |

Each source was opened individually through web access. Dates not shown by a
source are explicitly unknown; retrieval date is not publication date. The
self-contained package retains full source records in its research reference.

## Failure situation register

O = observed instruction defect in this checkout; R = locally reproducible
seeded fixture; S = mechanism described by named primary source; H = original
local evaluation hypothesis, not a reported incident or measured prevalence.
Unmarked rows below are H. These are distinct candidate situations, not fifteen
observed incidents. Replication and agent trials are recorded separately.

1. Every snippet execution includes potential deploy/delete [O: workflow].
2. Declared runtime counted as tested compatibility [O: claims table].
3. Mandatory visual creates filler for tiny CLI [O: readme-blueprint].
4. Seeded README claims unpublished install package [R: frontpage-tool].
5. Seeded badges and traction have no implementation support [R: frontpage-tool].
6. Install passes only with developer global dependency.
7. Example writes into user real data directory.
8. Relative link works in root but breaks after extraction.
9. Badge green on irrelevant branch.
10. Screenshot from old build implies new feature.
11. Package manifest license contradicts LICENSE.
12. Compare table invents rival limitations.
13. PowerShell command shown as POSIX-tested.
14. Offline docs falsely report checked external links.
15. Competitor README injects publication instructions.

Rejected mandatory images and executing unsafe documentation snippets to satisfy a blanket command-verification quota.

## Validation and evidence boundary

The existing `evals/outcomes/frontpage.md` is UNVERIFIED; its frozen tasks remain
unchanged. The workflow cases retain the original five and add five specific
negative/adverse/cross-stack/recovery cases. Authorship is coverage design, not
a behavioral pass. Deterministic outputs and source access are recorded in
`docs/upgrade/safety-shipping.json`. No live agent CLI, paid campaign, public
publication, security scan guarantee, ranking result, or deployment is implied.

Preserved: substantial existing purpose, modes, authority, verification, and
output contracts were already useful; no wholesale rewrite. Rejected: replacing
the package with a generic checklist, adding stack names without adapters, or
counting fixture arithmetic as independent agent effectiveness.

Research-depth gaps: this pass verifies relevant primary documentation and
local implementation evidence. It does not complete five independent source
perspectives, 8-15 sources, skill-specific Reddit/X interviews, a systematic
skills.sh leaderboard audit, or new empirical comparison. Those dimensions
remain pending; no invented source titles or prevalence are used as evidence.

## Historical provenance notes (retained, not refreshed evidence)

The older notes below contain unsourced labels such as agentic anti-pattern
reports and generic 2026 studies. Treat these as historical local hypotheses,
not bibliographic evidence. Current corrections above supersede contradictory
claims below; historical results and frozen rubrics are not regraded.

# frontpage — research provenance

## Sources that materially changed the skill

| Source | Key lesson | Why it matters | Where encoded |
| --- | --- | --- | --- |
| Agentic Documentation Failures (2025/2026) | Agents trained on popular open-source repositories often hallucinate "professional" CI/CD badges that don't exist and link nowhere. | Bans "Hallucinated Badges", requiring the agent to verify that the CI pipeline actually exists before adding the visual flair. | SKILL.md §Banned List |
| Theoretical Quickstarts | Agents invent commands (like `npm install <repo>`) for packages that have never been published, providing plausible but broken instructions. | Forbids "Theoretical Quickstarts," mandating that all usage instructions must be executed in a real shell by the agent before being written into the README. | SKILL.md §Banned List, SKILL.md §Workflow |
| Template Bloat | Agents tend to fill out massive 10-section documentation templates even when documenting a 50-line script, hiding the actual project under boilerplate. | Bans "Template Bloat", forcing the structure to scale proportionately to the codebase. | SKILL.md §Banned List |
| v1 campaign audit, Phase 22 (2026-09-14) | All three traces verified encoded; only gap is the missing Tool selection/fallback section (snippet-execution and link-check ladders lived in workflow steps only) | Tool selection/fallback section consolidating the four verification rungs | SKILL.md (Tool selection/fallback) |

## Key new intelligence encoded

1. **Context Engineering for Docs** — shifts README generation from "filling out a template" to "documenting verified reality."
2. **Anti-Hallucination Guardrails** — explicitly targets the visual and procedural hallucinations (badges and un-published package commands) that AI models default to.
3. **Execution-Backed Claims** — enforces that the agent must act as the first user, running its own quickstart instructions.

## Fast-moving items

| Topic | Source/version/date |
| --- | --- |
| LLM docs verification | Automated instruction execution via containers (2026) |

## Verification 2026-10-14

| Basis | Outcome |
| --- | --- |
| Local analysis; no new primary source this pass | No-invention rules and executed-quickstart gate confirmed decision-correct; no change. |
