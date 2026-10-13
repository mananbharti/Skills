Mode: read-only/static investigation. Only an intermittent export timeout and existence of one log sample are reported. Its contents, timestamp, trace ID, environment, candidate, elapsed time and timeout layer were not supplied. No reproduction or diagnosis ran; root cause is unconfirmed.

1. Preserve the sample; request a sanitized complete error/stack, UTC time, request/job correlation ID, candidate/configuration, deadline, data size and expected outcome. Do not truncate cause/exception frames.
2. Compare one successful export and the failure in the same environment using existing read-only logs/traces: accepted time, worker start, data-read end, render end, downstream-response end, retries and finish. Redact data; record units and clock sources.
3. Keep falsifiable hypotheses: queue wait (worker starts late), data/query work (data span dominates), rendering work (render span dominates), downstream dependency (waiting/retries dominate), and timeout configuration mismatch (deadline shorter than successful work). The symptom alone supports none over another.
4. First discriminating observation: determine which phase consumed the deadline with those correlated boundary timestamps. If unavailable, request narrow passive instrumentation from the owner; do not enable it in production here.
5. Ask for a disposable reproduction environment and smallest masked input only after the read-only comparison. A later controlled replay would hold candidate, input and dependencies fixed and measure success/failure counts; no replay executed now.

Stop: no patch, timeout increase, retry change, root-cause claim or production action. The next owner is the export maintainer; absent evidence stays unknown.
