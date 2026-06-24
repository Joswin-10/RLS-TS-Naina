from flask import Flask, render_template, request
from fcfs import fcfs
from sjf import sjf
from rr import round_robin
from process import Process
from gantt import plot_gantt
import copy

app = Flask(__name__)

# ---------------- GLOBAL PROCESS LIST ----------------
process_list = []


# ---------------- HOME PAGE ----------------
@app.route("/")
def home():
    return render_template("index.html")


# ---------------- INPUT PAGE ----------------
@app.route("/input")
def input_page():
    return render_template("input.html", processes=process_list)


# ---------------- ADD PROCESS ----------------
@app.route("/add", methods=["POST"])
def add_process():

    pid = request.form["pid"]
    arrival = int(request.form["arrival"])
    burst = int(request.form["burst"])

    process_list.append(Process(pid, arrival, burst))

    return render_template("input.html", processes=process_list)


# ---------------- RUN ALGORITHMS ----------------
@app.route("/run/<algo>")
def run_algo(algo):

    if len(process_list) == 0:
        return "⚠️ No processes added. Go to /input"

    p_list = copy.deepcopy(process_list)

    if algo == "fcfs":
        result = fcfs(p_list)
    elif algo == "sjf":
        result = sjf(p_list)
    elif algo == "rr":
        result = round_robin(p_list, 2)
    else:
        return "Invalid Algorithm"

    # Generate Gantt Chart
    plot_gantt(result, algo)

    return render_template(
        "result.html",
        processes=result,
        algo=algo
    )


# ---------------- RUN APP ----------------
if __name__ == "__main__":
    app.run(debug=True)