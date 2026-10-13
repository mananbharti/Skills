from pathlib import Path
from html.parser import HTMLParser
import xml.etree.ElementTree as ET,json
class P(HTMLParser):
 def __init__(self):super().__init__();self.meta={};self.links=[];self.canonical=[];self.headings=[];self.title="";self.in_title=False
 def handle_starttag(self,t,attrs):
  d=dict(attrs)
  if t=="meta":self.meta[d.get("name",d.get("property",""))]=d.get("content","")
  if t=="a":self.links.append(d["href"])
  if t=="link" and d.get("rel")=="canonical":self.canonical.append(d["href"])
  if t in ["h1","h2"]:self.headings.append(t)
  if t=="title":self.in_title=True
 def handle_endtag(self,t):
  if t=="title":self.in_title=False
 def handle_data(self,s):
  if self.in_title:self.title+=s
pages={}
for name in ["index.html","about.html"]:
 p=P();p.feed(Path(name).read_text());assert p.meta["description"] and p.meta["robots"]=="index, follow";assert len(p.canonical)==1;assert all(Path(x).is_file() for x in p.links);assert p.headings.count("h1")==1
 pages[name]={"title":p.title,"meta":p.meta,"canonical":p.canonical,"links":p.links,"headings":p.headings}
assert pages["index.html"]["title"]!=pages["about.html"]["title"]
assert pages["index.html"]["meta"]["description"]!=pages["about.html"]["meta"]["description"]
urls=[n.text for n in ET.parse("sitemap.xml").findall(".//{*}loc")]
assert urls==["https://notesapp.example/","https://notesapp.example/about.html"]
assert "Disallow: /" not in Path("robots.txt").read_text()
assert "aggregateRating" not in Path("index.html").read_text()
print(json.dumps({"rung":"static initial HTML/config only","pages":pages,"sitemap":urls,"http_status":"unverified","browser_render":"unverified","indexing":"unverified"},indent=2))
