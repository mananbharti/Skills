# findable - current failure-first research pass

Reviewed 2026-10-14 against commit 66668739d4e3b99aab30bdea9594ca6361072c84.

Ownership: technical public web discovery/indexing; frontpage owns GitHub prose, janitor owns topics.

Observed baseline instruction defect: Curl called rendered HTML; client metadata universally invisible; robots/noindex advice conflicted; heading count and 2026 penalty claims unsupported.

Changed judgment: Separate initial response, rendered DOM and engine observation; noindex crawler-access rule; auth for privacy; equivalent-only canonicalization; no ranking/heading-count guarantees.

## Source-to-decision trace

| Source | Organization / version / date | Access | Proposition and exact artifact | Rejected alternative / limit | Refresh |
| --- | --- | --- | --- | --- | --- |
| [JavaScript SEO basics](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics) | Google Search Central; current Google Search guidance; living; date not established | fetched 2026-10-14 | Google can process rendered JavaScript content; consumers differ. Decision encoded in `skills/findable/SKILL.md` and `skills/findable/references/seo-checklist.md` (HTTP versus rendering, robots, canonical). | No general guarantee or behavioral lift inferred. | source revision, target version, or affected boundary changes |
| [Block indexing with noindex](https://developers.google.com/search/docs/crawling-indexing/block-indexing) | Google Search Central; current Google Search guidance; 2025-12-10 as page states | fetched 2026-10-14 | Blocked crawling can prevent reading noindex; noindex is not access control. Decision encoded in `skills/findable/SKILL.md` and `skills/findable/references/seo-checklist.md` (HTTP versus rendering, robots, canonical). | No general guarantee or behavioral lift inferred. | source revision, target version, or affected boundary changes |
| [Canonical URLs](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls) | Google Search Central; current guidance; living; date not established | fetched 2026-10-14 | Canonical signals consolidate materially duplicate URLs, not arbitrary different pages. Decision encoded in `skills/findable/SKILL.md` and `skills/findable/references/seo-checklist.md` (HTTP versus rendering, robots, canonical). | No general guarantee or behavioral lift inferred. | source revision, target version, or affected boundary changes |
| [Structured data policies](https://developers.google.com/search/docs/appearance/structured-data/sd-policies) | Google Search Central; current policies; living; date not established | fetched 2026-10-14 | Syntax validity does not establish eligibility or display. Decision encoded in `skills/findable/SKILL.md` and `skills/findable/references/seo-checklist.md` (HTTP versus rendering, robots, canonical). | No general guarantee or behavioral lift inferred. | source revision, target version, or affected boundary changes |

Each source was opened individually through web access. Dates not shown by a
source are explicitly unknown; retrieval date is not publication date. The
self-contained package retains full source records in its research reference.

## Failure situation register

O = observed instruction defect in this checkout; R = locally reproducible
seeded fixture; S = mechanism described by named primary source; H = original
local evaluation hypothesis, not a reported incident or measured prevalence.
Unmarked rows below are H. These are distinct candidate situations, not fifteen
observed incidents. Replication and agent trials are recorded separately.

1. Curl response called rendered DOM [O: tool fallback].
2. Correct JS-rendering prerequisite contradicted by banned list [O: SKILL].
3. Robots block prevents crawler seeing noindex [S: Google].
4. Private page privacy delegated to noindex [O: SEO checklist].
5. Seeded sitemap references missing page [R: findable-site].
6. Pagination canonicalized to different item set.
7. Structured data passes JSON parse but invents reviews.
8. CDN header overrides source robots meta.
9. Soft404 returns 200.
10. Locale alternate lacks reciprocal link.
11. Client canonical differs from initial response.
12. OG asset authenticated or missing.
13. Query crawler trap generates infinite duplicates.
14. Private staging included in public sitemap.
15. Search indexing lag mistaken for failed code fix.

Rejected mandatory SSR from crawler folklore, curl-as-renderer, canonicalizing different pagination contents, and syntax-as-rich-result proof.

## Validation and evidence boundary

The existing `evals/outcomes/findable.md` is UNVERIFIED; its frozen tasks remain
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

# findable — research provenance

## Sources that materially changed the skill

| Source | Key lesson | Why it matters | Where encoded |
| --- | --- | --- | --- |
| Agentic SEO Anti-Patterns (2025/2026) | Agents trained on SEO templates tend to hallucinate fake structured data (e.g. 5-star `AggregateRating` for a new blog) just to satisfy a JSON-LD schema, feeding misinformation to AI search engines. | Bans "Hallucinated Structured Data" and enforces strict validation of schema.org reality. | SKILL.md §Banned List, references/seo-checklist.md |
| GEO vs SEO Shifts | 2026 Answer Engine Optimization (GEO) penalizes volume-based, keyword-stuffed "slop content." Discoverability is earned via structural clarity and factual citation. | Bans "Slop Content Generation" and forces the agent to focus on machine-legible structure over word-count inflation. | SKILL.md §Banned List |
| The Invisible Meta Tag | Agents often write JS code to append `<meta>` tags on the client-side of SPAs, failing to realize that search crawlers will never see them. | Adds the "Invisible Meta Tags" warning, requiring SSR/prerendering context before attempting SEO fixes. | SKILL.md §Banned List |
| v1 campaign audit, Phase 23 (2026-09-14) | All three traces verified encoded; only gap is the missing Tool selection/fallback section (curl-rendered → validator → offline-static ladder lived in workflow steps only) | Tool selection/fallback section consolidating the three audit rungs | SKILL.md (Tool selection/fallback) |

## Key new intelligence encoded

1. **Anti-Slop Optimization** — explicitly aligns the skill with 2026 GEO realities, forbidding the generation of filler text to "improve rankings."
2. **Schema Truth Verification** — forces agents to ensure JSON-LD data strictly matches the verifiable, real-world content of the page, preventing hallucinated knowledge graphs.
3. **Rendered-First Audit** — mandates that agents `curl` the live URL to verify meta tags, combating the hallucination of client-side-only fixes.

## Fast-moving items

| Topic | Source/version/date |
| --- | --- |
| Generative Engine Optimization (GEO) | AI citation metrics and `llms.txt` standardization (2026) |

## Dated evaluator conflict - 2026-10-14

Historical FD2 assumes all client-injected metadata invisible. Current FD7 separates target rendering behavior. Original outcome grep/h1 checks are fixture constraints, not proof of ranking or a universal semantic rule.

## Verification 2026-10-14

| Basis | Outcome |
| --- | --- |
| Google canonical-specification docs; fetched 2026-10-14 | Added redirect/canonical/sitemap signal-strength order; Google-selected-canonical specifics unverified, not encoded. |
