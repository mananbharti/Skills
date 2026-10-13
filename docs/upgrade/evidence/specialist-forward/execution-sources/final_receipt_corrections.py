from record import *
# Narrow a publication claim to what the fixture actually declares.
for p in [BASE/'frontpage/work/README.md',EVID/'frontpage/output/README.md']:
 s=p.read_text().replace('There is no published package, test suite or benchmark supplied by this fixture.','This fixture supplies no package declaration, test suite or benchmark.');p.write_text(s)
p=EVID/'frontpage/artifact.md';s=p.read_text().replace('no package declaration exists.','no package declaration is supplied.').replace('no package publication or broader support evidence.','no package publication or broader support evidence.');p.write_text(s)
# No bash snippet changed by this correction; keep executed output. Deliver a rerunnable comparison against retained raw input.
w=BASE/'ditto/work';p=w/'compare.py';s=p.read_text().replace('import re,json','import re,json,sys').replace('source=Path("reference.html").read_text();target=Path("index.html").read_text()','source=Path(sys.argv[1]).read_text();target=Path("index.html").read_text()');p.write_text(s)
run('ditto',['python3','compare.py','../original/reference.html'],name='static-comparison-explicit-source.txt')
shutil.copy(p,EVID/'ditto/output/compare.py')
p=EVID/'ditto/artifact.md';p.write_text(p.read_text()+'\nReproduce static comparison from the saved output directory: `python3 compare.py ../input/reference.html`. The original reference stays under raw input; the reconstruction does not include the source script. Final explicit-source comparison ran successfully in owned workspace.\n')
# Preserve all last corrections as raw execution sources and refresh only our evidence hashes.
shutil.copy(BASE/'final_receipt_corrections.py',EVID/'execution-sources/final_receipt_corrections.py')
for slug in TASKS:
 (EVID/slug/'output-hashes.json').write_text(json.dumps(hashes(EVID/slug/'output'),indent=2)+'\n')
(EVID/'evidence-hashes.json').write_text(json.dumps({k:v for k,v in hashes(EVID).items() if k!='evidence-hashes.json'},indent=2)+'\n')
print('Final artifact-only wording/comparison corrections saved; first outcomes preserved.')
