import socket

def start_udp_server(port, file_to_save):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('', port))
    print(f"UDP Server listening on port {port}")

    with open(file_to_save, 'wb') as f:
        while True:
            data, addr = server_socket.recvfrom(1024)
            if not data:
                break
            f.write(data)
        conn.close()

start_udp_server(12346, 'received_udp_file')
