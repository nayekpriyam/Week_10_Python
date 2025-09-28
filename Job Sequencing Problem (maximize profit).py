def job_sequencing(jobs):
    """
    jobs: list of tuples (id, deadline, profit)
    returns: (selected_job_ids_in_order, total_profit)
    """
    jobs_sorted = sorted(jobs, key=lambda x: x[2], reverse=True)
    max_deadline = max((d for _, d, _ in jobs), default=0)
    slots = [None] * (max_deadline + 1)  # 1..max_deadline
    result = []
    total_profit = 0
    for jid, dead, profit in jobs_sorted:
        for t in range(min(max_deadline, dead), 0, -1):
            if slots[t] is None:
                slots[t] = jid
                result.append((t, jid, profit))
                total_profit += profit
                break
    result.sort()
    selected_ids = [jid for _, jid, _ in result]
    return selected_ids, total_profit
