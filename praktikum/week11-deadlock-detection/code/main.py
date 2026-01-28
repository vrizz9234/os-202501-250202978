import csv
import os


def read_dataset(filename):
    processes = {}
    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            processes[row['Process']] = {
                'alloc': row['Allocation'],
                'req': row['Request']
            }
    return processes


def detect_deadlock(processes):
    wait_for = {}

    # Build wait-for graph
    for p1 in processes:
        wait_for[p1] = []
        for p2 in processes:
            if processes[p1]['req'] == processes[p2]['alloc']:
                wait_for[p1].append(p2)

    visited = set()
    rec_stack = []

    def has_cycle(process):
        visited.add(process)
        rec_stack.append(process)

        for neighbor in wait_for.get(process, []):
            if neighbor not in visited:
                if has_cycle(neighbor):
                    return True
            elif neighbor in rec_stack:
                return True

        rec_stack.pop()
        return False

    for process in processes:
        if process not in visited:
            if has_cycle(process):
                return True, rec_stack.copy()

    return False, []


# ================= MAIN PROGRAM =================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
dataset_file = os.path.join(BASE_DIR, "dataset_deadlock.csv")

processes = read_dataset(dataset_file)
deadlock, deadlocked_processes = detect_deadlock(processes)

print("=== HASIL DETEKSI DEADLOCK ===")
if deadlock:
    print("Deadlock terdeteksi!")
    print("Proses yang terlibat:", ", ".join(deadlocked_processes))
else:
    print("Tidak terjadi deadlock.")
