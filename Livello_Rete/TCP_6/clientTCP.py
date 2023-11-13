import socket
import time

def start_tcp_client(server_ip, port, file_to_send):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, port))

    with open(file_to_send, 'rb') as f:
        start_time = time.time()
        while True:
            bytes_read = f.read(1024)
            if not bytes_read:
                break
            client_socket.sendall(bytes_read)

    end_time = time.time()
    print(f"File sent in {end_time - start_time} seconds.")
    client_socket.close()

start_tcp_client("127.0.0.1", 12345, 'your_file_to_send')
