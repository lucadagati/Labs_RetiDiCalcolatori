import socket

# Crea un socket UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Invia dati al server
client_socket.sendto(b'Ciao, sono il client UDP!', ('localhost', 12346))

# Chiudi il socket
client_socket.close()
