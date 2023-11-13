# Laboratorio UDP con Wireshark

## Introduzione
In questo laboratorio, esploreremo il protocollo di trasporto UDP, un protocollo essenziale e senza fronzoli. L'UDP è semplice e diretto, il che ci permette di coprirlo rapidamente in questo laboratorio. Questo è ideale per chi ha limitazioni di tempo.

## Obiettivo
Diventare esperti nell'uso di Wireshark per analizzare il traffico UDP.

## Requisiti
- Conoscenza base di Wireshark.
- Connessione di rete attiva (o una traccia di pacchetti pre-registrata contenente pacchetti UDP).

## Attività
1. **Cattura di Pacchetti**
   - Avviare Wireshark e iniziare la cattura dei pacchetti.
   - Eseguire azioni che portino il tuo host a inviare e ricevere pacchetti UDP. Anche restando inattivi, è possibile catturare pacchetti UDP inviati da altri dispositivi sulla rete.

2. **Analisi dei Pacchetti UDP**
   - Interrompere la cattura dei pacchetti.
   - Impostare un filtro in Wireshark per mostrare solo i pacchetti UDP inviati e ricevuti dal tuo host.
   - Scegliere un pacchetto UDP e analizzarne i campi nell'intestazione UDP nella finestra dei dettagli.

## Esercizi
Dopo aver catturato e filtrato i pacchetti UDP, completare le seguenti attività:
1. **Analisi dell'Intestazione UDP**: Selezionare un pacchetto UDP e determinare il numero e il nome dei campi nell'intestazione UDP.
2. **Lunghezza dei Campi**: Determinare la lunghezza in byte di ciascun campo nell'intestazione UDP, utilizzando le informazioni visualizzate in Wireshark.
3. **Campo Lunghezza**: Capire a cosa si riferisce il valore nel campo Lunghezza e verificare con un pacchetto UDP catturato.
4. **Payload UDP Massimo**: Determinare il numero massimo di byte che possono essere inclusi in un payload UDP.
5. **Numero di Porta Sorgente Massimo**: Identificare il numero di porta sorgente più grande possibile.
6. **Numero di Protocollo per l'UDP**: Fornire il numero di protocollo per l'UDP in notazione esadecimale e decimale.
7. **Analisi di Coppie di Pacchetti UDP**: Esaminare una coppia di pacchetti UDP dove il primo è inviato dal tuo host e il secondo è una risposta al primo. Descrivere la relazione tra i numeri di porta nei due pacchetti.

## Suggerimenti per la Stampa dei Pacchetti
Per ogni domanda, è consigliato consegnare una stampa del/dei pacchetto/i usato/i per rispondere. Usare la funzione di stampa in Wireshark (File->Stampa) selezionando 'Solo pacchetto selezionato', 'Linea di riassunto del pacchetto', e i dettagli necessari per rispondere alle domande.


















































# Soluzioni - Analisi Pacchetti UDP con Wireshark

## 1. Campi dell'Intestazione UDP
- **Domanda**: Seleziona un pacchetto UDP dalla tua traccia e determina quanti e quali sono i campi nell'intestazione UDP.
- **Risposta**: L'intestazione UDP ha quattro campi: porta sorgente, porta destinazione, lunghezza e checksum.

## 2. Lunghezza dei Campi dell'Intestazione UDP
- **Domanda**: Determina la lunghezza (in byte) di ciascuno dei campi dell'intestazione UDP.
- **Risposta**: Ogni campo dell'intestazione UDP è lungo due byte.

## 3. Valore del Campo Lunghezza
- **Domanda**: Il valore nel campo Lunghezza si riferisce a cosa?
- **Risposta**: Il campo Lunghezza indica la lunghezza totale del segmento UDP, incluse intestazione e dati, misurata in byte. Nel pacchetto esaminato, la lunghezza è di 58 byte, con 8 byte di intestazione e 50 byte di dati.

## 4. Numero Massimo di Byte nel Payload UDP
- **Domanda**: Qual è il numero massimo di byte che possono essere inclusi in un payload UDP?
- **Risposta**: Dato che l'intestazione UDP usa 16 bit, la lunghezza massima di un segmento UDP (intestazione inclusa) è 65535 byte.

## 5. Numero di Porta Sorgente Massimo
- **Domanda**: Qual è il numero di porta sorgente più grande possibile?
- **Risposta**: Il numero massimo per una porta sorgente è 65535, derivante dai 16 bit utilizzati per rappresentare il numero di porta.

## 6. Numero di Protocollo per l'UDP
- **Domanda**: Qual è il numero di protocollo per l'UDP in notazione esadecimale e decimale?
- **Risposta**: Il numero di protocollo per l'UDP è 17, che in esadecimale si rappresenta con 0x11.

## 7. Relazione tra i Numeri di Porta in Coppie di Pacchetti UDP
- **Domanda**: Esamina una coppia di pacchetti UDP in cui il primo pacchetto è inviato dal tuo host e il secondo è una risposta al primo. Descrivi la relazione tra i numeri di porta nei due pacchetti.
- **Risposta**: La porta sorgente del primo pacchetto diventa la porta destinazione del secondo pacchetto e viceversa. Questo indica una comunicazione diretta tra i due host, dove il pacchetto di risposta è indirizzato esattamente all'host che ha inviato la richiesta.
