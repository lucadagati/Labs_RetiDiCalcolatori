# Demo di Simulazione P2P con Docker

Questa demo illustra l'implementazione di una semplice rete peer-to-peer (P2P) utilizzando Docker e Python. Il sistema consiste in quattro nodi che comunicano tra loro in una rete P2P definita nel `docker-compose.yml`.

## Caratteristiche

- **Docker Compose**: Usa Docker Compose per gestire più container come un'unica entità.
- **Python 3.9**: Sfrutta le caratteristiche asincrone di Python per simulare un comportamento P2P.

## Prerequisiti

Per eseguire questa demo, assicurati di avere installato:

- Docker
- Docker Compose

## Struttura dei File

- `docker-compose.yml`: Configura i servizi Docker.
- `Dockerfile`: Definisce l'immagine Docker per i nodi della rete.
- `main.py`: Il codice Python eseguito in ogni nodo.

## Installazione e Esecuzione

Segui questi passaggi per avviare la demo:

1. **Clona il Repository**

   ```bash
   git clone [URL-del-tuo-repository]
   cd [nome-del-tuo-repository]
```

## Costruisci le Immagini Docker

   ```bash
docker-compose build
   ```

## Avvia i Container

   ```bash
docker-compose up
   ```

Dopo l'avvio, ogni nodo (container) nella rete P2P eseguirà il codice definito in main.py.

## Pulizia
Per fermare e rimuovere i container creati, usa:

   ```bash
docker-compose down
   ```


