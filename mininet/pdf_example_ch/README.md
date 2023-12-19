sercizio 1: Test di Connettività
Ping tra Hosts: Usa il comando ping per testare la connettività tra gli host h1 e h2.

Comando: mininet> h1 ping h2
Aspettativa: Dovrebbero esserci risposte ping senza perdita di pacchetti.
Pingall Command: Esegui il comando pingall in Mininet per verificare la connettività tra tutti gli host nella rete.

Comando: mininet> pingall
Aspettativa: Tutti gli host dovrebbero essere in grado di pingarsi reciprocamente senza perdite.
Esercizio 2: Analisi del Traffico con Wireshark
Cattura del Traffico: Avvia Wireshark sul tuo computer host e inizia a catturare i pacchetti sulle interfacce dei switch (ad esempio, s1-eth1 e s1-eth2).
Genera Traffico: Utilizza ping o altri strumenti per generare traffico di rete.
Analizza i Pacchetti: Osserva i pacchetti in Wireshark e identifica i pacchetti ICMP generati dal ping.
Aspettativa: Dovresti vedere pacchetti ICMP Echo Request e Echo Reply.
Esercizio 3: Configurazione e Test delle Interfacce
Controllo delle Interfacce di Rete: Usa il comando ifconfig su entrambi gli host per visualizzare le loro interfacce di rete e i relativi indirizzi IP.

Comandi:
mininet> h1 ifconfig
mininet> h2 ifconfig
Aspettativa: Dovresti vedere le interfacce e gli indirizzi IP assegnati.
Modifica Configurazione IP: Cambia l'indirizzo IP di uno degli host e verifica se il ping funziona ancora.

Comandi:
mininet> h1 ifconfig h1-eth0 10.0.0.3 netmask 255.255.255.0
mininet> h1 ping h2
Esercizio 4: Analisi delle Prestazioni di Rete
Test di Velocità: Utilizza strumenti come iperf per testare la velocità della rete tra i due host.

Comandi:
Su h1 (server): mininet> h1 iperf -s
Su h2 (client): mininet> h2 iperf -c 10.0.0.1
Aspettativa: Dovresti vedere un report sulla velocità di trasferimento dati.
Test di Latenza: Misura la latenza tra gli host usando il comando ping con diverse dimensioni di pacchetto.

Comando: mininet> h1 ping -s [dimensione] h2
Questi esercizi offrono una panoramica di base sulle funzionalità e sulle potenzialità di Mininet per testare e analizzare topologie di rete. Puoi espandere questi esercizi o renderli più complessi modificando la topologia di rete o introducendo nuovi scenari di rete.
