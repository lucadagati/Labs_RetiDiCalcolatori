import socket
import threading

def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(f"Dati ricevuti: {data.decode()}")
        client_socket.sendall(data)
    client_socket.close()

# Crea un socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen()
print("Server TCP in attesa di connessioni...")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Connessione da {addr}")
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()
