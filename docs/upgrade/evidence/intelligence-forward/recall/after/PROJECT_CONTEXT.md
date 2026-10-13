# Project context
<!-- maintained by recall — stable facts only -->

## Stack
- Python 3.14, stdlib only, unittest via `python3 -m unittest discover -s tests -t .`

## Conventions
- Fixtures live in `benchmarks/fixtures/<skill>/`

## Database constraint
- Explicit user statement (2026-10-14): SQLite remains the live system until a verified migration. Future target decision: DECISIONS.md, 2026-10-14 PostgreSQL.
