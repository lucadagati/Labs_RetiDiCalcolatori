import socket

def start_tcp_server(port, file_to_save):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', port))
    server_socket.listen(1)
    print(f"TCP Server listening on port {port}")

    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    with open(file_to_save, 'wb') as f:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            f.write(data)

    conn.close()

start_tcp_server(12345, 'received_tcp_file')
