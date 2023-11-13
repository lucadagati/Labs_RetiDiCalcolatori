import socket
import time

def start_udp_client(server_ip, port, file_to_send):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    with open(file_to_send, 'rb') as f:
        start_time = time.time()
        while True:
            bytes_read = f.read(1024)
            if not bytes_read:
                break
            client_socket.sendto(bytes_read, (server_ip, port))

    end_time = time.time()
    print(f"File sent in {end_time - start_time} seconds.")
    client_socket.close()

start_udp_client("127.0.0.1", 12346, 'your_file_to_send')
