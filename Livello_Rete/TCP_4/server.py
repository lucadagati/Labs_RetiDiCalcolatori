import socket
import datetime
import time

def current_time():
    return datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]

def terminate_connection(conn):
    print(f"{current_time()} - Server: Ricevuto FIN dal client.")
    time.sleep(0.1)  # Ritardo artificiale
    
    print(f"{current_time()} - Server: Invio ACK al client.")
    conn.send(b'ACK')
    time.sleep(0.1)  # Ritardo artificiale

    print(f"{current_time()} - Server: Invio FIN al client.")
    conn.send(b'FIN')
    time.sleep(0.1)  # Ritardo artificiale
    
    print(f"{current_time()} - Server: Aspetto l'ACK finale dal client.")
    if conn.recv(1024) == b'ACK':
        print(f"{current_time()} - Server: Ricevuto ACK finale dal client. Connessione chiusa.")
    conn.close()

# Creazione e configurazione del socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen()

# Accetta connessione dal client
conn, addr = server_socket.accept()
print(f"{current_time()} - Server: Connessione stabilita con {addr}")

# Funzione per terminare la connessione
terminate_connection(conn)

# Chiude il server socket
server_socket.close()
