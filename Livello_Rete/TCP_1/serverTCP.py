import socket

# Crea un socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Assegna un indirizzo IP e una porta
server_socket.bind(('localhost', 12345))

# Ascolta le connessioni in entrata
server_socket.listen()

print("Server TCP in attesa di connessioni...")

# Accetta una connessione
client_socket, addr = server_socket.accept()
print(f"Connessione da {addr}")

# Riceve dati dal client
data = client_socket.recv(1024)
print(f"Dati ricevuti: {data.decode()}")

# Chiudi la connessione
client_socket.close()
server_socket.close()
