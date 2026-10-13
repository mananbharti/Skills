$ ['python3', '-c', 'from pathlib import Path; import re,json; s=Path("README.md").read_text(); links=re.findall(r"\\[[^\\]]+\\]\\(([^)]+)\\)",s); print(json.dumps({"local_links":{x:Path(x).is_file() for x in links},"external_links":[],"notes_json":Path("notes.json").read_text()})); assert all(Path(x).is_file() for x in links)']
exit: 0
stdout:
{"local_links": {"notes.py": true}, "external_links": [], "notes_json": "[\"hello\"]"}

stderr:
