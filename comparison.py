data = []

for name, func in [
    ("FCFS", fcfs),
    ("SJF", sjf),
    ("RR", lambda p: round_robin(p, 2))
]:
    proc = func(copy.deepcopy(process_list))
    wt, tat = calculate_average(proc)

    data.append({"name": name, "wt": wt, "tat": tat})

plot_comparison(data)