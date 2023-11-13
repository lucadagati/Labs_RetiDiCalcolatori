# Demo TCP vs UDP in Python

Questa repository contiene una demo che illustra le differenze fondamentali tra i protocolli di trasmissione TCP (Transmission Control Protocol) e UDP (User Datagram Protocol) in Python. La demo consiste nel trasferimento di un file da un client a un server utilizzando entrambi i protocolli.

## Panoramica

TCP è un protocollo orientato alla connessione che offre varie funzionalità come la consegna affidabile dei dati, il controllo della congestione e la garanzia che i pacchetti arrivino in ordine. UDP, d'altra parte, è un protocollo non orientato alla connessione che permette la trasmissione di dati più veloce ma senza queste garanzie.

Questa demo mette in evidenza queste differenze tramite un semplice scenario di trasferimento di un file.

## Struttura del Progetto

Il progetto è strutturato come segue:

- `tcp_server.py`: Server TCP che riceve i dati e li salva in un file.
- `tcp_client.py`: Client TCP che legge un file e lo invia al server TCP.
- `udp_server.py`: Server UDP che riceve i dati e li salva in un file.
- `udp_client.py`: Client UDP che legge un file e lo invia al server UDP.
- `generate_file.py`: Script per generare un file di test di dimensioni predefinite (10 MB).

## Istruzioni per l'Uso

Per eseguire questa demo, seguire questi passi:

1. **Installare Python**: Assicurarsi di avere Python installato sul proprio sistema.
2. **Clonare la Repository**: Clonare questo repository sul proprio sistema.
3. **Generare il File di Test**: Eseguire `generate_file.py` per creare il file di test.
4. **Avviare il Server**: Eseguire `tcp_server.py` o `udp_server.py` per avviare il rispettivo server.
5. **Eseguire il Client**: Eseguire `tcp_client.py` o `udp_client.py` per inviare il file al server.

## Requisiti

- Python 3.x


