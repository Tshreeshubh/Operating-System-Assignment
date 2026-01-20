import os

filename = "os_demo.txt"

print(f"--- File Management Demo: {filename} ---")

# 1. CREATE & WRITE
# Opens file in 'write' mode. Creates it if it doesn't exist.
with open(filename, "w") as f:
    f.write("Operating Systems are cool.\n")
    print(f"[+] Created '{filename}' and wrote data.")

# 2. READ
# Opens file in 'read' mode to display content.
with open(filename, "r") as f:
    content = f.read()
    print(f"[R] Read content: {content.strip()}")

# 3. APPEND
# Opens file in 'append' mode to add data without erasing.
with open(filename, "a") as f:
    f.write("Adding a second line.")
    print(f"[+] Appended new line.")

# 4. VERIFY APPEND
with open(filename, "r") as f:
    print(f"[R] Updated content:\n---\n{f.read()}---")

# 5. DELETE
# Uses the OS system call to remove the file linkage.
if os.path.exists(filename):
    os.remove(filename)
    print(f"[-] Deleted '{filename}'.")
else:
    print(f"[!] File not found.")
