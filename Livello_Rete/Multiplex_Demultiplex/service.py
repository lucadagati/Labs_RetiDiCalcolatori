import socket
import threading

# Server code
def server():
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to a public host, and a well-known port
    server_socket.bind(('localhost', 12345))
    server_socket.listen(5)
    
    print("Server listening on port 12345")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr} has been established.")

        threading.Thread(target=handle_client, args=(client_socket,)).start()

def handle_client(client_socket):
    while True:
        msg = client_socket.recv(1024)
        if not msg:
            break
        print(f"Received: {msg.decode('utf-8')} from the client")
        client_socket.send("Message received".encode('utf-8'))
    client_socket.close()

# Client code
def client(id):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    client_socket.send(f"Hello from client {id}".encode('utf-8'))
    response = client_socket.recv(1024)
    print(f"Response from server: {response.decode('utf-8')}")
    client_socket.close()

# Starting the server in a new thread
server_thread = threading.Thread(target=server)
server_thread.start()

# Starting multiple clients to simulate multiplexing
client_threads = []
for i in range(1, 4):  # Starting three clients
    thread = threading.Thread(target=client, args=(i,))
    client_threads.append(thread)
    thread.start()

# Joining the threads
for thread in client_threads:
    thread.join()

# This is a simple demo and does not handle exceptions or graceful termination for brevity.

