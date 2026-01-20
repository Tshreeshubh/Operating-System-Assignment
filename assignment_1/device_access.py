import os
import sys
import shutil

print("--- Device Access & I/O Demo ---")

# 1. LIST MOUNTED DRIVES (Mac & Linux Support)
drives = []

if sys.platform == "darwin":
    # macOS stores mounted drives in /Volumes
    print("[*] macOS detected. Scanning /Volumes...")
    volumes = os.listdir("/Volumes")
    
    # Add Root drive and External drives to list
    drives.append("/") 
    for v in volumes:
        drives.append(os.path.join("/Volumes", v))

elif os.path.exists("/proc/partitions"):
    # Linux specific check
    print("[*] Linux detected. Listing Block Devices...")
    with open("/proc/partitions", "r") as f:
        next(f); next(f) # Skip headers
        for line in f:
            parts = line.split()
            if parts: print(f"  Dev: {parts[3]} Size: {int(parts[2])//1024}MB")
    drives.append("/")

# 2. CHECK DISK USAGE
print("\n--- Disk Usage Details ---")

gb = 1024 ** 3

for path in drives:
    try:
        # Get stats for the specific path
        stat = shutil.disk_usage(path)
        
        print(f"Mount: {path}")
        print(f"  Total: {stat.total // gb} GB")
        print(f"  Used:  {stat.used // gb} GB")
        print(f"  Free:  {stat.free // gb} GB")
        print("-" * 20)
        
    except OSError:
        # Skip if system creates a ghost volume/permission error
        continue
