# Workflow scenarios

Each scenario separates Setup/Task from candidate checks and qualitative
rubrics. Authored coverage, executed trials and graded outcomes are distinct.
`scripts/eval-workflow --check` validates the current schema and enforces at
least ten authored cases per frozen skill; this does not establish effectiveness.

| Skill | Authored cases (including retained signature cases) | Fixture-backed | Current evidence |
| --- | --- | --- | --- |
| `backend` | 14 | 4 | [Upgrade ledger](../../../docs/upgrade-ledger.md): local exploratory observations; native activation/lift UNVERIFIED |
| `blueprint` | 14 | 7 | [Upgrade ledger](../../../docs/upgrade-ledger.md): local exploratory observations; native activation/lift UNVERIFIED |
| `cleared` | 10 | 1 | [Upgrade ledger](../../../docs/upgrade-ledger.md): local exploratory observations; native activation/lift UNVERIFIED |
| `concierge` | 12 | 1 | [Upgrade ledger](../../../docs/upgrade-ledger.md): local exploratory observations; native activation/lift UNVERIFIED |
| `distill` | 10 | 1 | [Upgrade ledger](../../../docs/upgrade-ledger.md): local exploratory observations; native activation/lift UNVERIFIED |
| `ditto` | 11 | 2 | [Upgrade ledger](../../../docs/upgrade-ledger.md): local exploratory observations; native activation/lift UNVERIFIED |
| `findable` | 10 | 1 | [Upgrade ledger](../../../docs/upgrade-ledger.md): local exploratory observations; native activation/lift UNVERIFIED |
| `friction` | 11 | 4 | [Upgrade ledger](../../../docs/upgrade-ledger.md): local exploratory observations; native activation/lift UNVERIFIED |
| `frontpage` | 13 | 2 | [Upgrade ledger](../../../docs/upgrade-ledger.md): local exploratory observations; native activation/lift UNVERIFIED |
| `frugal` | 13 | 2 | [Upgrade ledger](../../../docs/upgrade-ledger.md): local exploratory observations; native activation/lift UNVERIFIED |
| `handsfree` | 11 | 0 | [Upgrade ledger](../../../docs/upgrade-ledger.md): local exploratory observations; native activation/lift UNVERIFIED |
| `harden` | 13 | 3 | [Upgrade ledger](../../../docs/upgrade-ledger.md): local exploratory observations; native activation/lift UNVERIFIED |
| `headroom` | 11 | 1 | [Upgrade ledger](../../../docs/upgrade-ledger.md): local exploratory observations; native activation/lift UNVERIFIED |
| `hotpath` | 11 | 2 | [Upgrade ledger](../../../docs/upgrade-ledger.md): local exploratory observations; native activation/lift UNVERIFIED |
| `hotseat` | 16 | 1 | [Upgrade ledger](../../../docs/upgrade-ledger.md): local exploratory observations; native activation/lift UNVERIFIED |
| `janitor` | 10 | 2 | [Upgrade ledger](../../../docs/upgrade-ledger.md): local exploratory observations; native activation/lift UNVERIFIED |
| `masterplan` | 11 | 2 | [Upgrade ledger](../../../docs/upgrade-ledger.md): local exploratory observations; native activation/lift UNVERIFIED |
| `pilot` | 11 | 0 | [Upgrade ledger](../../../docs/upgrade-ledger.md): local exploratory observations; native activation/lift UNVERIFIED |
| `polish` | 14 | 6 | [Upgrade ledger](../../../docs/upgrade-ledger.md): local exploratory observations; native activation/lift UNVERIFIED |
| `proof` | 11 | 2 | [Upgrade ledger](../../../docs/upgrade-ledger.md): local exploratory observations; native activation/lift UNVERIFIED |
| `recall` | 10 | 1 | [Upgrade ledger](../../../docs/upgrade-ledger.md): local exploratory observations; native activation/lift UNVERIFIED |
| `referee` | 10 | 1 | [Upgrade ledger](../../../docs/upgrade-ledger.md): local exploratory observations; native activation/lift UNVERIFIED |
| `roadtest` | 13 | 2 | [Upgrade ledger](../../../docs/upgrade-ledger.md): local exploratory observations; native activation/lift UNVERIFIED |
| `runway` | 10 | 0 | [Upgrade ledger](../../../docs/upgrade-ledger.md): local exploratory observations; native activation/lift UNVERIFIED |
| `scout` | 10 | 0 | [Upgrade ledger](../../../docs/upgrade-ledger.md): local exploratory observations; native activation/lift UNVERIFIED |
| `sleuth` | 10 | 1 | [Upgrade ledger](../../../docs/upgrade-ledger.md): local exploratory observations; native activation/lift UNVERIFIED |
| `spelunk` | 10 | 1 | [Upgrade ledger](../../../docs/upgrade-ledger.md): local exploratory observations; native activation/lift UNVERIFIED |
| `unslop` | 14 | 4 | [Upgrade ledger](../../../docs/upgrade-ledger.md): local exploratory observations; native activation/lift UNVERIFIED |

Historical outcome tasks and result records are unchanged. Some authored
workflow assertions were corrected where they contradicted the intended
contract; old outcomes are not regraded against these revisions. Synthetic
Setup-only cases require actual materialization and execution before grading.

```bash
scripts/eval-workflow --check
scripts/eval-workflow --list
```

Live execution requires an explicit scenario and the human-paid guard for
billed adapters. `scripts/eval-workflow --scenario H3 --agent codex` without
the two human keys refuses before any agent invocation. CI runs only local
deterministic checks. Retained exploratory in-session artifacts live under
`docs/upgrade/evidence/`; they are not a randomized baseline/treatment campaign.
