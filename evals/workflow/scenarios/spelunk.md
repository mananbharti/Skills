# Workflow scenarios — spelunk

Authored 2026-09-14 (v1 campaign, Phase 03, zero-spend: no agent runs used).
Same contract as `signature-skills.md`: setup → task → candidate checks
(D#, deterministic where possible) → rubric dimensions (R#, qualitative,
graded blind). Authored ≠ executed: each scenario counts as coverage only
after a runner executes it against a real agent and stores raw results.

## spelunk

### SP1 normal — task-specific locate (quick mode)

- Setup: `benchmarks/fixtures/ts-dashboard`; question "where is the Order type defined?".
- Task: answer in quick mode.
- D1: answer names all three definition sites (`src/App.tsx`, `src/components/OrderList.tsx`, `src/api/orders.ts`).
- D2: every claimed path exists in the fixture (zero hallucinated paths).
- D3: response is a direct answer + ≤ 10-line context strip (no deep-map ceremony).
- R1: would `sleuth`/`pilot` have everything needed to act on this answer?

### SP2 hard edge — monorepo, wrong app at first glance

- Setup: synthetic monorepo with 3 apps; request concerns only `apps/billing`.
- Task: map the relevant app.
- D1: output maps `apps/billing` only; other apps appear at most in a one-line "not covered" note.
- D2: entry point + one traced execution path named with real symbols.
- D3: tool-call budget respected (quick ≤ 25); no recursive full-tree reads.
- R1: did the map stay scoped under ambiguity, or did it boil the ocean?

### SP3 capability/failure — no git, no manifests, no symbols

- Setup: directory of plain scripts with no manifests, no git history, no indexable symbols.
- Task: map it anyway.
- D1: output states what is missing (no manifest → stack inferred from extensions, labeled inferred).
- D2: an "Open unknowns" / "not covered" section exists and is non-empty.
- D3: no invented commands (no "run npm test" when no manifest defines it).
- R1: is the honesty about unknowns as useful as the facts found?

### SP4 restraint — one obvious file

- Setup: "what does `src/api/orders.ts` do" in a mapped repo.
- Task: answer with minimum motion.
- D1: answer comes from reading that file (no inventory run, no map artifact).
- D2: no `docs/repo-map.md` created; no mode escalation proposed.
- R1: did anything happen that reading the file didn't require?

### SP5 adversarial — README lies, code tells the truth

- Setup: fixture whose README describes an architecture the code contradicts (e.g. README claims Postgres + tests; code uses SQLite + has no tests).
- Task: map the repo truthfully.
- D1: output follows the code (SQLite, no tests) and flags the README divergence explicitly as cognitive debt.
- D2: every stack/command claim carries a real path; README-derived claims are labeled as such or absent.
- D3: no claim is sourced from the README alone where code contradicts it.
- R1: would a planner acting on this map be surprised by reality?

Upgrade cases authored 2026-10-14.

Authored specifications, not executed outcomes. Synthetic setups below must be
materialized in isolated workspaces by a runner before grading.

### SP6 generated — wrong apparent owner

- Setup: Generated API client and generator schema define same interface; user asks where to fix response type.
- Task: Locate source of truth.
- D1: Names schema/generator input as owner; generated file as derivative.
- D2: Cites registration/caller, not just matching symbol name.
- R1: Would following map survive regeneration?

### SP7 dynamic — plugin registration

- Setup: Python plugin function exists but only one plugin is registered in config.
- Task: Explain active execution path.
- D1: Distinguishes defined function from registered runtime path.
- D2: Runtime behavior marked inferred when no execution evidence exists.
- R1: Does a symbol match become an unsupported call graph?

### SP8 stale — fresh map on wrong branch

- Setup: repo-map from branch A says sqlite; branch B code uses another adapter.
- Task: Answer current storage owner.
- D1: Consults affected source and flags stale scoped claim.
- D2: Does not erase history or trust mtime.
- R1: Is branch provenance actionable?

### SP9 scanner — cache and vendor noise

- Setup: Temporary tree: src/a.py and tests/test_a.py plus large .venv/vendor/generated sources with TODO markers.
- Task: Run bundled inventory --json.
- D1: Source/test counts include first-party files only; large-file/debt output omits excluded trees.
- D2: JSON parses and no file content/secret values appear.
- R1: Do all inventory sections use consistent boundaries?

### SP10 budget — huge mixed repository

- Setup: Known Go handler in one app; repository also contains vendored JVM and mobile output.
- Task: Map request path in quick mode.
- D1: Reads target imports/registration only; no whole vendor scan.
- D2: Reports uncovered apps and actual target commands.
- R1: Does the map stop when requested uncertainty closes?
