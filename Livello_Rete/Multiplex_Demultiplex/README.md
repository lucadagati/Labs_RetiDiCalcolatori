# Demo di Multiplexing e Demultiplexing nel Livello di Trasporto ISO/OSI

## Panoramica
Questa demo illustra il concetto di multiplexing e demultiplexing nel livello di trasporto dello stack ISO/OSI, che è fondamentale per garantire una comunicazione end-to-end efficace tra le applicazioni eseguite su diversi sistemi.

### Multiplexing
Nel livello di trasporto dello stack ISO/OSI, il multiplexing permette di trasmettere dati da diverse applicazioni (o processi) attraverso la stessa connessione di rete. Ciò significa che il livello di trasporto può ricevere dati da più applicazioni su un singolo sistema terminale, come un computer, e incapsularli in segmenti o datagrammi per la trasmissione attraverso la rete. Questo processo consente un uso efficiente delle risorse di rete, poiché più sessioni di comunicazione possono condividere la stessa connessione fisica.

### Demultiplexing
Il demultiplexing è il processo inverso del multiplexing. Quando i dati arrivano al sistema terminale destinatario, il livello di trasporto determina a quale applicazione (o processo) consegnare i dati, esaminando gli header dei segmenti o dei datagrammi ricevuti. Questi header contengono informazioni, come i numeri di porta, che aiutano a identificare il processo destinatario corretto.

## Componenti della Demo

### Server
Il server simula il sistema terminale destinatario. Esso:
- Ascolta su una porta specifica.
- Utilizza il demultiplexing per determinare a quale "processo" virtuale consegnare i dati ricevuti.

### Client
I client simulano i sistemi terminali sorgente. Ogni client:
- Rappresenta un processo diverso che invia dati al server.
- Include informazioni nei dati inviati che permettono al server di identificare il processo di destinazione.

### Multiplexing dei Dati
- I dati di tutti i client vengono inviati attraverso la stessa connessione di rete al server.

### Demultiplexing al Server
- Il server esamina i dati ricevuti per determinare a quale processo virtuale consegnarli.

