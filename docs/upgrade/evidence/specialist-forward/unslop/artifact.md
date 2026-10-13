Mode: Detox, one structural batch: consolidate byte-identical money formatting using the existing utils.format_price while retaining _format_price as an alias for callers. Protected invariant: totals result, DEBUG stdout, exception path and legacy pipe export bytes remain unchanged. No source-skill/fixture edits, commit or broad rewrite.

| Rank | Location | Observation | Decision |
| --- | --- | --- | --- |
| High leverage | shop.py:2–6 | Same formatter exists in utils.py; duplicate changes can drift. | Shared implementation, old symbol retained. |
| Medium | shop.py:_old_compute, BasePricer/Pricer | No fixture callers found, but external library callers not known. | Deferred; did not delete publicly importable symbols on text absence alone. |
| Correctness concern | shop.py:notify | Exceptions intentionally swallowed in observed baseline. | Kept and handed off; changing it would change behavior. |
| Cosmetic | shop.py:totals, utils.py:os import | DEBUG stdout and unused import. | Kept this round to isolate one structural change. |

Baseline and post suite: 3/3 passed, actual unittest exit0. Characterization JSON exactly equal for empty, ordinary, fractional rounding and negative-price totals, stdout, notification result, and legacy exports with ordinary/pipe/empty IDs. Original exports captured as hex bytes rather than merely displayed strings. batch.patch is reviewable; only formatter definition replaced by alias. Net shop.py line delta: -1 (50 -> 49 lines). Revert by restoring this one batch from original/shop.py.

Residual risk: formatter object identity/monkeypatching may differ outside the fixture; no external consumers are supplied. Existing private name survives. No UI requires a browser here. Baseline/post evidence supports the bounded fixture behavior; it does not prove all unknown consumers.
