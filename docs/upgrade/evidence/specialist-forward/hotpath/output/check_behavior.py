import importlib.util, random, json
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
