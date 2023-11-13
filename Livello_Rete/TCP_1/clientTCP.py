import socket

# Crea un socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connettiti al server
client_socket.connect(('localhost', 12345))

# Invia dati al server
client_socket.sendall(b'Ciao, sono il client TCP!')

# Chiudi la connessione
client_socket.close()
