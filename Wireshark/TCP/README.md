# Analisi del Comportamento TCP con Wireshark

## Descrizione del Laboratorio
In questo laboratorio, ci concentreremo sull'analisi approfondita del comportamento del protocollo TCP (Transmission Control Protocol). Attraverso l'esame di una traccia di segmenti TCP inviati e ricevuti durante il trasferimento di un file di 150KB (contenente "Le avventure di Alice nel Paese delle Meraviglie" di Lewis Carroll) dal tuo computer a un server remoto, esploreremo vari aspetti chiave del protocollo TCP.

### Obiettivi Principali
- **Numeri di Sequenza e Conferma:** Studieremo come TCP utilizza questi numeri per garantire un trasferimento dati affidabile.
- **Controllo della Congestione:** Analizzeremo l'algoritmo di controllo della congestione di TCP, osservando in particolare le fasi di slow start ed evitamento della congestione.
- **Controllo del Flusso:** Esamineremo il meccanismo di controllo del flusso pubblicizzato dal ricevitore di TCP.
- **Prestazioni di Connessione:** Valuteremo le prestazioni della connessione TCP, includendo throughput e tempo di andata e ritorno (RTT).

Il laboratorio include anche una breve considerazione sull'allestimento della connessione TCP.

### File pcap
Nel repository, troverai il file pcap con il flusso TCP, già pulito e pronto per l'analisi.

## Guida all'Analisi con Wireshark

### Analisi dei Segmenti TCP
1. **Indirizzo IP e Numero di Porta TCP:** Determina l'indirizzo IP e il numero di porta TCP utilizzati dal computer client durante il trasferimento del file a gaia.cs.umass.edu.
2. **Indirizzo IP di gaia.cs.umass.edu:** Identifica l'indirizzo IP del server e su quale numero di porta sta inviando e ricevendo segmenti TCP.

### Comandi Specifici
- Per cambiare la visualizzazione in Wireshark e concentrarti sui segmenti TCP anziché sui messaggi HTTP, vai su `Analizza -> Protocolli Abilitati`, deseleziona la casella HTTP e premi OK.

### Domande di Laboratorio
Rispondi alle seguenti domande basandoti sulla traccia tcp-ethereal-trace-1 disponibile in [Wireshark Labs](http://gaia.cs.umass.edu/wireshark-labs/wireshark-traces.zip):
- Quali sono i numeri di sequenza dei primi sei segmenti TCP nella connessione, includendo il segmento contenente il comando HTTP POST?
- Qual è il valore RTT per ciascuno dei sei segmenti?
- Analizza la lunghezza di ciascuno dei primi sei segmenti TCP.
- Qual è la quantità minima di spazio buffer disponibile annunciato al ricevente per l'intera traccia?
- Ci sono stati dei segmenti ritrasmessi?
- Qual è la velocità di trasferimento per la connessione TCP?

### Controllo della Congestione TCP in Azione
Utilizza lo strumento di graficazione Grafico Sequenza-Tempo (Stevens) in Wireshark per analizzare la quantità di dati inviati per unità di tempo dal client al server. Questo ti aiuterà a identificare le fasi di slow start di TCP e di evitamento della congestione.

## Risorse Aggiuntive
- [Introduzione a Wireshark](https://www.wireshark.org)
- [Documentazione TCP](https://www.ietf.org/rfc/rfc793.txt)

## Contributi e Feedback
I tuoi contributi e feedback su questo laboratorio sono sempre ben accetti. Sentiti libero di aprire una issue o una pull request per qualsiasi suggerimento o correzione.


# Soluzioni - Analisi TCP con Wireshark

## TCP Basics

### 1. Indirizzo IP e Porta TCP del Computer Client
- **IP address**: `192.168.1.102`
- **TCP port number**: `1161`

### 2. Indirizzo IP e Porta TCP di gaia.cs.umass.edu
- **IP address**: `128.119.245.12`
- **TCP port number**: `80`

### 3. Numero di Sequenza del Segmento TCP SYN
- **Sequence number**: `0`
- **SYN flag**: Set to `1` (identifies the segment as a SYN segment)

### 4. Numero di Sequenza del Segmento SYNACK
- **Sequence number**: `0`
- **ACK field value**: `1` (calculated by adding `1` to the initial sequence number of the client's SYN segment)
- **SYN and ACK flags**: Both set to `1` (identifies the segment as a SYNACK segment)

### 5. Numero di Sequenza del Segmento TCP con il Comando HTTP POST
- **Sequence number**: `1`

### 6. Numeri di Sequenza dei Primi Sei Segmenti e RTT
- **Segment numbers in trace**: 1 – 6 as No. 4, 5, 7, 8, 10, and 11.
- **Sequence numbers**: `1`, `566`, `2026`, `3486`, `4946`, `6406`.
- **Send times, ACK receive times, and RTT values** detailed for each segment.
- **EstimatedRTT values** calculated using the formula: `EstimatedRTT = 0.875 * EstimatedRTT + 0.125 * SampleRTT`.

### 7. Lunghezza dei Primi Sei Segmenti TCP
- **First TCP segment (HTTP POST)**: `565 bytes`.
- **Other five segments**: `1460 bytes` each (MSS).

### 8. Spazio Buffer Minimo Disponibile e Controllo del Mittente
- **Minimum buffer space (receiver window)**: `5840 bytes`.
- **No sender throttling** due to lack of receiver buffer space.

### 9. Segmenti Ritrasmessi nel File di Traccia
- **No retransmitted segments**, verified by sequence number analysis.

### 10. Dati Riconosciuti in un ACK
- **Acknowledged sequence numbers and acknowledged data** listed for each ACK.
- **Identification of cases** where the receiver is ACKing every other received segment.

### 11. Throughput della Connessione TCP
- **Throughput**: Approximately `30.222 KByte/sec`.

### 12. Fasi di Slow Start e Congestion Avoidance di TCP
- **Start of TCP Slow Start**: At the beginning of the connection.
- **Identification of TCP slow start and congestion avoidance phases** is not precisely possible in this trace.
