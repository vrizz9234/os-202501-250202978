def detect_deadlock(processes, wait_for):
    visited = set()
    stack = set()

    def dfs(p):
        if p in stack:
            return True
        if p in visited:
            return False

        visited.add(p)
        stack.add(p)

        for q in wait_for.get(p, []):
            if dfs(q):
                return True

        stack.remove(p)
        return False

    for p in processes:
        if dfs(p):
            return True

    return False


# ====== CONTOH PEMANGGILAN ======
processes = ["P1", "P2", "P3"]

wait_for = {
    "P1": ["P2"],
    "P2": ["P1"],
    "P3": []
}

if detect_deadlock(processes, wait_for):
    print("DEADLOCK TERDETEKSI")
else:
    print("TIDAK TERJADI DEADLOCK")
