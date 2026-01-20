import socket

# --- CONFIGURATION ---
UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(f"UDP Client targeting {UDP_IP}:{UDP_PORT}")
print("Type your message and press Enter (type 'exit' to quit):")

while True:
    try:
        msg = input("You: ")
        if msg == "exit": break
        
        # Send via UDP
        sock.sendto(msg.encode(), (UDP_IP, UDP_PORT))
        
    except KeyboardInterrupt:
        break

sock.close()
