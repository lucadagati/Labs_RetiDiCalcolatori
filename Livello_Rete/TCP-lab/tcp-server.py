# tcp_server.py
import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 9999))
    server_socket.listen(1)
    print("Server TCP in ascolto sulla porta 9999...")

    conn, addr = server_socket.accept()
    print(f"Connessione stabilita con {addr}")

    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(f"Ricevuto pacchetto di {len(data)} bytes.")
        conn.sendall(b'ACK')  # Invia un ACK come risposta

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
