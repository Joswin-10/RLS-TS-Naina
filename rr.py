from collections import deque

def round_robin(processes, quantum):
    time = 0
    queue = deque(processes)

    while queue:
        p = queue.popleft()

        if p.burst_time > quantum:
            time += quantum
            p.burst_time -= quantum
            queue.append(p)
        else:
            time += p.burst_time
            p.burst_time = 0
            p.completion_time = time
            p.turnaround_time = p.completion_time - p.arrival_time
            p.waiting_time = p.turnaround_time  # simplified for now

    return processes
