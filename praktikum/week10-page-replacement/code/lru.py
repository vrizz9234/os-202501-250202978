def lru_page_replacement(reference, frames):
    memory = []
    page_faults = 0
    recent = {}

    print("\nLRU Simulation")
    for i, page in enumerate(reference):
        if page not in memory:
            page_faults += 1
            if len(memory) < frames:
                memory.append(page)
            else:
                lru_page = min(recent, key=recent.get)
                memory[memory.index(lru_page)] = page
                del recent[lru_page]
            status = "Page Fault"
        else:
            status = "Page Hit"

        recent[page] = i
        print(f"Page: {page} -> Memory: {memory} ({status})")

    return page_faults