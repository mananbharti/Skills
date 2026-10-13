from record import *
# Correct source line anchors against actual raw numbered sources (initial prose anchors were off).
updates={
'blueprint':{'App.tsx:30–59':'App.tsx:28–51,122','api/orders.ts:14–17':'api/orders.ts:14–18','App.tsx:59–81':'App.tsx:54–72','api/orders.ts:19–31':'api/orders.ts:20–31'},
'friction':{'index.html:23–24,32':'index.html:19–20,27','index.html:25':'index.html:21','index.html:26':'index.html:22','index.html:20–27':'index.html:17–23','index.html:30–39':'index.html:25–34'},
'roadtest':{'app.js:10':'app.js:9'}}
for slug, replacements in updates.items():
 p=EVID/slug/'artifact.md';s=p.read_text()
 for a,b in replacements.items():s=s.replace(a,b)
 p.write_text(s)
 if slug=='blueprint':
  (BASE/slug/'work/docs/architecture/README.md').write_text(s)
  (EVID/slug/'output/docs/architecture/README.md').write_text(s)
# Ditto original fixture remains raw input. Deliver only reconstruction, local assets and comparison source referencing input provenance.
p=EVID/'ditto/output/reference.html'
if p.exists():p.unlink()
# Fix structural delta report based on actual diff, no estimated line count.
p=EVID/'unslop/artifact.md';s=p.read_text();old=len((BASE/'unslop/original/shop.py').read_text().splitlines());new=len((BASE/'unslop/work/shop.py').read_text().splitlines());s=s.replace('Net shop.py line delta: -1.',f'Net shop.py line delta: {new-old} ({old} -> {new} lines).');p.write_text(s)
# Per-skill snapshot sources and task inputs are immutable in each owned input dir.
# Verify repository fixtures against the initial copied raw fixtures; inspect no other upgrade report.
checks={}
for slug,(fixture,prompt) in TASKS.items():
 e=EVID/slug
 assert (e/'report.json').is_file() and (e/'artifact.md').is_file()
 report_data=json.loads((e/'report.json').read_text())
 report_data['raw_prompt_scope']='prompt.txt carries the assigned task and safety boundary; scenario inputs only for plan-only cases.'
 report_data['source_skill_hashes']='input-hashes.json, active copied package snapshot'
 (e/'report.json').write_text(json.dumps(report_data,indent=2)+'\n')
 (e/'output-hashes.json').write_text(json.dumps(hashes(e/'output'),indent=2)+'\n')
 if fixture:checks[slug]={'repository_fixture_matches_copied_input':hashes(ROOT/'benchmarks/fixtures'/fixture)==hashes(e/'input')}
# preserve executable orchestration scripts as raw workflow evidence (no paid calls or network).
(EVID/'execution-sources').mkdir(exist_ok=True)
for p in BASE.glob('*.py'):shutil.copy(p,EVID/'execution-sources'/p.name)
(EVID/'preservation.json').write_text(json.dumps(checks,indent=2)+'\n')
(EVID/'commands.jsonl').touch()
for cmd in [['scripts/validate-skills'],['scripts/check-names'],['scripts/check-links']]:
 p=subprocess.run(cmd,cwd=ROOT,text=True,capture_output=True)
 rec={'argv':cmd,'cwd':str(ROOT),'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr}
 with (EVID/'commands.jsonl').open('a') as f:f.write(json.dumps(rec)+'\n')
 (EVID/(Path(cmd[0]).name+'.txt')).write_text('$ '+cmd[0]+'\nexit: '+str(p.returncode)+'\n'+p.stdout+p.stderr)
 print(json.dumps(rec))
rows=[]
for slug in TASKS:
 r=json.loads((EVID/slug/'report.json').read_text());rows.append({'skill':slug,'status':r['status'],'report':slug+'/report.json','artifact':slug+'/artifact.md','gaps':r['gaps']})
summary={'observation_type':'independent exploratory specialist forward tests; no control/baseline agent comparison, not generalized effectiveness proof','task_count':len(rows),'completed_artifact_records':len(rows),'reports':rows,'preservation':'preservation.json','validator_commands':'commands.jsonl','no_shared_repository_commits':True,'toy_git_baseline_commit':'janitor: authorized fixture baseline only; task staged not committed; no remote','browser_limit':'loopback server PermissionError and file URL policy denial; static fallback without retry/bypass','method_limits':['Same specialist performed all17 sequentially; task summaries persisted, not a blinded randomized trial.','Plan-only scenarios and source inspections are not dynamic behavior proof.','Hotpath synthetic list/string SKU scope; no production or general workload claim.','No paid keys, model CLIs, deployments, publication or live external service actions.'],'unavailable':['real browser flow evidence','actual provider usage comparison','real traffic/quota/cost evidence','live deployment/crawl verification']}
(EVID/'report.json').write_text(json.dumps(summary,indent=2)+'\n')
(EVID/'artifact.md').write_text('''Specialist forward observations completed for17 assigned tasks. Each directory contains prompt, report.json, artifact.md, command logs, input/output hashes and applicable raw fixtures/artifacts. This is exploratory forward testing, not controlled comparative proof or a skill-effectiveness benchmark.

Meaningful bounded outcomes: cart test-only change exposes actual assertion24.3 !=27.0 while preserving original suite; synthetic hotpath projection profile/work counters show45000 ->8 examinations with local equivalent outputs; unslop formatter consolidation preserves sampled legacy bytes/stdout; toy Git stages only task hunk; README snippets and static metadata checks execute locally.

Architecture, UX, UI recreation and checkout outputs remain source/static evidence. Browser server denied and file URL policy blocked, preserved without retry/bypass. Security/debug/readiness/deployment scenarios are bounded plans/verdicts, not actual system verification. Capacity/cost arithmetic remains synthetic. Root independently adjudicates these observations.

Repository validation outputs are retained in the three validator text files; their exact statuses live in commands.jsonl. No shared repository commit, push, source-skill modification, paid CLI, live deployment, publication or external service mutation executed. The sole commit is the explicitly authorized toy janitor baseline.\n''')
(EVID/'evidence-hashes.json').write_text(json.dumps(hashes(EVID),indent=2)+'\n')
print(json.dumps({'tasks':len(rows),'preservation':checks,'overall_report':str(EVID/'report.json')}))
