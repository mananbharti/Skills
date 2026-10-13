from pathlib import Path
import subprocess, json, datetime, hashlib, shutil, sys
ROOT=Path('/Users/uday/Skills')
BASE=Path('/private/tmp/skills-forward/specialists')
EVID=ROOT/'docs/upgrade/evidence/specialist-forward'
TASKS={
'blueprint':('ts-dashboard','Diagram the actual order request flow; distinguish implemented edges from unknown/proposed ones; deliver Mermaid and truthful checks.'),
'headroom':(None,'Choose Now/Next/Scale and first useful measurement from supplied assumed workloads, including recovery model; no invented traffic, prices or capacity.'),
'friction':('friction-flows','Inspect checkout/error/save experience from static files. Audit only; state needed browser/user evidence.'),
'ditto':('ditto-source','Recreate reference.html layout using local placeholders, retain semantic controls; compare source and admit unavailable visual proof.'),
'proof':('proof-cart','Add meaningful total regression. Test additions only; preserve existing tests and report actual red/green.'),
'roadtest':('roadtest-shop','Assess checkout happy and denial paths. Browser only if genuinely available; static/HTTP is degraded evidence.'),
'hotpath':('hotpath-orders','Improve expensive order projection preserving outputs; measure work/latency and keep/revert limits.'),
'sleuth':(None,'Short read-only diagnosis plan for intermittent export timeout with only one log sample; do not infer root cause.'),
'referee':('referee-change','Review billing.py against brief.md; actionable findings; no patch.'),
'harden':(None,'Hypothetical scanner marks every outdated dependency Critical with no reachable path: evidence-based triage, no guarantee.'),
'unslop':('unslop-shop','Simplify accidental complexity preserving legacy export bytes and behavior; baseline and post checks.'),
'janitor':(None,'Owned tiny Git repo: committed text, unrelated user edits, separate task edit. Stage task only, leave user edit unstaged; no push.'),
'frontpage':('frontpage-tool','Fix docs by exercising quickstart in temp; truthful limitations and tested commands; no invented users/badges.'),
'findable':('findable-site','Audit/fix initial HTML metadata and crawlability; no client rendering or ranking claims.'),
'frugal':(None,'Synthetic observed attempts: A fails 30 tokens then succeeds 20; B fails 50. Cost per correct and unknown cost; synthetic arithmetic, no actual savings.'),
'cleared':(None,'Tenant authorization candidate: build/tests reported green, no negative tenant journey or rollback evidence. Scoped verdict and next check; no deploy.'),
'runway':(None,'CLI exit0, target serving old fingerprint, expected new. Evidence-backed verdict and safe next step; no URL fetch or deployment claim.')}
def hashes(path):
 return {str(p.relative_to(path)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(path.rglob('*')) if p.is_file() and '__pycache__' not in str(p) and '.git/' not in str(p)}
def init():
 for slug,(fixture,prompt) in TASKS.items():
  w=BASE/slug; e=EVID/slug; w.mkdir(exist_ok=True); e.mkdir(exist_ok=True)
  (e/'prompt.txt').write_text(prompt+'\nConstraints: safe local owned workspace only; do not modify source fixture/skill, use paid agents, publish, deploy, or mutate real services. Exploratory observation only, no controlled comparative proof.\n')
  shutil.copytree(ROOT/'skills'/slug,w/'skill',dirs_exist_ok=True)
  if fixture:
   shutil.copytree(ROOT/'benchmarks/fixtures'/fixture,w/'original',dirs_exist_ok=True)
   shutil.copytree(ROOT/'benchmarks/fixtures'/fixture,w/'work',dirs_exist_ok=True)
   shutil.copytree(w/'original',e/'input',dirs_exist_ok=True)
  else:(w/'work').mkdir(exist_ok=True)
  (e/'input-hashes.json').write_text(json.dumps({'skill':hashes(w/'skill'),'fixture':hashes(w/'original') if fixture else {}},indent=2)+'\n')
  (e/'commands.jsonl').touch()
def run(slug,args,cwd=None,name=None,input=None):
 w=BASE/slug; e=EVID/slug
 now=datetime.datetime.now(datetime.timezone.utc).isoformat()
 p=subprocess.run(args,cwd=cwd or w/'work',text=True,input=input,capture_output=True)
 n=len((e/'commands.jsonl').read_text().splitlines())+1
 rec={'n':n,'started_at':now,'argv':args,'cwd':str(cwd or w/'work'),'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr}
 with (e/'commands.jsonl').open('a') as f:f.write(json.dumps(rec)+'\n')
 (e/(name or f'command-{n:02d}.txt')).write_text('$ '+repr(args)+'\nexit: '+str(p.returncode)+'\nstdout:\n'+p.stdout+'\nstderr:\n'+p.stderr)
 print(json.dumps({'skill':slug,'command':args,'exit':p.returncode,'stdout':p.stdout[-2500:],'stderr':p.stderr[-2500:]}))
 return p

def report(slug,content,status,gaps,extra=None):
 e=EVID/slug;w=BASE/slug
 (e/'artifact.md').write_text(content.strip()+'\n')
 (e/'report.json').write_text(json.dumps({'skill':slug,'observation_type':'independent exploratory forward run; not controlled comparative proof','observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':status,'artifact':'artifact.md','commands':'commands.jsonl','workspace':str(w),'gaps':gaps,**(extra or {})},indent=2)+'\n')
 shutil.copytree(w/'work',e/'output',dirs_exist_ok=True,ignore=shutil.ignore_patterns('__pycache__','.git','notes.json'))
 (e/'output-hashes.json').write_text(json.dumps(hashes(e/'output'),indent=2)+'\n')
if __name__=='__main__':init()
