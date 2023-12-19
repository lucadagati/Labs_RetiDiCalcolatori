# Istruzioni per la Demo di Port Forwarding con Mininet

1. ## Avvio della Demo
   Prima di tutto, avvia lo script Mininet che hai preparato (`mininet_port_forwarding_demo.py`):
   ```bash
   sudo python mininet_port_forwarding_demo.py
   ```

2. ## Configurazione e Test del Server Web su Host1
   ### Avvio di un Server Web su Host1:
   In una finestra della CLI di Mininet, avvia un server web su Host1. Per esempio, con Python 3:
   ```bash
   h1 python3 -m http.server 80
   ```
   Questo server sarà ora in ascolto sulla porta 80 di Host1.

   ### Test del Server Web da Host1:
   Ancora nella CLI di Mininet, verifica che il server web su Host1 sia raggiungibile da se stesso:
   ```bash
   h1 curl localhost
   ```
   Dovresti vedere l'output HTML del server web.

3. ## Test del Port Forwarding dal Router a Host1
   ### Accesso al Server Web di Host1 da Host2 tramite il Router:
   Dato che il router reindirizza le richieste dalla porta 8080 alla porta 80 di Host1, prova a connetterti al server web da Host2:
   ```bash
   h2 curl 10.0.0.1:8080
   ```
   Questo comando dovrebbe restituire la stessa pagina web che hai visto quando hai testato Host1 direttamente. Questo conferma che il port forwarding funziona come previsto.

4. ## Verifica delle Regole iptables sul Router
   ### Controlla le Regole NAT sul Router:
   Per assicurarti che le regole di iptables siano configurate correttamente, puoi controllarle sul router:
   ```bash
   r0 iptables -t nat -L -v
   r0 iptables -L -v
   ```

## Note Aggiuntive
Se incontri problemi con il port forwarding, assicurati che le regole iptables sul router siano impostate correttamente e che il server web su Host1 sia in esecuzione e accessibile.

Ricorda che il server web deve essere avviato su Host1 prima di eseguire i test di connessione da Host2.
