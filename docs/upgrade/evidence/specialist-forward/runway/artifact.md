Verdict: the expected new release is not verified live; promotion/release completion is BLOCKED on fingerprint mismatch.

| Observation | Source | Supported conclusion |
| --- | --- | --- |
| CLI exited 0 | Supplied scenario | Command reported success; does not establish public release behavior. |
| Target response fingerprint is old; expected new | Supplied scenario | Observed target content contradicts expected release identity. |

No URL was fetched, no deployment executed, no smoke or health check claimed. Observation timestamp, target, candidate artifact and raw response are missing; health, HTTPS, domains, logs, rollback and cause are unverified. The mismatch could involve target routing, artifact selection, asynchronous publication or a cache, but none is diagnosed.

Safe next step: the release owner compares read-only platform release metadata (immutable candidate hash, target mapping, publication completion, cache/routing state) with the existing sanitized target response evidence and records timestamp/headers. Obtain the normal public-path fingerprint again only in the separately authorized release workflow; require new plus key-flow evidence before declaring complete. Preserve the known previous version and rollback record. Do not redeploy, purge caches, switch traffic or rollback from CLI exit status alone.
