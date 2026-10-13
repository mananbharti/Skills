Rung: static initial HTML/config. Public fixture intent inferred from task; no live host, server, HTTP request, browser, crawler or search-console observation. notesapp.example host taken from supplied sitemap, still a placeholder requiring deployment-owner confirmation. No publication/indexing submission executed.

| Before issue / source | Local fix | Evidence and limit |
| --- | --- | --- |
| index.html noindex/nofollow, robots Disallow:/ | Public source fixtures index/follow and Allow:/ | Static directives parsed; served proxy/CDN headers unknown. |
| Duplicate Home titles, missing descriptions/canonicals | Unique titles/descriptions; distinct absolute canonicals | check_static.py parsed both pages; hostname/redirect policy not live-verified. |
| Fake Product214-review5-star rating | Removed JSON-LD entirely | No rating claim in visible page or evidence; no replacement schema invented. |
| Home div headings, About two h1 | Header/main, primary h1, subordinate h2 | Semantic initial HTML check; no indexing penalty claim based on count. |
| Missing-page link and sitemap loc | Removed broken legacy link; sitemap home/about | File-local targets exist and XML parses; no HTTP200/canonical-served proof. |
| Social metadata absent | Factual og:title/description/type/url | Tags parsed; no og:image/Twitter card invented because no verified asset. Real preview rendering remains unknown. |

Static check passes: unique titles/descriptions, expected canonicals, local link existence, one primary heading per file, valid XML URLs, no blanket disallow, no fake aggregateRating. Before evidence retained in input/read logs. These fixes address authored metadata and crawl configuration only. Deployment must verify exact response status/redirect/canonical, robots header/meta, initial and rendered HTML and sitemap responses for actual public hostname. Private/staging policy must remain protected; do not copy public directives blindly. Social assets and search-engine discovery/crawl/index/ranking are unverified; no ranking or client rendering promise.
