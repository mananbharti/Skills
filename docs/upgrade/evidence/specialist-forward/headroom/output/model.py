import json
p=json.load(open("capacity-case.json"))
r,e=p["workloads"]
print(json.dumps({"basis":"synthetic assumptions, not measured capacity", "read_average_inflight":r["offered_jobs_per_second"]*r["average_service_seconds"],"existing_backlog_growth_jobs_s":e["offered_jobs_per_second"]-e["successful_completions_per_second"],"existing_recovery_seconds":None,"candidate_ideal_recovery_seconds":e["backlog_jobs"]/(p["candidate_exports"]["successful_completions_per_second"]-e["offered_jobs_per_second"]),"minimum_drain_for_1800s":e["offered_jobs_per_second"]+e["backlog_jobs"]/e["deadline_seconds"],"generator_started_fraction":p["load_report"]["started_per_second"]/p["load_report"]["scheduled_per_second"]},indent=2))
