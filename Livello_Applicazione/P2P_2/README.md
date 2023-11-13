# Demo di Rete Peer-to-Peer (P2P) con Docker e Python

Questa demo illustra il funzionamento di base di una rete Peer-to-Peer (P2P) utilizzando Docker e Python. È destinata a scopi didattici e dimostra come i peer possono simulare lo scambio di parti di un file in un ambiente controllato.

## Panoramica

In questa demo, quattro peer simulano il download di parti di un file in una rete P2P. Ogni peer è eseguito in un container Docker e utilizza un semplice script Python per simulare lo scambio di dati.

## Prerequisiti

- Docker
- Docker Compose
- Conoscenza di base di Docker, Python e reti

## Installazione e Configurazione

### Passaggi per l'installazione:

1. Clona o scarica questo repository nella tua macchina locale.
2. Assicurati che Docker e Docker Compose siano installati e funzionanti sul tuo sistema.

### Struttura dei File:

- `peer.py`: Script Python per i peer.
- `docker-compose.yml`: File di configurazione per Docker Compose.
- `Dockerfile`: Dockerfile per costruire l'immagine del container.

## Esecuzione della Demo

Per eseguire la demo, segui questi passaggi:

1. **Costruzione delle Immagini Docker:**
   Apri un terminale nella directory del progetto e esegui:

   ```bash
   docker-compose build
   ```

2. **Avvio dei Container:**
Una volta completata la costruzione delle immagini, avvia i container con:
   ```bash
docker-compose up
   ```

3. **Monitoraggio:**
Osserva i log dei container per vedere la simulazione dello scambio di file.

4. **Ferma la Demo:**
Per arrestare tutti i container, usa:

   ```bash
docker-compose down
   ```
