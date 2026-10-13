import io,json,contextlib
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
