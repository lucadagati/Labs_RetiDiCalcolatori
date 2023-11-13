import socket

# Crea un socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Assegna un indirizzo IP e una porta
server_socket.bind(('localhost', 12346))

print("Server UDP in attesa di dati...")

# Riceve dati dal client
data, addr = server_socket.recvfrom(1024)
print(f"Dati ricevuti da {addr}: {data.decode()}")

# Chiudi il socket
server_socket.close()
