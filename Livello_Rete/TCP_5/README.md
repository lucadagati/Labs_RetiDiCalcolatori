# Simulazione del Retransmission Timeout in TCP

Questa demo in Python simula il comportamento del Retransmission Timeout (RTO) in TCP, mostrando come il TCP adatta dinamicamente il suo timer di timeout in risposta alle condizioni della rete, come la perdita di pacchetti.

## Descrizione

Lo script simula una serie di tentativi di invio di pacchetti, con una probabilità casuale di perdita di pacchetti. Viene visualizzato come il RTO viene adattato - aumentando in risposta alla perdita di pacchetti e diminuendo quando i pacchetti vengono ricevuti con successo.

## Requisiti

- Python 3.x

## Uso

Per eseguire la demo, clona il repository e avvia lo script `simulate_tcp_rto.py`.

```bash
python simulate_tcp_rto.py
```
