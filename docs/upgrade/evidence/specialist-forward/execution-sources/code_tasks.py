from record import *
import difflib
# proof: preserve suite, add public behavior assertion only.
w=BASE/'proof'/'work'
run('proof',['python3','-m','unittest','discover','-s','tests','-v'],name='baseline-tests.txt')
(w/'tests/test_discount.py').write_text('''import unittest
from cart import total

class TestDiscount(unittest.TestCase):
    def test_percentage_discount_is_applied_once_to_whole_cart(self):
        cart = [{"name": "book", "price": 20.0, "qty": 1},
                {"name": "pen", "price": 5.0, "qty": 2}]
        self.assertEqual(total(cart, discount=0.10), 27.0)
''')
p=run('proof',['python3','-m','unittest','discover','-s','tests','-v'],name='regression-tests.txt')
assert p.returncode==1 and '24.3 != 27.0' in p.stderr
assert (w/'cart.py').read_bytes()==(BASE/'proof/original/cart.py').read_bytes()
assert (w/'tests/test_cart.py').read_bytes()==(BASE/'proof/original/tests/test_cart.py').read_bytes()
report('proof','''Behavior: percentage discount is applied once to the whole cart. Risk: a customer receives the wrong charged amount. Boundary: real pure total function, existing stdlib unittest runner; no mock or new framework. Oracle: $20 book + two $5 pens = $30 subtotal; 10% discount => $27.00. Fixture is a fresh in-memory list; observable return asserted.

Baseline: 3 existing tests passed. After adding tests/test_discount.py: runner exited1; 4 ran, 1 assertion failure, existing 3 remain green. Actual returned24.3 differs from27.0, exposing two discount multiplications. App code and existing tests are byte-identical to originals; no implementation fix made.

Failure sensitivity is established by the actual known-broken function (not an import/setup failure). This is a red regression deliverable, not a passing change. Green after a correct fix remains unverified because fixes were forbidden. Empty/zero-discount behavior is covered by preserved tests; input validation and payment integration remain outside this pure calculation boundary. Next owner: billing maintainer/sleuth for a separately authorized fix.''','red-regression',['Fix prohibited; green-after-fix and payment integration not tested.'])
# unslop: characterize side effects as well as return bytes before simple deduplication.
w=BASE/'unslop'/'work'
(w/'characterize.py').write_text('''import io,json,contextlib
import shop
cases=[[],[{"price":20.,"qty":1},{"price":5.,"qty":2}],[{"price":0.105,"qty":1}],[{"price":-1.25,"qty":2}]]
out=[]
for lines in cases:
    log=io.StringIO()
    with contextlib.redirect_stdout(log): value=shop.totals(lines)
    out.append({"input":lines,"value":value,"stdout":log.getvalue()})
exports=[shop.export_legacy(oid,cents).encode().hex() for oid,cents in [("A1",3000),("x|y",-125),("",0)]]
log=io.StringIO()
with contextlib.redirect_stdout(log): notified=shop.notify("fake-test-message")
print(json.dumps({"totals":out,"export_bytes_hex":exports,"notify_result":notified,"notify_stdout":log.getvalue()},sort_keys=True))
''')
run('unslop',['python3','-m','unittest','discover','-s','tests','-v'],name='baseline-tests.txt')
a=run('unslop',['python3','characterize.py'],name='baseline-characterization.txt')
run('unslop',['rg','-n','_format_price|format_price|BasePricer|Pricer|_old_compute|notify','.', '-g','!characterize.py'],name='reachability.txt')
before=(w/'shop.py').read_text()
# Single structural change: one identical formatter, preserving private name import alias.
after=before.replace('from utils import format_price\n\n\ndef _format_price(cents):\n    return f"${cents / 100:.2f}"','from utils import format_price\n\n# Preserve the existing private symbol while sharing the identical formatter.\n_format_price = format_price')
(w/'shop.py').write_text(after)
(EVID/'unslop/batch.patch').write_text(''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='a/shop.py',tofile='b/shop.py')))
run('unslop',['python3','-m','unittest','discover','-s','tests','-v'],name='post-tests.txt')
b=run('unslop',['python3','characterize.py'],name='post-characterization.txt');assert a.stdout==b.stdout
report('unslop','''Mode: Detox, one structural batch: consolidate byte-identical money formatting using the existing utils.format_price while retaining _format_price as an alias for callers. Protected invariant: totals result, DEBUG stdout, exception path and legacy pipe export bytes remain unchanged. No source-skill/fixture edits, commit or broad rewrite.

| Rank | Location | Observation | Decision |
| --- | --- | --- | --- |
| High leverage | shop.py:2–6 | Same formatter exists in utils.py; duplicate changes can drift. | Shared implementation, old symbol retained. |
| Medium | shop.py:_old_compute, BasePricer/Pricer | No fixture callers found, but external library callers not known. | Deferred; did not delete publicly importable symbols on text absence alone. |
| Correctness concern | shop.py:notify | Exceptions intentionally swallowed in observed baseline. | Kept and handed off; changing it would change behavior. |
| Cosmetic | shop.py:totals, utils.py:os import | DEBUG stdout and unused import. | Kept this round to isolate one structural change. |

Baseline and post suite: 3/3 passed, actual unittest exit0. Characterization JSON exactly equal for empty, ordinary, fractional rounding and negative-price totals, stdout, notification result, and legacy exports with ordinary/pipe/empty IDs. Original exports captured as hex bytes rather than merely displayed strings. batch.patch is reviewable; only formatter definition replaced by alias. Net shop.py line delta: -1. Revert by restoring this one batch from original/shop.py.

Residual risk: formatter object identity/monkeypatching may differ outside the fixture; no external consumers are supplied. Existing private name survives. No UI requires a browser here. Baseline/post evidence supports the bounded fixture behavior; it does not prove all unknown consumers.''','bounded-cleanup',['External import/monkeypatch consumers unknown; public zombie classes left intact.'])
# hotpath: profile and benchmark fixed synthetic lists; change only repeated catalog lookup.
w=BASE/'hotpath'/'work'
(w/'measure.py').write_text('''import cProfile,pstats,io,json,time,statistics,platform,sys
import orders
lines=[{"sku":f"sku-{(i%8)+1}","qty":(i%3)+1} for i in range(10000)]
for _ in range(5): orders.totals(lines)
values=[]
for _ in range(31):
    start=time.perf_counter_ns(); result=orders.totals(lines); values.append((time.perf_counter_ns()-start)/1e6)
orders.SCANS["n"]=0; result=orders.totals(lines); count=orders.SCANS["n"]
prof=cProfile.Profile();prof.runcall(orders.totals,lines); s=io.StringIO();pstats.Stats(prof,stream=s).sort_stats("cumulative").print_stats(8)
print(json.dumps({"runtime":sys.version,"platform":platform.platform(),"workload":"synthetic10000-lines8-skus quantities1..3; catalog fixture8 rows; no network/concurrency","warmups":5,"samples_ms":values,"p50_ms":statistics.median(values),"p95_ms":sorted(values)[29],"range_ms":[min(values),max(values)],"result":result,"catalog_examinations":count},indent=2));print(s.getvalue())
''')
(w/'check_behavior.py').write_text('''import importlib.util, random, json
import orders
spec=importlib.util.spec_from_file_location("baseline","../original/orders.py"); old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
random.seed(11)
cases=[[],[{"sku":"sku-1","qty":0}],[{"sku":"sku-8","qty":-2}],[{"sku":"sku-3","qty":0.5}],[{"sku":"absent","qty":1}]]
for n in range(100): cases.append([{"sku":f"sku-{random.randint(1,8)}","qty":random.choice([0,1,2,-1,.5])} for _ in range(n)])
def outcome(module,lines):
    try:return ("value",module.totals(lines))
    except Exception as e:return ("error",type(e).__name__,e.args)
for case in cases:assert outcome(old,case)==outcome(orders,case),(case,outcome(old,case),outcome(orders,case))
# First duplicate price wins; mutation between calls must be visible.
for db in [[("sku-1",1.),("sku-1",999.)],[("sku-1",7.)],[("sku-1",8.)]]:
    old.DB=db;orders.DB=db
    assert outcome(old,[{"sku":"sku-1","qty":2}])==outcome(orders,[{"sku":"sku-1","qty":2}])
print(json.dumps({"equivalent_list_cases":len(cases),"duplicate_and_catalog_replacement_cases":3,"basis":"string SKU fixture contract; no concurrent catalog mutation or arbitrary equality/hash objects"}))
''')
run('hotpath',['python3','measure.py'],name='baseline-measurement.txt')
before=(w/'orders.py').read_text();start=before.index('def totals(lines):')
after=before[:start]+'''def totals(lines):
    # Build afresh for each call: no stale cross-request catalog cache.
    prices = None
    out = 0.0
    for line in lines:
        if prices is None:
            prices = {}
            for key, price in DB:
                SCANS["n"] += 1
                prices.setdefault(key, price)  # Preserve first duplicate match.
        out += prices[line["sku"]] * line["qty"]
    return round(out, 2)
'''
(w/'orders.py').write_text(after)
(EVID/'hotpath/change.patch').write_text(''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='a/orders.py',tofile='b/orders.py')))
run('hotpath',['python3','check_behavior.py'],name='correctness.txt')
run('hotpath',['python3','measure.py'],name='after-measurement.txt')
# parsed metric helper
raw=[json.loads(line) for line in (EVID/'hotpath/commands.jsonl').read_text().splitlines()]
def metric(output):return json.JSONDecoder().raw_decode(output)[0]
a=metric(raw[0]['stdout']);b=metric(raw[-1]['stdout'])
threshold=max(1.0,(a['range_ms'][1]-a['range_ms'][0])/a['p50_ms']*100)
run('hotpath',[str(BASE/'hotpath/skill/scripts/measure-report'),'--baseline',str(a['p50_ms']),'--after',str(b['p50_ms']),'--conditions','Local Python; same8-rowcatalog and10000 synthetic lines;5warmups31samples; p50 milliseconds; no network or concurrency','--threshold',str(threshold)],name='delta-helper.txt')
report('hotpath',f'''Target declared for this bounded fixture: reduce catalog examinations from repeated per-line scans to at most8 for the 10000-line synthetic workload, preserving numerical results and error type/arguments for string SKUs. Timing keep limit: reduction must exceed the baseline relative max–min spread (or1% whichever larger); revert on correctness failure or a smaller/noisy timing benefit. Not a production latency budget.

Baseline cProfile identifies lookup as cumulative hot path; the fmt helper is never called. One causal variable changed: build a per-call price index on first line; first duplicate wins via setdefault, original arithmetic order and rounding retained, catalog replacements between calls visible. Public lookup itself preserved.

Fixed conditions: runtime/platform recorded, fixture8-row catalog, synthetic10000 lines,5warmups31samples, perf_counter_ns, no network or concurrent load. Baseline p50={a['p50_ms']:.6f}ms, p95={a['p95_ms']:.6f}ms, range={a['range_ms']}; after p50={b['p50_ms']:.6f}ms, p95={b['p95_ms']:.6f}ms, range={b['range_ms']}. Catalog examinations={a['catalog_examinations']} -> {b['catalog_examinations']}; results identical={a['result']}. Declared evidence-derived threshold={threshold:.3f}%; helper records delta. Kept for this large synthetic list: structural work reduction and bounded timing gain; revert from original/orders.py if invalidated.

Correctness command passed105 list cases plus3 duplicate/catalog-replacement cases using deterministic seed11 and baseline module. Covers empty, zero/negative/fractional quantity, unknown SKU, rounding and first duplicate semantics. Index costsO(unique catalog) temporary memory; indexing whole catalog can cost more for one short order, so do not infer all workloads improve. Stop after bounded target reached; no second optimization.

Limitations: synthetic workload, local microbenchmark, sequential baseline/after not interleaved, no real-user latency, no RSS measurement, string SKU keys assumed from fixture. Catalog mutation during generator iteration and arbitrary custom equality/hash objects were not tested; these may differ and require owner contract before use beyond list/stringSKU scope. SCANS remains diagnostic but now counts index build examinations.''','measured-local-optimization',['Synthetic microbenchmark only; short-order and memory tradeoffs, dynamic-generator mutation semantics not established.'],extra={'baseline':a,'after':b,'threshold_percent':threshold})
