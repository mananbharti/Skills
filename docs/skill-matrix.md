# Skill ownership matrix

This is an ownership contract for the frozen 28 skills. It makes no untested
stack, platform or outcome claim. `P` is primary ownership, `C` is optional
collaboration; a handoff needs an actual missing capability. The full dense
matrix is available as [CSV](upgrade/capability-matrix.csv) and
[JSON](upgrade/capability-matrix.json).

| Skill | Primary responsibility | Optional collaboration | Conditional / unsupported path |
| --- | --- | --- | --- |
| `concierge` | routing | onboarding | No routing step for an already clear owner or trivial task. |
| `handsfree` | autonomy | implementation | Only authorized scope; host permissions and paid-service gates still apply. |
| `hotseat` | ideation | specification | Challenge choices; no invented consensus, research or validation. |
| `spelunk` | repository navigation, onboarding | architecture | Static inventory is not runtime behavior; generated and vendor code need distinct treatment. |
| `scout` | research freshness | security | Pin installed versions; unavailable sources leave factual gaps. |
| `distill` | specification | ideation | Short brief proportional to ambiguity; do not force a product interview. |
| `masterplan` | planning | migrations | Existing and proposed paths must be distinct; no fixed slice quota. |
| `recall` | durable memory | context cost | Fresh code and current human decisions outrank old notes; never persist credentials. |
| `pilot` | implementation | testing | Execute approved scope; denied secrets do not block safe unrelated work. |
| `backend` | backend, schemas, tenancy, payments, authentication, migrations, observability | security, privacy, games | Provider and datastore adapters need detected versions and local tests; no universal exactly-once promise. |
| `blueprint` | architecture | onboarding | Trace current vs proposed structure; static diagram checks are not rendering proof. |
| `headroom` | scalability | games, operations | User counts alone are not workload; recommendations need trigger metrics. |
| `polish` | frontend, design systems | accessibility | Preserve intent and tokens; native-device appearance needs device evidence. |
| `friction` | usability, accessibility, localization | frontend, privacy | Task walks are hypotheses without real users; legal conformance unverified. |
| `ditto` | reference matching | frontend | Authorized references; a screenshot cannot establish unseen interactions. |
| `proof` | testing | mobile, games | Choose project-native boundaries; a static artifact does not prove device/platform compatibility. |
| `roadtest` | browser verification | accessibility, mobile | Browser path primary; HTTP fallback cannot prove visual or native-device behavior. |
| `sleuth` | debugging, incidents | observability | A workaround is provisional; production mutation and sensitive logs remain gated. |
| `referee` | review | security | Review actionable changed behavior; an independent reviewer is not a substitute for runtime checks. |
| `hotpath` | optimization | scalability, observability | Matched load and correctness gates; write-query profiling can have side effects. |
| `harden` | security, privacy | tenancy, authentication | Exploit preconditions and confidence required; no security or legal certification. |
| `unslop` | refactoring | implementation | Preserve behavior and compatibility bytes; never use cleanup as a reason for feature rewrite. |
| `janitor` | git | release | Protect dirty user state; external pushes and history rewriting require their actual authorization. |
| `frontpage` | documentation | onboarding | Quickstarts and claims require repository evidence, no invented users or badges. |
| `findable` | SEO | documentation | Initial HTML and rendered DOM differ; no ranking promises or fabricated structured data. |
| `frugal` | context cost | autonomy | Failures and retries enter cost per correct task; token telemetry may be unknown. |
| `cleared` | readiness | privacy, security, release | Relevant critical unknowns block; omit irrelevant checks for isolated changes. |
| `runway` | release, rollback, operations | migrations, incidents | Served build and target scope verified separately; app-store/device and provider adapters remain conditional. |

Payment/provider details live with `backend`, risk review with `harden`.
Privacy engineering follows the same boundary; jurisdiction-specific legal
advice is outside this bundle. Backend observability means instrumenting owned
services, while `sleuth` uses observations to diagnose and `runway` uses them
to assess deployment health. Mobile and game variants use existing owners
only where project-native tools supply real evidence. Native-device, live
Postgres, real-time deployment and app-store paths need separate trials;
listing an owner does not claim those trials have passed.
