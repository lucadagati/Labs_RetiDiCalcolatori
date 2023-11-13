import matplotlib.pyplot as plt

def simulate_tcp_congestion_control(algorithm):
    cwnd = 1  # Inizializza la finestra di congestione (Congestion Window)
    cwnd_history = [cwnd]
    threshold = 10  # Soglia iniziale
    ack_received = True  # Assumi che l'ACK sia ricevuto correttamente all'inizio

    for i in range(1, 100):
        if ack_received:
            if cwnd < threshold:
                cwnd *= 2  # Crescita esponenziale (Slow Start)
            else:
                if algorithm == 'tahoe':
                    cwnd += 1  # Crescita lineare (Congestion Avoidance)
                elif algorithm == 'reno' or algorithm == 'newreno':
                    cwnd += 1 / cwnd  # Crescita additiva (Congestion Avoidance)

        # Simula una perdita di pacchetto ogni 20 cicli
        if i % 20 == 0:
            ack_received = False

        if not ack_received:
            if algorithm == 'tahoe':
                cwnd = 1  # Reset di cwnd a 1
            elif algorithm == 'reno':
                cwnd /= 2  # Riduzione della cwnd a metà
            elif algorithm == 'newreno':
                cwnd = cwnd / 2 + 3  # Riduzione della cwnd e buffer di 3 pacchetti
            threshold = cwnd  # Aggiorna la soglia
            ack_received = True  # Resetta la condizione dell'ACK

        cwnd_history.append(cwnd)

    return cwnd_history

# Simula e visualizza
plt.figure(figsize=(12, 6))
plt.plot(simulate_tcp_congestion_control('tahoe'), label='Tahoe')
plt.plot(simulate_tcp_congestion_control('reno'), label='Reno')
plt.plot(simulate_tcp_congestion_control('newreno'), label='NewReno')
plt.title("Simulazione Controllo della Congestione TCP")
plt.xlabel("Cicli")
plt.ylabel("Dimensione Finestra di Congestione (CWND)")
plt.legend()
plt.show()
