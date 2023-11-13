import socket
import threading
import json

# Server Code
def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(5)
    print("Server listening on port 12345")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr} has been established.")
        threading.Thread(target=handle_client, args=(client_socket,)).start()

def handle_client(client_socket):
    try:
        while True:
            # Reading the message length first
            msg_length = client_socket.recv(4)
            if not msg_length:
                break
            msg_length = int.from_bytes(msg_length, 'big')

            # Reading the message based on the length
            msg = client_socket.recv(msg_length)
            if not msg:
                break

            # Parsing the message and processing the header
            msg = json.loads(msg.decode('utf-8'))
            print(f"Received: {msg['data']} from client ID {msg['client_id']}")
            client_socket.send("Message received".encode('utf-8'))
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client_socket.close()

# Client Code
def client(id, message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    # Preparing the message with a custom header
    msg = json.dumps({"client_id": id, "data": message}).encode('utf-8')
    msg_length = len(msg).to_bytes(4, 'big')

    # Sending the length of the message first, then the message
    client_socket.sendall(msg_length)
    client_socket.sendall(msg)

    response = client_socket.recv(1024)
    print(f"Response from server: {response.decode('utf-8')}")
    client_socket.close()

# Starting the server in a new thread
server_thread = threading.Thread(target=server)
server_thread.start()

# Simulating multiple clients using threading
client_threads = []
messages = ["Hello from client 1", "Data from client 2", "Message from client 3"]
for i in range(1, 4):  # Three clients
    thread = threading.Thread(target=client, args=(i, messages[i-1]))
    client_threads.append(thread)
    thread.start()

# Joining the threads
for thread in client_threads:
    thread.join()

# This code simulates a more realistic scenario of multiplexing and demultiplexing.

