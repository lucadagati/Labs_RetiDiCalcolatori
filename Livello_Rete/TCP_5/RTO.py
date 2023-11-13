import random
import time

def simulate_tcp_rto():
    # Impostazioni iniziali
    rto = 1  # Timeout iniziale (secondi)
    max_rto = 10  # RTO massimo
    ack_received = True

    for i in range(10):  # Simula 10 tentativi di invio
        print(f"Tentativo {i+1}: RTO corrente = {rto}s")

        # Simula l'invio di un pacchetto
        if random.random() < 0.3:  # 30% probabilità di perdita del pacchetto
            ack_received = False
            print("  Pacchetto perso. Attendere per RTO prima della ritrasmissione...")
        else:
            ack_received = True
            print("  Pacchetto ricevuto correttamente.")

        # Gestione RTO
        if not ack_received:
            rto = min(rto * 2, max_rto)  # Raddoppia RTO, fino al massimo
        else:
            rto = max(1, rto / 2)  # Riduce RTO, con un minimo di 1 secondo

        time.sleep(rto)  # Simula l'attesa per il prossimo tentativo di invio

simulate_tcp_rto()
