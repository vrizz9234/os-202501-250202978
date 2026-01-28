# scheduling_simulation.py
# Simulasi Penjadwalan CPU: FCFS dan SJF Non-Preemptive

# Dataset Proses (Arrival Time, Burst Time)
processes = [
    {"name": "P1", "arrival": 0, "burst": 6},
    {"name": "P2", "arrival": 1, "burst": 8},
    {"name": "P3", "arrival": 2, "burst": 7},
    {"name": "P4", "arrival": 3, "burst": 3},
]

def fcfs(processes):
    # Urutkan berdasarkan Arrival Time
    procs = sorted(processes, key=lambda x: x["arrival"])
    time = 0
    waiting_times = []
    turnaround_times = []

    print("=== FCFS Scheduling ===")
    print(f"{'Proses':<6} {'Arrival':<7} {'Burst':<5} {'Waiting':<7} {'Turnaround':<10}")
    for p in procs:
        start_time = max(time, p["arrival"])
        waiting_time = start_time - p["arrival"]
        turnaround_time = waiting_time + p["burst"]

        print(f"{p['name']:<6} {p['arrival']:<7} {p['burst']:<5} {waiting_time:<7} {turnaround_time:<10}")

        waiting_times.append(waiting_time)
        turnaround_times.append(turnaround_time)
        time = start_time + p["burst"]

    print(f"Rata-rata Waiting Time: {sum(waiting_times)/len(waiting_times):.2f}")
    print(f"Rata-rata Turnaround Time: {sum(turnaround_times)/len(turnaround_times):.2f}\n")


def sjf_non_preemptive(processes):
    procs = processes.copy()
    time = 0
    completed = []
    waiting_times = {}
    turnaround_times = {}

    print("=== SJF Non-Preemptive Scheduling ===")
    print(f"{'Proses':<6} {'Arrival':<7} {'Burst':<5} {'Waiting':<7} {'Turnaround':<10}")

    while procs:
        # Pilih proses yang sudah arrive dan burst time paling kecil
        available = [p for p in procs if p["arrival"] <= time]
        if not available:
            time += 1
            continue
        next_proc = min(available, key=lambda x: x["burst"])

        waiting_time = time - next_proc["arrival"]
        turnaround_time = waiting_time + next_proc["burst"]

        print(f"{next_proc['name']:<6} {next_proc['arrival']:<7} {next_proc['burst']:<5} {waiting_time:<7} {turnaround_time:<10}")

        waiting_times[next_proc["name"]] = waiting_time
        turnaround_times[next_proc["name"]] = turnaround_time

        time += next_proc["burst"]
        completed.append(next_proc)
        procs.remove(next_proc)

    print(f"Rata-rata Waiting Time: {sum(waiting_times.values())/len(waiting_times):.2f}")
    print(f"Rata-rata Turnaround Time: {sum(turnaround_times.values())/len(turnaround_times):.2f}\n")


# Main Program
if __name__ == "__main__":
    fcfs(processes)
    sjf_non_preemptive(processes)
