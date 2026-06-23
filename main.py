from process import Process
from fcfs import fcfs
from sjf import sjf
from rr import round_robin
from utils import calculate_average
from graph import plot_comparison
import copy


def print_result(name, processes):
    print(f"\n{name} Results:\n")

    for p in processes:
        print(f"{p.pid} | WT={p.waiting_time} | TAT={p.turnaround_time}")

    avg_wt, avg_tat = calculate_average(processes)

    print("Average WT:", avg_wt)
    print("Average TAT:", avg_tat)


# ---------------- SAMPLE DATA ----------------
process_list = [
    Process("P1", 0, 5),
    Process("P2", 1, 3),
    Process("P3", 2, 2),
]

# ---------------- RUN ALL ----------------
p1 = copy.deepcopy(process_list)
p2 = copy.deepcopy(process_list)
p3 = copy.deepcopy(process_list)

print_result("FCFS", fcfs(p1))
print_result("SJF", sjf(p2))
print_result("Round Robin", round_robin(p3, 2))

# ---------------- COMPARISON TABLE ----------------
print("\n📊 FINAL COMPARISON TABLE\n")
print("Algorithm | Avg WT | Avg TAT")
print("-----------------------------")

data = []

for name, proc in [
    ("FCFS", fcfs(copy.deepcopy(process_list))),
    ("SJF", sjf(copy.deepcopy(process_list))),
    ("RR", round_robin(copy.deepcopy(process_list), 2))
]:
    wt, tat = calculate_average(proc)

    print(f"{name} | {wt:.2f} | {tat:.2f}")

    data.append({
        "name": name,
        "wt": wt,
        "tat": tat
    })

# ---------------- GRAPH ----------------
plot_comparison(data)