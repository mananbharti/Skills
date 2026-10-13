import cProfile,pstats,io,json,time,statistics,platform,sys
import orders
lines=[{"sku":f"sku-{(i%8)+1}","qty":(i%3)+1} for i in range(10000)]
for _ in range(5): orders.totals(lines)
values=[]
for _ in range(31):
    start=time.perf_counter_ns(); result=orders.totals(lines); values.append((time.perf_counter_ns()-start)/1e6)
orders.SCANS["n"]=0; result=orders.totals(lines); count=orders.SCANS["n"]
prof=cProfile.Profile();prof.runcall(orders.totals,lines); s=io.StringIO();pstats.Stats(prof,stream=s).sort_stats("cumulative").print_stats(8)
print(json.dumps({"runtime":sys.version,"platform":platform.platform(),"workload":"synthetic10000-lines8-skus quantities1..3; catalog fixture8 rows; no network/concurrency","warmups":5,"samples_ms":values,"p50_ms":statistics.median(values),"p95_ms":sorted(values)[29],"range_ms":[min(values),max(values)],"result":result,"catalog_examinations":count},indent=2));print(s.getvalue())
