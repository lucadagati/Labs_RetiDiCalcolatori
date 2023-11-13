import socket
import datetime
import time

def current_time():
    return datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]

# Creazione del socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connessione al server
client_socket.connect(('localhost', 12345))

print(f"{current_time()} - Client: Inizia il processo di terminazione.")
time.sleep(0.1)  # Ritardo artificiale

print(f"{current_time()} - Client: Invio FIN al server.")
client_socket.send(b'FIN')
time.sleep(0.1)  # Ritardo artificiale

if client_socket.recv(1024) == b'ACK':
    print(f"{current_time()} - Client: Ricevuto ACK dal server.")
    time.sleep(0.1)  # Ritardo artificiale

if client_socket.recv(1024) == b'FIN':
    print(f"{current_time()} - Client: Ricevuto FIN dal server. Invio ACK finale.")
    client_socket.send(b'ACK')

client_socket.close()
print(f"{current_time()} - Client: Connessione chiusa.")
