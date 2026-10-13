from pathlib import Path
from html.parser import HTMLParser
import hashlib
class Parser(HTMLParser):
    def __init__(self): super().__init__(); self.elements=[]
    def handle_starttag(self,tag,attrs): self.elements.append((tag,dict(attrs)))
p=Parser(); s=Path('index.html').read_text(); p.feed(s)
assert ('meta',{'name':'viewport','content':'width=device-width, initial-scale=1'}) in p.elements
assert any(t=='main' for t,a in p.elements)
assert sum(t=='th' and a.get('scope')=='col' for t,a in p.elements)==3
assert any(t=='button' and a.get('onclick')=="alert('todo')" for t,a in p.elements)
assert Path('tokens.css').read_bytes()==Path('/Users/uday/Skills/benchmarks/fixtures/polish-dashboard/tokens.css').read_bytes()
assert all(v in s for v in ('1,204','$8,210','+12%','#1024','#1025','$54.00','$12.50'))
def luminance(h):
    vals=[int(h[i:i+2],16)/255 for i in (1,3,5)]
    vals=[v/12.92 if v<=.04045 else ((v+.055)/1.055)**2.4 for v in vals]
    return sum(v*w for v,w in zip(vals,(.2126,.7152,.0722)))
for name,a,b in [('text/surface','#1a2233','#ffffff'),('muted/surface','#5b6478','#ffffff'),('primary/surface','#2f6fed','#ffffff')]:
    la,lb=sorted([luminance(a),luminance(b)]); ratio=(lb+.05)/(la+.05)
    print(f'{name}: computed sRGB contrast {ratio:.3f}:1'); assert ratio>=4.5
print('Static checks passed: token bytes, visible data, existing action, viewport and structural semantics. Rendering and keyboard UNVERIFIED.')
