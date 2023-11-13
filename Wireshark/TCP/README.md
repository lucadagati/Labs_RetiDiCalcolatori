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

## 1. Indirizzo IP e Porta TCP del Computer Client
- IP: `192.168.1.102`
- Porta TCP: `1161`

## 2. Indirizzo IP e Porta TCP di gaia.cs.umass.edu
- IP: `128.119.245.12`
- Porta TCP: `80`

## 3. Numero di Sequenza del Segmento TCP SYN
- Numero di sequenza: `0`
- Identificato come SYN: flag SYN impostato su `1`

## 4. Numero di Sequenza del Segmento SYNACK di gaia.cs.umass.edu
- Numero di sequenza: `0`
- Campo ACK: `1` (determinato sommando `1` al numero di sequenza iniziale del segmento SYN del client)

## 5. Numero di Sequenza del Segmento TCP con il Comando HTTP POST
- Numero di sequenza: `1`

## 6. Numeri di Sequenza dei Primi Sei Segmenti nel Collegamento TCP
- Variano da `1` a `6406`
- Tempi di invio e ricezione degli ACK specificati per ciascun segmento

## 7. Lunghezza dei Primi Sei Segmenti TCP
- Primo segmento (HTTP POST): `565 byte`
- Altri cinque segmenti: `1460 byte` ciascuno

## 8. Spazio Buffer Minimo Disponibile e Controllo del Mittente
- Spazio buffer minimo: `5840 byte`
- Nessuna limitazione del mittente per mancanza di spazio nel buffer del ricevente

## 9. Segmenti Ritrasmessi nel File di Traccia
- Nessun segmento ritrasmesso, verificato tramite i numeri di sequenza

## 10. Dati Riconosciuti in un ACK
- Variabilità nei numeri di sequenza riconosciuti, con casi di riconoscimento di ogni altro segmento ricevuto

## 11. Throughput della Connessione TCP
- Throughput: circa `30.222 KByte/sec`

## 12. Fasi di Slow Start e Congestion Avoidance di TCP
- Inizio Slow Start: all'inizio della connessione
- Non è possibile determinare con precisione la fine della Slow Start e l'inizio della Congestion Avoidance
"""

