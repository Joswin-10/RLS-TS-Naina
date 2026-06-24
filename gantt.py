import os
import matplotlib.pyplot as plt

def plot_gantt(processes, algo_name):

    if not os.path.exists("static"):
        os.makedirs("static")

    fig, ax = plt.subplots(figsize=(8, 3))

    for p in processes:
        ax.barh(1, p.burst_time, left=p.start_time, edgecolor="black")
        ax.text(p.start_time + p.burst_time/2, 1, p.pid,
                ha='center', va='center')

    ax.set_yticks([])
    ax.set_xlabel("Time")
    ax.set_title(f"Gantt Chart - {algo_name.upper()}")

    plt.tight_layout()
    plt.savefig("static/gantt.png")
    plt.close()