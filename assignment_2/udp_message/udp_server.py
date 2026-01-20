import socket
import pika

# --- CONFIGURATION ---
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
QUEUE_NAME = 'ipc_messages'

def start_server():
    # 1. CONNECT TO RABBITMQ
    # We establish the connection once so we don't have to reconnect for every message
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME)
    
    # 2. SETUP UDP LISTENER
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))

    print(f"[*] UDP Server listening on {UDP_PORT}")
    print(f"[*] Connected to RabbitMQ. Forwarding messages to queue: '{QUEUE_NAME}'")

    try:
        while True:
            # Wait for data from UDP Client
            data, addr = sock.recvfrom(1024)
            message = data.decode()
            
            # Publish to RabbitMQ
            channel.basic_publish(exchange='', routing_key=QUEUE_NAME, body=message)
            
            print(f" [✓] Received UDP: '{message}' -> Sent to RabbitMQ")
            
    except KeyboardInterrupt:
        print("\nClosing connection...")
        connection.close()
        sock.close()

if __name__ == "__main__":
    start_server()
