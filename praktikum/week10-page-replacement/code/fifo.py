def fifo_page_replacement(reference, frames):
    memory = []
    page_faults = 0

    print("FIFO Simulation")
    for page in reference:
        if page not in memory:
            page_faults += 1
            if len(memory) < frames:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)
            status = "Page Fault"
        else:
            status = "Page Hit"

        print(f"Page: {page} -> Memory: {memory} ({status})")

    return page_faults