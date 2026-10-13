# harden - current failure-first research pass

Reviewed 2026-10-14 against commit 66668739d4e3b99aab30bdea9594ca6361072c84.

Ownership: security trust boundaries, tenancy, agent/tool abuse; backend implements domain contracts.

Observed baseline instruction defect: 2021 category IDs mislabeled 2025; prompt injection equated with RCE; raw secret history diff encouraged; dev-only interpreted as safe.

Changed judgment: Correct versioned OWASP mapping, include supply chain/exception handling; redact history output; tenant denial requires no side effect and downstream model-independent policy.

## Source-to-decision trace

| Source | Organization / version / date | Access | Proposition and exact artifact | Rejected alternative / limit | Refresh |
| --- | --- | --- | --- | --- | --- |
| [Top 10:2025](https://top10.owasp.org/2025/) | OWASP; 2025 edition; 2025 | fetched 2026-10-14 | The published category IDs differ from the older list. Decision encoded in `skills/harden/references/attack-surface.md` (taxonomy, tenant, agent and CI boundaries). | No general guarantee or behavioral lift inferred. | source revision, target version, or affected boundary changes |
| [API1 Broken Object Level Authorization](https://api-security.owasp.org/editions/2023/en/0xa1-broken-object-level-authorization/) | OWASP; API Security Top 10 2023; 2023 | fetched 2026-10-14 | Object authorization must hold at each reachable operation. Decision encoded in `skills/harden/references/attack-surface.md` (taxonomy, tenant, agent and CI boundaries). | No general guarantee or behavioral lift inferred. | source revision, target version, or affected boundary changes |
| [LLM01 Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) | OWASP GenAI; LLM01:2025; 2025 | fetched 2026-10-14 | Injected external instructions can cross model/tool boundaries; impact depends on capabilities. Decision encoded in `skills/harden/references/attack-surface.md` (taxonomy, tenant, agent and CI boundaries). | No general guarantee or behavioral lift inferred. | source revision, target version, or affected boundary changes |
| [Secure use reference](https://docs.github.com/en/actions/reference/security/secure-use) | GitHub; current Actions documentation; living; date not established | fetched 2026-10-14 | Privileged workflows executing untrusted PR content can expose credentials. Decision encoded in `skills/harden/references/attack-surface.md` (taxonomy, tenant, agent and CI boundaries). | No general guarantee or behavioral lift inferred. | source revision, target version, or affected boundary changes |

Each source was opened individually through web access. Dates not shown by a
source are explicitly unknown; retrieval date is not publication date. The
self-contained package retains full source records in its research reference.

## Failure situation register

O = observed instruction defect in this checkout; R = locally reproducible
seeded fixture; S = mechanism described by named primary source; H = original
local evaluation hypothesis, not a reported incident or measured prevalence.
Unmarked rows below are H. These are distinct candidate situations, not fifteen
observed incidents. Replication and agent trials are recorded separately.

1. Old OWASP IDs shipped under 2025 header [O: attack-surface].
2. Prompt injection universally called RCE [O: attack-surface].
3. Raw history diff can reproduce secrets [O: attack-surface].
4. SQL interpolation leaks other owner notes [R: harden-notes].
5. Delete path ignores username [R: harden-notes].
6. List enforces tenant while export does not.
7. Cache key omits tenant.
8. 403 emitted after unauthorized write.
9. Queue worker loses authenticated subject.
10. Dev dependency executes in secret-bearing CI.
11. Webhook valid signature permits replay.
12. Uploaded filename becomes shell argument.
13. SSRF redirect crosses destination boundary.
14. Malformed error path fails open.
15. Injected document asks tool to export another tenant.

Rejected remembered category IDs under a new edition, scanner-only severity, dev-only-as-safe, and prompt-only tenant controls.

## Validation and evidence boundary

The existing `evals/outcomes/harden.md` is UNVERIFIED; its frozen tasks remain
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

# harden — research provenance

## Sources that materially changed the skill

| Source | Key lesson | Why it matters | Where encoded |
| --- | --- | --- | --- |
| OWASP GenAI Top 10 (2025/2026) | Prompt injection is no longer a chatbot curiosity; it is a systemic vulnerability akin to RCE, especially via Indirect Prompt Injection (IPI) from external documents. | Elevates "Indirect Prompt Injection" to A03 (Injection) and treats external data processed by agents as untrusted. | references/attack-surface.md |
| Excessive Agency Risks | Granting agents standing write-access without human-in-the-loop gates is a critical architectural failure. | Adds "Excessive Agency" to the A04 (Insecure Design) checklist. | references/attack-surface.md |
| Anti-CVSS Theater | Security audits that spam 50 generic CVEs from package scanners ignore contextual exploitability and cause alert fatigue. | Bans "CVSS Theater", requiring findings to be prioritized by actual reachability and impact rather than generic scores. | SKILL.md §Finding format |
| v1 campaign audit, Phase 19 (2026-09-14) | All three traces verified encoded; gaps are the missing Prerequisites and Tool selection/fallback sections (authorization assumed-but-unstated, scanner→adversarial→static ladder scattered) | Prerequisites (code + runnable path + authorization line) and Tool selection/fallback sections | SKILL.md (Prerequisites, Tool selection/fallback) |

## Key new intelligence encoded

1. **OWASP GenAI Top 10 Integration** — explicitly adds modern agentic attack vectors (Indirect Prompt Injection, Excessive Agency) to the core threat model.
2. **Anti-CVSS Theater** — forces the agent to differentiate between a theoretical CVE in a dev-dependency and an actually exploitable runtime vulnerability.
3. **Agentic Blast Radius** — expands threat modeling to include the damage an autonomous agent could cause if its context window is poisoned.

## Fast-moving items

| Topic | Source/version/date |
| --- | --- |
| LLM Vulnerability frameworks | OWASP Top 10 for Agentic Applications (2026) |

## Verification 2026-10-14

| Basis | Outcome |
| --- | --- |
| tukaani.org XZ backdoor notes (L. Collin); fetched 2026-10-14 | Added artifact-vs-tagged-source provenance to supply-chain review; scanner timelines unverified, not encoded. |
