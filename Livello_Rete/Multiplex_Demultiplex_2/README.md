# Demo Avanzata di Multiplexing e Demultiplexing in Rete

## Panoramica
Questa demo avanzata illustra il concetto di multiplexing e demultiplexing in un contesto di rete più realistico. Utilizziamo una singola connessione TCP per inviare messaggi da più client al server e implementiamo un meccanismo di header personalizzato per aiutare il server a distinguere tra i messaggi dei diversi client.

## Concetti Chiave

### Header Personalizzato
- Ogni messaggio inviato dai client include un header che identifica il mittente.

### Singola Connessione per Multiple Richieste
- Utilizziamo una singola connessione TCP per inviare messaggi da più "client" (processi diversi nella stessa applicazione client).

### Demultiplexing Basato su Header
- Il server esamina l'header di ciascun messaggio per determinare a quale processo interno inoltrare i dati.

## Codice Server e Client

### Codice Server
- Il server accetta connessioni, legge i messaggi e utilizza l'header per eseguire il demultiplexing.

### Codice Client
- Il client invia messaggi con un header personalizzato.
- Utilizziamo threading per simulare l'invio di messaggi da diversi client attraverso la stessa connessione.

## Dettagli Implementativi

### Server
- Si mette in ascolto sulla porta 12345.
- Avvia un nuovo thread per gestire ogni connessione ricevuta.
- Legge la lunghezza del messaggio e il messaggio stesso.
- Decodifica e analizza il messaggio per estrarre l'ID del client e eseguire il demultiplexing.
- Risponde al client dopo aver processato il messaggio.

### Client
- Stabilisce una connessione con il server.
- Prepara un messaggio JSON con un ID univoco e il contenuto del messaggio.
- Invia la lunghezza del messaggio seguita dal messaggio effettivo.
- Riceve e stampa la risposta dal server.

## Simulazione del Multiplexing e Demultiplexing
- **Multiplexing**: Usiamo diverse connessioni TCP per simulare l'invio di messaggi da diversi client, gestiti dallo stesso server.
- **Demultiplexing**: Il server utilizza l'ID del client nell'header per determinare la destinazione interna del messaggio.

