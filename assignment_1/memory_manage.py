import math

class MemorySimulator:
    def __init__(self, total_size, page_size):
        self.page_size = page_size
        self.num_frames = total_size // page_size
        # Memory map: None = Empty, String = Process ID
        self.memory = [None] * self.num_frames
        print(f"--- Init Memory: {total_size}KB Total, {page_size}KB Pages ---")

    def allocate(self, process_id, size):
        # 1. PAGING CALCULATION
        # Calculate needed pages (ceiling division)
        pages_needed = math.ceil(size / self.page_size)
        
        # Check for free frames
        free_frames = [i for i, x in enumerate(self.memory) if x is None]
        
        if len(free_frames) < pages_needed:
            print(f"[!] Fail: Not enough memory for {process_id}")
            return

        # 2. ALLOCATION
        # Assign pages to the first available frames (non-contiguous)
        print(f"[+] Allocating {process_id} ({size}KB) -> Needs {pages_needed} pages")
        
        for i in range(pages_needed):
            frame_index = free_frames[i]
            self.memory[frame_index] = process_id # Write to memory
            print(f"    Page {i} -> Frame {frame_index}")

        # 3. FRAGMENTATION CHECK
        # Internal fragmentation happens in the last page
        used_space = size
        allocated_space = pages_needed * self.page_size
        fragmentation = allocated_space - used_space
        print(f"    Internal Fragmentation: {fragmentation}KB wasted")

    def deallocate(self, process_id):
        print(f"[-] Deallocating {process_id}...")
        # Clear frames matching the ID
        for i in range(self.num_frames):
            if self.memory[i] == process_id:
                self.memory[i] = None

    def display_map(self):
        print("    [Memory Map]: ", end="")
        # Visual representation of frames
        map_str = [pid if pid else "." for pid in self.memory]
        print(map_str)

# --- Simulation Run ---
sim = MemorySimulator(total_size=50, page_size=10)

# 1. Allocate Process A
# 25KB needs 3 pages (10+10+5). 5KB wasted.
sim.allocate("A", 25)
sim.display_map()

# 2. Allocate Process B
sim.allocate("B", 10)
sim.display_map()

# 3. Deallocate A to create holes
sim.deallocate("A")
sim.display_map()

# 4. Allocate Process C
# Demonstrates Paging: C fills the gaps left by A
sim.allocate("C", 20)
sim.display_map()
