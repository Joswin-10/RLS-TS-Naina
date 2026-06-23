import matplotlib.pyplot as plt

def plot_comparison(data):
    algorithms = [d["name"] for d in data]
    wt = [d["wt"] for d in data]
    tat = [d["tat"] for d in data]

    plt.plot(algorithms, wt, marker='o', label="Waiting Time")
    plt.plot(algorithms, tat, marker='o', label="Turnaround Time")

    plt.title("CPU Scheduling Comparison")
    plt.xlabel("Algorithms")
    plt.ylabel("Time")
    plt.legend()

    plt.show()