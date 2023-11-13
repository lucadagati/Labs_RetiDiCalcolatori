# Demo: Gestione di Connessioni Multiple con Threading in TCP

## Introduzione
Questa demo mostra come gestire connessioni multiple contemporaneamente in un server TCP utilizzando il threading in Python. Il server TCP è configurato per avviare un nuovo thread per ogni connessione client, permettendo così la gestione simultanea di più client.

## Server TCP con Threading
Nel server TCP con threading, ogni volta che un client si connette, viene creato un nuovo thread che gestisce la comunicazione con quel client. Ciò consente al server di continuare ad accettare altre connessioni senza interruzioni.

### Implementazione
- Il server TCP viene avviato e messo in ascolto su un indirizzo IP e una porta specificati.
- Quando un client si connette, il server accetta la connessione e avvia un nuovo thread passando la connessione del client alla funzione `handle_client`.
- La funzione `handle_client` gestisce la comunicazione con il client. Riceve i dati inviati dal client, li stampa e li reinvia al client.
- Se non ci sono dati in arrivo (connessione chiusa), il thread si conclude e chiude la connessione con il client.

## Client TCP
Il client TCP rimane invariato rispetto agli esempi precedenti. Per testare la gestione delle connessioni multiple, è possibile eseguire più istanze del client.

### Test
- Avvia lo script del server TCP in un terminale.
- Esegui multiple istanze dello script del client in terminali separati.
- Osserva come il server gestisce le connessioni multiple contemporaneamente.

## Note
Questo esempio dimostra l'efficacia del threading nella gestione di connessioni multiple in un ambiente di rete, un aspetto cruciale per la scalabilità dei server in ambienti reali.
