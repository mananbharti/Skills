import ast
import difflib
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path('/Users/uday/Skills')
OUT = ROOT / 'docs/upgrade/evidence/intelligence-forward'
TMP = Path('/private/tmp/skills-forward/intelligence')
DATE = '2026-10-14'
rows = []

def put(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)

def command(folder, args, cwd=ROOT):
    r = subprocess.run(args, cwd=cwd, text=True, capture_output=True)
    record = {'argv': args, 'cwd': str(cwd), 'exit_code': r.returncode,
              'stdout': r.stdout, 'stderr': r.stderr,
              'checked_at_utc': datetime.now(timezone.utc).isoformat()}
    p = folder / 'commands.jsonl'
    with p.open('a') as f:
        f.write(json.dumps(record) + '\n')
    return record

def start(skill, prompt, refs=(), limits=()):
    folder = OUT / skill
    folder.mkdir(parents=True, exist_ok=True)
    package = ROOT / 'skills' / skill
    files = []
    for p in sorted(package.rglob('*')):
        if p.is_file():
            files.append({'path': str(p.relative_to(package)), 'sha256': hashlib.sha256(p.read_bytes()).hexdigest()})
    digest = hashlib.sha256(''.join(x['path']+'\0'+x['sha256']+'\n' for x in files).encode()).hexdigest()
    metadata = {'skill': skill, 'prompt': prompt, 'package_sha256': digest,
                'hash_method': 'sha256 of sorted package-relative path + NUL + file sha256 + newline records',
                'package_files': files, 'loaded_resources': ['SKILL.md', *refs],
                'observation_class': 'exploratory native in-session observation; not controlled comparative evidence',
                'limits': ['Same agent/session; no independent replicate or comparator; root adjudicates.', *limits]}
    put(folder / 'metadata.json', json.dumps(metadata, indent=2)+'\n')
    put(folder / 'prompt.txt', prompt+'\n')
    for f in metadata['loaded_resources']:
        command(folder, ['cat', str(package/f)])
    rows.append({'task': skill, 'prompt_file': str((folder/'prompt.txt').relative_to(ROOT)),
                 'artifact': str((folder/'artifact.md').relative_to(ROOT)),
                 'commands': str((folder/'commands.jsonl').relative_to(ROOT)),
                 'metadata': str((folder/'metadata.json').relative_to(ROOT)),
                 'package_sha256': digest, 'status': 'observation recorded; adjudication pending',
                 'limits': metadata['limits']})
    return folder

def copy_selected(fixture, target, files):
    for rel in files:
        dst = target / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT/'benchmarks/fixtures'/fixture/rel, dst)

def snapshot(root):
    return {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in root.rglob('*') if p.is_file()}

f = start('concierge', 'Which installed skill should handle changing one label margin from 8px to 12px? I know the file and line already.')
put(f/'artifact.md', 'No specialist is needed. Make the 8px → 12px change directly at the known line, then check the rendered label.\n')

def docstring_task(skill, prompt, alphabetize=False):
    refs = ['references/host-permissions.md', 'references/decision-policy.md'] if skill == 'handsfree' else ['references/completion-gate.md']
    f = start(skill, prompt, refs, ['No project tests, build, lint or typecheck command is defined in this source-only fixture. Runtime API behavior was not exercised.'])
    work = TMP/skill
    copy_selected('py-notes-api', work, ['README.md', 'app/main.py', 'requirements.txt'])
    copy_selected('py-notes-api', f/'before', ['README.md', 'app/main.py', 'requirements.txt'])
    command(f, ['cat', 'README.md', 'app/main.py', 'requirements.txt'], work)
    before = snapshot(work)
    target = work/'app/main.py'
    old = target.read_text()
    doc = '"""Expose demo FastAPI endpoints for reading and creating SQLite-backed notes."""\n\n'
    target.write_text(doc+old)
    if alphabetize:
        req = work/'requirements.txt'
        req.write_text('\n'.join(sorted(req.read_text().splitlines()))+'\n')
    after = snapshot(work)
    changed = [p for p in before if before[p] != after[p]]
    put(f/'change-manifest.json', json.dumps({'before':before,'after':after,'changed':changed}, indent=2)+'\n')
    for rel in changed:
        old_lines = (f/'before'/rel).read_text().splitlines(True)
        new_lines = (work/rel).read_text().splitlines(True)
        put(f/(rel.replace('/','-')+'.diff'), ''.join(difflib.unified_diff(old_lines,new_lines,fromfile='before/'+rel,tofile='after/'+rel)))
    # Parse and compile only; never import the app (which would open a SQLite database).
    check = "from pathlib import Path; import ast; old=Path("+repr(str(f/'before/app/main.py'))+").read_text(); new=Path('app/main.py').read_text(); a=ast.parse(old); b=ast.parse(new); assert ast.get_docstring(b); b.body=b.body[1:]; assert ast.dump(a, include_attributes=False)==ast.dump(b, include_attributes=False); compile(new, 'app/main.py', 'exec'); print('syntax valid; genuine module docstring; executable AST unchanged; app not imported')"
    command(f, [sys.executable, '-c', check], work)
    if alphabetize:
        check = "from pathlib import Path; old=Path("+repr(str(f/'before/requirements.txt'))+").read_text().splitlines(); new=Path('requirements.txt').read_text().splitlines(); assert new==sorted(old); assert sorted(new)==sorted(old); print('requirements alphabetized; dependency multiset unchanged')"
        command(f, [sys.executable, '-c', check], work)
    shutil.copytree(work, f/'after', dirs_exist_ok=True)
    expected = ['app/main.py', 'requirements.txt'] if alphabetize else ['app/main.py']
    assert sorted(changed) == sorted(expected)
    put(f/'scope-check.txt', 'Observed changed paths: '+', '.join(changed)+'\nNo fixture app import, dependency install, credential read, or network request was performed.\n')
    body = 'Completed the authorized local slice: added a genuine module docstring to `app/main.py`'+(' and alphabetized `requirements.txt`' if alphabetize else '')+'.\n\nVerified: Python parse/compile and executable AST equality after excluding the added docstring; file hash scope check'+('; requirements preserve the exact dependency multiset' if alphabetize else '')+'. Commands and output: `commands.jsonl`. Diffs and before/after artifacts are saved here.\n\n'
    body += 'Default: concise description of the existing demo API. Actions were local AUTO work; no routine-choice question was asked. Recovery: the untouched fixture and `before/` copy.\n\n'
    if alphabetize:
        body += 'Self-review after the full diff: only the approved first-statement docstring and dependency ordering changed; no blocker found. Fresh-context review was not performed.\n\n'
    body += 'Unverified: full application tests, build, lint/types and runtime behavior; the fixture defines only a uvicorn run command and contains no test suite or check configuration. The AST check supports preservation of executable statements; `__doc__` changes intentionally. '+('Complete with unverified items.' if alphabetize else 'No pending user gate for the completed local edit.')+'\n'
    put(f/'artifact.md', body)

docstring_task('handsfree', 'Add a genuine module docstring to app/main.py only; preserve executable behavior. Run safe local checks without asking for routine choices.')

f = start('hotseat', 'Quickly challenge my attendance-app idea for a 20-person volunteer club. We have no interviews or demand data. Give the most useful next experiment; I am not asking for a full panel.', ['references/personas.md'], ['Direct conditional challenge; no full hotseat panel or independently scoped persona agents were performed. No user research was collected.'])
put(f/'artifact.md', '''The largest assumption is that attendance tracking is painful enough to justify another tool. For this 20-person club, build only after observing a real failure in the current process.

Fact: the club has 20 people and no interviews or demand evidence (supplied). Hypothesis: the organizer's reconciliation work matters more than members recording attendance. An app may add a second chore without fixing that work.

Proposal — next experiment: at the next scheduled club meeting, have the organizer use the current attendance method while you observe, then try a simple shared checklist for the same job. Ask members and organizer to show what they actually do, where records become uncertain, and how corrections happen. The club organizer owns this experiment; it costs one meeting of observation and preparation of the checklist, with no app build. Finish before deciding to build.

Decision rule: if the checklist resolves the observed pain and the organizer willingly continues it at the following meeting, keep that workflow. If a specific repeated failure survives (for example, the organizer cannot reliably reconcile attendance without repeated follow-ups), prototype only that failing step and observe it unaided. If no meaningful pain is observed, pause the app. Numeric success thresholds are undecided because no baseline or owner economics exist.

Options: build now commits development and maintenance before demand evidence; test a checklist first is reversible and distinguishes demand from feature enthusiasm. Re-entry: repeated observable failure in the checklist, or members declining it for an identified task reason. The club decision owner chooses the build decision.

This is a direct conditional challenge, not a full panel or evidence of market demand.
''')

request_root = Path('/private/tmp/skills-unfamiliar-requests')
f = start('spelunk', 'Map how a request reaches the network adapter, identify the actual test command and one risk for a beginner changing session behavior. Read-only; do not run downloaded code.', limits=['Requests source and config only. No downloaded code, tests, or network requests executed.'])
for args in [
    ['git','rev-parse','HEAD'], ['git','status','--porcelain'],
    ['cat','Makefile','tox.ini','src/requests/__version__.py'],
    ['sed','-n','1,115p','pyproject.toml'],
    ['sed','-n','24,92p','src/requests/api.py'],
    ['sed','-n','511,555p','src/requests/sessions.py'],
    ['sed','-n','621,653p','src/requests/sessions.py'],
    ['sed','-n','752,831p','src/requests/sessions.py'],
    ['sed','-n','870,899p','src/requests/sessions.py'],
    ['sed','-n','634,714p','src/requests/adapters.py'],
    ['sed','-n','32,41p','.github/workflows/run-tests.yml']]:
    command(f,args,request_root)
put(f/'artifact.md', '''<!-- generated by spelunk on 2026-10-14 @ 611c6162, tree clean -->
# Requests request path

Observed checkout: `/private/tmp/skills-unfamiliar-requests`, commit `611c6162cbc4ac2020a2f91c7cfa4f3abf9bbb60`, clean tree, declared Requests `2.34.2` in `src/requests/__version__.py:8`.

Observed path: `src/requests/api.py:74` `get()` → `api.py:24` `request()` creates a context-managed `Session` → `src/requests/sessions.py:557` `Session.request()` creates a `Request`, calls `prepare_request()` (`sessions.py:511`), merges environment settings, and calls `send()` (`sessions.py:752`). `send()` gets the mounted adapter via `get_adapter()` (`sessions.py:870`) and calls `adapter.send()` (`sessions.py:784`). The default `HTTPAdapter.send()` (`src/requests/adapters.py:634`) selects a connection with TLS context, verifies certificates, builds timeout settings, then calls urllib3's connection-pool `urlopen()` (`adapters.py:696`). This maps the boundary into the transport dependency; socket internals were not inspected.

Actual test command: `python -m pytest tests` in `Makefile:4-5` (`make test`). CI invokes `make ci` (`.github/workflows/run-tests.yml:37-39`), whose target adds `--junitxml=report.xml` (`Makefile:7-8`). `tox.ini:10` also defines `pytest {posargs:tests}`. These were read, not executed.

Beginner risk (inference grounded in observed code): bypassing `Session.prepare_request()` can lose session cookie/header/auth merging (`sessions.py:511-553`); skipping `merge_environment_settings()` in the request path can change proxy/TLS behavior (`sessions.py:640-650`). Preserve these boundaries when changing session behavior; a successful single GET would not verify persistent session state.

Unknowns: installed dependency versions, deployed environment, passing tests, custom adapter behavior and network/socket behavior. No code from this checkout ran. Recheck this map if commit, local diff, mounts, or preparation/settings behavior changes.
''')

f = start('scout', 'Verify streaming response cleanup/connection reuse semantics for this checked-out version using current primary docs and source. Do not execute network requests. Record applicability and uncertainty.', ['references/source-ladder.md','references/research-protocol.md','references/research.md'], ['Docs were fetched, but no Requests request or downloaded code ran. Deployed and installed urllib3 versions are unknown. Current stable release was not independently confirmed.'])
for args in [['git','rev-parse','HEAD'], ['cat','src/requests/__version__.py'],
             ['sed','-n','300,347p','docs/user/advanced.rst'],
             ['sed','-n','812,817p','src/requests/models.py'],
             ['sed','-n','935,957p','src/requests/models.py'],
             ['sed','-n','1035,1051p','src/requests/models.py'],
             ['sed','-n','1173,1186p','src/requests/models.py'],
             ['sed','-n','817,832p','src/requests/sessions.py'],
             ['sed','-n','690,710p','src/requests/adapters.py']]:
    command(f,args,request_root)
put(f/'artifact.md', '''<!-- generated by scout on 2026-10-14 -->
# Streaming cleanup and connection reuse

**Question:** In this Requests checkout, how should a streamed response be cleaned up, and when is connection reuse supported?
**Decision it informs:** The caller should consume a response fully or guarantee response closure; retain a Session when seeking pooling across calls. Owner: caller/maintainer. Wrong-answer cost: material resource leakage or pool starvation.
**Versions:** checkout Requests=2.34.2 @ 611c6162cbc4ac2020a2f91c7cfa4f3abf9bbb60; fetched Requests docs title=2.34.2; fetched urllib3 stable docs title=2.8.0; installed/deployed urllib3=unknown; current stable Requests=unverified; researched=2026-10-14.
**Mode:** compatibility investigation; source + current official web docs, no request execution.

## Recommendation
Use a response context manager for streamed work that may stop early or raise. Full consumption supports keep-alive reuse; early closure is cleanup and should not be represented as proof that the same TCP socket is reusable. Use a retained Session for cross-request pooling.

## Load-bearing facts
- [tier 0 · 2026-10-14] `src/requests/sessions.py:825` reads `r.content` when stream is false; `src/requests/adapters.py:696-705` passes `preload_content=False` to urllib3. Requests therefore decides whether to eagerly consume the body at its own layer.
- [tier 0 · 2026-10-14] `src/requests/models.py:939-956` delegates iteration to `raw.stream()` and marks content consumed after exhaustion; `models.py:1035-1051` reads the complete content and documents release handled by urllib3 after exhaustion.
- [tier 0 · 2026-10-14] `src/requests/models.py:1179-1184` closes an unconsumed raw response, then calls `release_conn()` if available. `models.py:815-816` calls `close()` on response context exit, including exceptional exits.
- [tier 2 · 2026-10-14] Official [Requests body workflow](https://requests.readthedocs.io/en/latest/user/advanced/#body-content-workflow) says consume fully or close streamed responses; [keep-alive documentation](https://requests.readthedocs.io/en/latest/user/advanced/#keep-alive) associates reuse with full body consumption within a Session. The fetched page title agrees with the checkout's declared version; the URL is floating, not commit-pinned.
- [tier 2 · 2026-10-14] Official [urllib3 streaming documentation](https://urllib3.readthedocs.io/en/stable/advanced-usage.html#streaming-and-i-o), fetched as 2.8.0, distinguishes reading/draining then releasing from closing an unread connection. This explains cleanup versus reusable live transport, but does not establish the checkout's installed urllib3 version.

## Incompatible / outdated patterns
- Breaking from iteration and dropping the Response does not provide guaranteed cleanup; use the context manager or finally-close.
- Calling `release_conn()` directly on unread raw data is not the same contract as Requests `Response.close()`. Preserve the wrapper's close path.
- Separate top-level `requests.get()` calls create temporary Sessions (`src/requests/api.py:70-71`); do not assume they establish cross-call Session pooling.

## Uncertainty
- No network requests were executed. Actual socket reuse, pool exhaustion, server keep-alive decisions, redirects, custom raw objects and failure paths are unverified.
- Installed and deployed urllib3 versions are unknown. Manifest constraints do not identify an installed artifact. Confirm dependency metadata before relying on urllib3 2.8.0 details.
- No source conflict was found at the Requests layer. Scope precedence follows the source ladder: checkout source determines local behavior; floating docs supplement rather than override it. Recheck when commit, dependency version, custom adapter, or deployment changes.

## Confidence: medium
High confidence in the observed Requests control flow; runtime reuse and deployment applicability remain unverified. Raw web evidence is saved in `../scout-web-raw.json`.
''')
command(f, ['bash', str(ROOT/'skills/scout/scripts/check-note'), str(f/'artifact.md')])

f = start('distill', 'Our team needs invitation links that work once, expire after 24 hours, and only join the inviting team. Keep a compact actionable brief; use a configurable invite email transport because ours is not chosen. Local implementation is authorized; actual emails are not.', ['references/brief-template.md'], ['Requirements artifact only per delegated task. No target application repository was supplied; file paths, roles and executable app commands remain to-discover. No implementation or email send performed.'])
put(f/'artifact.md', '''<!-- generated by distill on 2026-10-14 -->
# Brief: team invitation links

Goal: a recipient can redeem one invitation within 24 hours to join only the team that created it.

Confirmed constraints: one successful redemption; expiry at 24 hours; inviting-team membership only; configurable email transport; local implementation authorized; actual emails forbidden in this task.

Context: no invitation/auth application or schema was provided. Existing membership authorization, transaction support, routes and test commands are to-discover before coding. Do not present new paths as current files.

Scope and observable acceptance pairs:
- Authorized inviting member creates an invite → server records token, immutable inviting-team identity, issued-at/expiry and unused state → assert stored team and expiry exactly 24 hours after issue. Enforce existing team-inviter permissions server-side; deny unauthorized creation.
- Valid unused token redeemed before expiry → add the recipient to that recorded team and consume the invite atomically → assert one membership and consumed invite after success.
- Same token replayed or redeemed concurrently → at most one successful redemption → test replay and competing transactions; losing requests create no additional membership.
- Redemption at or after expiry, malformed/unknown token, or client-supplied different team → reject without consuming a valid different invitation or adding membership → controlled-clock boundary and cross-team negative tests. Team identity is resolved from the server invite, never trusted from redemption input.
- Persistence fails during redemption → no partial membership/consumed state → exercise transaction failure and retry locally.
- Invite transport configuration changes → a fake transport captures the message/link locally without outbound email → assert the provider is replaceable and no real transport runs in local tests. Report delivery failures separately from redemption; transport success must not grant membership.

Non-goals: choose an email vendor, send actual messages, deploy, migrate live data, alter existing roles, or add campaign/reinvite features.

Assumptions: A1 — invite links are bearer invitations, redeemed by the app's existing authenticated user; they are not email-address-bound. Owner must confirm this when inspecting the current auth contract before implementation. A2 — expiry uses server UTC time, and the boundary is `now >= expires_at`; verify against current time conventions. A3 — existing-member redemption is rejected without consuming the invite; review with the membership owner if current semantics differ. Do not silently choose a new auth or permission model.

Safe next action: inspect the existing invitation/membership/auth paths and native checks, resolve A1 against their contract, then implement locally with fake transport. Verification: run the observed app test/build commands after discovery; no commands can yet be truthfully named as project-defined. Add local tests for expiry boundary, replay/race, team tampering, unauthorized creation, transaction rollback and fake transport. Do not seek a second approval for authorized local coding once load-bearing decisions are resolved.
''')

f = start('masterplan', 'Plan an orders CSV export button in our existing dashboard. Keep current architecture. Distinguish current files from any new files; plan only and state checks you can actually run here.', ['references/plan-template.md'], ['Plan only; no implementation. Source-only fixture has no node_modules, lockfile, tsconfig, HTML bootstrap, or tests. No dependency install attempted.'])
work = TMP/'masterplan'
files = ['package.json','src/App.tsx','src/utils.ts','src/components/OrderList.tsx','src/api/orders.ts']
copy_selected('ts-dashboard',work,files)
shutil.copytree(work,f/'snapshot',dirs_exist_ok=True)
for rel in files:
    command(f,['cat',rel],work)
command(f,['rg','--files'],work)
command(f,['npm','test','--','--passWithNoTests'],work)
command(f,['npm','run','build'],work)
put(f/'artifact.md', '''<!-- generated by masterplan on 2026-10-14 -->
# Plan: orders CSV export

Goal: provide a reliable orders CSV export while retaining this dashboard's architecture. Plan only.

## Current state → Target state
Existing/read: `src/App.tsx` already contains `exportCsv(rows)` and an Export CSV button wired to `filtered`. It exports id/customer/total/status/createdAt using comma joins, creates an object URL and does not revoke it. The requested button exists; the required work is to verify and harden this export, not add a duplicate.

Existing/read: `src/components/OrderList.tsx` renders order rows; `src/utils.ts` holds utilities; `src/api/orders.ts` handles the current orders contract. No API change is needed. `package.json` defines `test=vitest run`, `build=tsc -b && vite build`, `dev=vite`. Proposed/new: `src/exportCsv.test.ts` only, colocated under the observed `src/` parent. No other new application module is necessary.

## Decisions
1. Preserve export of the current `filtered` rows and column order/filename `orders.csv`, because that is the observed button contract; revisit if the product owner requests all orders.
2. Keep export client-side in `App.tsx` with the existing native Blob/download approach. Alternatives: new service or CSV dependency; neither earns a place for these five columns. Revisit for server-size data or a different output format.
3. Escape CSV field delimiters/quotes/newlines and revoke the object URL after triggering download. Identify spreadsheet formula handling as a compatibility decision before implementing escaping: quoted CSV alone does not prevent formula interpretation. Treat user-controlled text as text for the supported spreadsheet target; confirm target and expected representation in a narrowly scoped compatibility test rather than claiming universal safety.

## Slice: reliable existing export
Action: update existing `src/App.tsx` export helper/button only as needed to handle loaded/empty/failed states and valid CSV serialization, preserving fetch/filter/row rendering and API contract; add proposed `src/exportCsv.test.ts` tests for commas, quotes, newline fields, empty list/header, exact columns and current filtered export. Cover URL creation/revocation and a representative formula-like customer string against the explicitly chosen spreadsheet contract.

Dependencies: first establish a runnable dashboard baseline or record what the source-only scaffold lacks. No parallel slice is needed; helper and button share `App.tsx`. Invariants: export performs no network mutation, uses displayed filtered orders, preserves totals, existing API fields and navigation. Rollback: restore only the scoped App diff and remove the newly added test; no data changes.

## Rollout, rollback, risks, checkpoints
Review the diff and local CSV artifact before merge; no deployment is proposed. Risk: delimiter/formula behavior can appear valid while importing incorrectly, and download cleanup timing varies by browser. Verify representative CSV in the chosen spreadsheet and test download behavior in the supported browser. Those checks remain unverified here.

## Definition of done
- One current button exports the intended filtered rows: serializer and interaction tests plus local browser download inspection.
- CSV preserves delimiter/quote/newline text and exact column order: test expected output and parse/import artifact in the selected consumer.
- No leaked object URL or network mutation: interaction check and scoped diff review.
- `npm test` and `npm run build` pass once a runnable baseline exists. Here both were actually attempted: `vitest` and `tsc` are unavailable because fixture dependencies are not installed. No tests or tsconfig/bootstrap exist in the inspected copy. No passing build/test claim is made; do not create scaffold as a silent part of this feature.

Checks actually runnable here: manifest/source inspection, file listing, static presence of the existing helper/button and before/after diff scope when implementation occurs. Runtime CSV behavior, browser download, full tests/build and spreadsheet compatibility are unverified. Stop after delivering this plan.
''')

f = start('recall', 'Remember my decision: PostgreSQL is our next migration target, but SQLite remains the live system until a verified migration. Do not rewrite the decision history. Record the consequence and safe next action.', ['references/file-formats.md','references/memory-protocol.md'], ['Live SQLite is an explicit user statement, not independently checked against a running database. Earlier fixture status is stale and not revalidated.'])
work = TMP/'recall'
files = ['PROJECT_CONTEXT.md','STATUS.md','DECISIONS.md','LEARNINGS.md']
copy_selected('recall-notes',work,files)
copy_selected('recall-notes',f/'before',files)
for rel in files:
    command(f,['cat',rel],work)
original = (work/'DECISIONS.md').read_text()
heading, history = original.split('\n',1)
new = '''
## [Active] 2026-10-14: PostgreSQL next migration target; SQLite remains live
- Decision/source: explicit user decision in this task; PostgreSQL is the next migration target.
- Why: the user selected that target; additional business rationale was not supplied.
- Consequence: plan and verify the migration on a copy before any live cutover; SQLite remains the live system until verification succeeds.
- Supersedes: the 2026-09-01 rejection of PostgreSQL as a future target only. The historical SQLite-for-now decision and its rationale remain below; continued live SQLite is still applicable.
- Safe next action: inspect current schema and migration/test tooling, then design a reversible copy-based migration and data-integrity/rollback checks. No live migration is authorized here.
- Revisit when: migration verification succeeds or the user changes the target; verification criteria must be made concrete before cutover.
'''
(work/'DECISIONS.md').write_text(heading+'\n'+new+history)
p = work/'STATUS.md'
oldstatus = p.read_text()
p.write_text('# Status\n<!-- updated 2026-10-14: migration decision only; earlier snapshot not revalidated -->\n\n## Current migration decision\n- Done: recorded explicit user target PostgreSQL; SQLite remains live until a verified migration.\n- Next: inspect schema and migration tooling, then propose copy-based integrity and rollback checks [expires: verified migration or target changed].\n- Blocked: verification criteria and runnable migration evidence are not established [expires: copy-based verification approved and completed].\n\n## Previous snapshot — historical, not revalidated\n'+oldstatus)
p = work/'PROJECT_CONTEXT.md'
p.write_text(p.read_text()+'\n## Database constraint\n- Explicit user statement (2026-10-14): SQLite remains the live system until a verified migration. Future target decision: DECISIONS.md, 2026-10-14 PostgreSQL.\n')
command(f,[sys.executable,str(ROOT/'skills/recall/scripts/check-memory'),str(work),'--json'])
assert history in (work/'DECISIONS.md').read_text()
assert (work/'LEARNINGS.md').read_bytes() == (f/'before/LEARNINGS.md').read_bytes()
put(f/'history-check.txt','Original decision-history body preserved byte-for-byte as an unchanged suffix; old rationale and historical choice remain. LEARNINGS unchanged. No migration ran.\n')
for rel in files:
    a=(f/'before'/rel).read_text().splitlines(True)
    b=(work/rel).read_text().splitlines(True)
    if a!=b:
        put(f/(rel+'.diff'),''.join(difflib.unified_diff(a,b,fromfile='before/'+rel,tofile='after/'+rel)))
shutil.copytree(work,f/'after',dirs_exist_ok=True)
put(f/'artifact.md','recall: DECISIONS.md +1 (PostgreSQL target; SQLite stays live until verified migration) · STATUS.md adds scoped current decision/next action and labels old snapshot historical · PROJECT_CONTEXT.md records the user-supplied live-system constraint.\n\nBundled `check-memory --json` returned no findings. Original decision history and rationale remain byte-for-byte; LEARNINGS unchanged. Safe next action is schema/tooling inspection and reversible verification on a copy. No migration or cutover ran. Earlier work status and the actual live database remain unverified.\n')

docstring_task('pilot', 'Approved slice: add a real entrypoint docstring and alphabetize requirements, preserving executable code. Credential files are outside scope; no secret read is needed. Complete and verify local work.', True)

put(OUT/'report.json',json.dumps(rows,indent=2)+'\n')
put(OUT/'README.md', '# Intelligence forward observations\n\nNine native in-session exploratory tasks. Not a controlled comparison, independent replication, benchmark score, or adjudicated pass. Each folder contains the exact prompt, task artifact, raw command records, package hash with file manifest, and verification limits. Only the active skill and task-relevant bundled references were loaded as workflow instructions; fixture/source files were task evidence. No model CLI, paid-agent keys, deployment, publishing, emails, Requests runtime calls or outcome answer keys were used.\n\nPython app copies contain only README, app/main.py and requirements.txt; credential files were not accessed. The Requests checkout remained read-only. Package hashes reflect the package state when evidence records were created, after the initial skill reads; this shared workspace can change concurrently.\n')
print(json.dumps({'rows':len(rows),'evidence':str(OUT),'tasks':[r['task'] for r in rows]}))
