import socket  # Importa il modulo socket per le comunicazioni di rete
import threading  # Importa il modulo threading per eseguire funzioni in parallelo
import sys  # Importa il modulo sys per accedere agli argomenti passati da riga di comando
import os  # Importa il modulo os per interagire con il sistema operativo

# Definisce una funzione per gestire la connessione con il client
def handle_client(client_socket):
    try:
        # Attendere la ricezione del nome del file dal client, 1024 è la dimensione del buffer
        file_name = client_socket.recv(1024).decode()
        # Apre il file in modalità lettura binaria
        with open(file_name, 'rb') as file:
            # Invia il file attraverso il socket
            client_socket.sendfile(file)
        # Stampa un messaggio di conferma quando il file è stato inviato
        print(f"File {file_name} inviato correttamente.")
    except Exception as e:
        # Stampa un messaggio di errore se qualcosa va storto durante l'invio del file
        print(f"Errore durante l'invio del file: {e}")
    finally:
        # Chiude il socket del client
        client_socket.close()

# Definisce una funzione che mantiene il server in ascolto per le connessioni in entrata
def server_loop(local_port):
    # Crea un socket TCP/IP
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Associa il socket a un indirizzo pubblico e alla porta specificata
    server.bind(('0.0.0.0', local_port))
    # Imposta il server per ascoltare le connessioni in entrata, con un massimo di 5 connessioni in coda
    server.listen(5)
    # Stampa un messaggio che indica che il server è in ascolto
    print(f'Ascolto come server sulla porta {local_port}')

    # Loop infinito per accettare connessioni in continuazione
    while True:
        # Accetta una connessione in entrata
        client_sock, addr = server.accept()
        # Stampa l'indirizzo del client connesso
        print(f'Accettata connessione da: {addr}')
        # Crea un nuovo thread per gestire la connessione del client
        client_handler = threading.Thread(target=handle_client, args=(client_sock,))
        # Avvia il thread
        client_handler.start()

# Definisce la funzione principale che dirige il comportamento del nodo
def main(mode, file_name=None, target_host=None, target_port=None):
    # Controlla se il nodo deve comportarsi come server
    if mode == 'server':
        # Imposta la porta locale dalla riga di comando e avvia il server loop
        local_port = int(sys.argv[2])
        server_loop(local_port)
    # Controlla se il nodo deve comportarsi come client
    elif mode == 'client':
        # Crea un socket TCP/IP
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Si connette al server target
        client.connect((target_host, int(target_port)))
        # Invia il nome del file al server
        client.send(file_name.encode())
        # Apre il file in modalità scrittura binaria
        with open(file_name, 'wb') as file:
            # Riceve i dati del file dal server
            file_data = client.recv(1024)
            # Continua a ricevere i dati fino a che non ci sono più dati da ricevere
            while file_data:
                file.write(file_data)
                file_data = client.recv(1024)
        # Stampa un messaggio di conferma della ricezione del file
        print(f"Ricevuto file: {file_name}")
        # Chiude il socket del client
        client.close()

# Questo blocco viene eseguito se lo script è avviato direttamente da riga di comando
if __name__ == '__main__':
    # Controlla se il numero di argomenti corrisponde a un avvio come server
    if len(sys.argv) == 3:
        # Avvia il nodo come server
        main(sys.argv[1], sys.argv[2])
    # Controlla se il numero di argomenti corrisponde a un avvio come client
    elif len(sys.argv) == 5:
        # Avvia il nodo come client
        main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
