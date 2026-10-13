recall: DECISIONS.md +1 (PostgreSQL target; SQLite stays live until verified migration) · STATUS.md adds scoped current decision/next action and labels old snapshot historical · PROJECT_CONTEXT.md records the user-supplied live-system constraint.

Bundled `check-memory --json` returned no findings. Original decision history and rationale remain byte-for-byte; LEARNINGS unchanged. Safe next action is schema/tooling inspection and reversible verification on a copy. No migration or cutover ran. Earlier work status and the actual live database remain unverified.
