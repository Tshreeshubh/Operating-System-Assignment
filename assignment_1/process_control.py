import os
import sys
import time

def simple_process_demo():
    print(f"Parent Process (PID: {os.getpid()}) starting...")

    try:
        # 1. CREATE (FORK)
        # We copy the current process. 
        # 'pid' becomes 0 in the new Child, and the Child's actual PID in the Parent.
        pid = os.fork()
    except OSError as e:
        sys.exit(f"Failed to create process: {e}")

    if pid == 0:
        # --- CHILD PROCESS ---
        print(f"   [Child] I am the new process (PID: {os.getpid()}).")
        print("   [Child] waiting 2 seconds...")
        time.sleep(2)
        
        # 2. EXECUTE
        # We replace this python program with the system 'date' command.
        # This completely wipes the memory of the child process and loads the new tool.
        print("   [Child] Replacing myself with the 'date' command now!")
        os.execlp('date', 'date')
        
    else:
        # --- PARENT PROCESS ---
        print(f"Parent created child with PID: {pid}")
        print("Parent is waiting for child to finish...")
        
        # 3. WAIT
        # The parent blocks here until the child finishes.
        child_pid, status = os.wait()
        
        print(f"Parent: Child {child_pid} has finished. Continuing main task.")

if __name__ == "__main__":
    simple_process_demo()
