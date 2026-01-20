import threading
import time

# Shared resource
database_value = 0

# Create Lock (Mutex)
db_lock = threading.Lock()

def update_database(thread_name):
    global database_value
    
    print(f"[{thread_name}] trying to acquire lock...")
    
    # Acquire Lock
    # Blocks here if another thread has the lock
    with db_lock:
        print(f"[{thread_name}] lock acquired. Processing...")
        
        # Critical Section
        # Simulate read/write delay
        local_copy = database_value
        local_copy += 1
        time.sleep(0.5) 
        database_value = local_copy
        
        print(f"[{thread_name}] updated value to {database_value}")
        
    # Release Lock
    # Automatically happens when exiting 'with' block
    print(f"[{thread_name}] lock released.")

print("--- Threading & Sync Demo ---")

threads = []

# Create Threads
for i in range(3):
    t_name = f"Thread-{i+1}"
    t = threading.Thread(target=update_database, args=(t_name,))
    threads.append(t)

# Start Threads
for t in threads:
    t.start()

# Wait for Threads
# Main program pauses until all threads are done
for t in threads:
    t.join()

print(f"--- Final Value: {database_value} ---")
