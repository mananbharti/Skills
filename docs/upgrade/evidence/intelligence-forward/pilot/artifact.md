Completed the authorized local slice: added a genuine module docstring to `app/main.py` and alphabetized `requirements.txt`.

Verified: Python parse/compile and executable AST equality after excluding the added docstring; file hash scope check; requirements preserve the exact dependency multiset. Commands and output: `commands.jsonl`. Diffs and before/after artifacts are saved here.

Default: concise description of the existing demo API. Actions were local AUTO work; no routine-choice question was asked. Recovery: the untouched fixture and `before/` copy.

Self-review after the full diff: only the approved first-statement docstring and dependency ordering changed; no blocker found. Fresh-context review was not performed.

Unverified: full application tests, build, lint/types and runtime behavior; the fixture defines only a uvicorn run command and contains no test suite or check configuration. The AST check supports preservation of executable statements; `__doc__` changes intentionally. Complete with unverified items.
