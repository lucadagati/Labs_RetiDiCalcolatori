# TCP Congestion Control Simulation

Questa demo in Python simula gli algoritmi di controllo della congestione TCP, tra cui Tahoe, Reno e NewReno. Lo scopo è fornire una comprensione visuale del comportamento della finestra di congestione sotto diverse condizioni di rete.

## Descrizione

La simulazione visualizza come la finestra di congestione (Congestion Window, CWND) cambia nel tempo in risposta alla ricezione degli ACK e alla rilevazione delle perdite di pacchetti. Questa demo include una semplice rappresentazione degli algoritmi TCP Tahoe, Reno e NewReno.

## Requisiti

- Python 3.x
- Matplotlib (installabile tramite `pip install matplotlib`)

## Uso

Per eseguire la simulazione, clona il repository e avvia lo script `tcp_congestion_control_simulation.py`.

```bash
python tcp_congestion_control_simulation.py
```

