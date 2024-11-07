# tcp_client.py
import socket
import time

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 9999))
    print("Connesso al server TCP.")

    window_size = 1024  # Dimensione iniziale della finestra in bytes
    max_window_size = 8192  # Dimensione massima della finestra
    increment = 512  # Incremento per la finestra

    while window_size <= max_window_size:
        try:
            # Invia pacchetto di dimensione pari a window_size
            client_socket.sendall(b'x' * window_size)
            print(f"Inviato pacchetto di {window_size} bytes.")
            
            # Attende l'ACK
            client_socket.settimeout(2)
            ack = client_socket.recv(1024)
            if ack == b'ACK':
                print("ACK ricevuto. Aumento della finestra.")
                window_size += increment
            else:
                print("ACK non ricevuto. Riduzione della finestra.")
                window_size = max(1024, window_size - increment)

            time.sleep(1)  # Pausa per osservare meglio le dinamiche

        except socket.timeout:
            print("Timeout! Riduzione della finestra.")
            window_size = max(1024, window_size - increment)

    client_socket.close()
    print("Connessione chiusa.")

if __name__ == "__main__":
    start_client()
