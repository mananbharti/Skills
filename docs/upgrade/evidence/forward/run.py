from pathlib import Path
import subprocess,sys,json,datetime
slug,label,*cmd=sys.argv[1:]
base=Path('/Users/uday/Skills/docs/upgrade/evidence/forward')/slug
p=subprocess.run(cmd,cwd=Path('/private/tmp/skills-forward')/slug,text=True,capture_output=True)
r={'command':cmd,'cwd':str(Path('/private/tmp/skills-forward')/slug),'time_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr}
(base/(label+'.json')).write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r,indent=2))
