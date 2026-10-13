from pathlib import Path
import re,subprocess,json
readme=Path("README.md").read_text()
for block in re.findall(r"```bash\n(.*?)```",readme,re.S):
    for command in block.strip().splitlines():
        p=subprocess.run(command,shell=True,text=True,capture_output=True)
        print(json.dumps({"command":command,"exit":p.returncode,"stdout":p.stdout,"stderr":p.stderr}))
        assert p.returncode==0
