def fcfs(processes):
    time = 0

    for p in processes:
        if time < p.arrival_time:
            time = p.arrival_time

        p.completion_time = time + p.burst_time
        p.turnaround_time = p.completion_time - p.arrival_time
        p.waiting_time = p.turnaround_time - p.burst_time

        time = p.completion_time

    return processes
    return processes