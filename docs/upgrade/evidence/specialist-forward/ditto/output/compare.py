from pathlib import Path
from html.parser import HTMLParser
import re,json,sys
source=Path(sys.argv[1]).read_text();target=Path("index.html").read_text()
class P(HTMLParser):
    def __init__(self):super().__init__();self.tags=[];self.assets=[]
    def handle_starttag(self,tag,attrs):
        self.tags.append(tag);attrs=dict(attrs)
        if tag=="img":self.assets.append(attrs["src"])
s=P();s.feed(source);t=P();t.feed(target)
assert len([x for x in s.tags if x=="button"])==len([x for x in t.tags if x=="button"])==1
assert t.tags.count("a")==5
assert all(Path(asset).is_file() for asset in t.assets)
assert "ANALYTICS_KEY" not in target and "Comic Sans" not in target and "<script" not in target
assert "repeat(3,1fr)" in target and "font-size:40px" in target
assert "--action:#e8590c" in target and "--background:#eef1f6" in target
print(json.dumps({"comparison_rung":"static source only", "source_buttons":s.tags.count("button"),"target_buttons":t.tags.count("button"),"source_links":s.tags.count("a"),"target_links":t.tags.count("a"),"target_local_assets":t.assets,"base_grid":"3columns","base_h1":"40px","source_scripts":"removed, not copied","browser_fidelity":"unverified"},indent=2))
