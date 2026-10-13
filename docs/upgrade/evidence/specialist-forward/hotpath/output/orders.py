"""Order totaling over a catalog list. Stdlib only.

Seeded structural waste: every price lookup linearly scans the whole
catalog, so N order lines cost ~N*len(DB) examinations. The per-line
`fmt` helper is a cold decoy — formatting is ~1% of the work.
"""

DB = [
    ("sku-1", 20.0),
    ("sku-2", 5.0),
    ("sku-3", 12.5),
    ("sku-4", 7.75),
    ("sku-5", 99.0),
    ("sku-6", 3.25),
    ("sku-7", 45.0),
    ("sku-8", 8.5),
]

SCANS = {"n": 0}


def lookup(sku):
    for key, price in DB:
        SCANS["n"] += 1
        if key == sku:
            return price
    raise KeyError(sku)


def fmt(name, amount):
    return f"{name}: ${amount:.2f}"


def totals(lines):
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
