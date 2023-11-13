# Demo TCP e UDP in Python

## Introduzione
Questa demo dimostra l'uso pratico dei protocolli TCP (Transmission Control Protocol) e UDP (User Datagram Protocol) in Python. Il TCP è un protocollo orientato alla connessione che assicura la consegna affidabile dei dati, mentre l'UDP è un protocollo senza connessione che non garantisce la consegna dei dati.

## Demo 1: TCP (Transmission Control Protocol)
Il TCP stabilisce una connessione sicura e garantisce la consegna affidabile dei dati. La demo TCP è suddivisa in due parti: Creazione del Server TCP e Creazione del Client TCP.

### Passo 1: Creazione del Server TCP
Il server TCP viene configurato per ascoltare le connessioni in entrata su un indirizzo IP e una porta specificati. Riceve i dati dal client e li stampa.

### Passo 2: Creazione del Client TCP
Il client TCP si connette al server e invia un messaggio. Dopo l'invio dei dati, la connessione viene chiusa.

## Demo 2: UDP (User Datagram Protocol)
L'UDP invia dati senza stabilire una connessione, senza garanzie sulla consegna o sull'ordine dei dati. La demo UDP è divisa in Creazione del Server UDP e Creazione del Client UDP.

### Passo 1: Creazione del Server UDP
Il server UDP ascolta i dati in entrata su un indirizzo IP e una porta. Riceve i dati dal client e li stampa.

### Passo 2: Creazione del Client UDP
Il client UDP invia un messaggio al server UDP. Non viene stabilita alcuna connessione e non ci sono garanzie sulla consegna dei dati.

## Esecuzione delle Demo
- Esegui prima lo script del server in un terminale.
- In un altro terminale, esegui lo script del client corrispondente.
- Osserva l'output su entrambi i terminali per comprendere il flusso di comunicazione.

## Note
Questi esempi sono stati progettati per illustrare le differenze fondamentali tra i protocolli TCP e UDP in un contesto semplice e comprensibile.
