# Istruzioni per Test di Configurazione iptables

1. ## Test per Host1 (Accetta solo traffico SSH)
   ### Verifica del blocco di traffico non SSH:
   Dall'host2 o host3, prova a fare ping verso host1. Questo traffico dovrebbe essere bloccato.
   ```bash
   h2 ping h1
   ```
   ### Verifica dell'accettazione del traffico SSH:
   Se hai un server SSH in esecuzione su host1, prova a connetterti via SSH da host2 o host3. Questa connessione dovrebbe avere successo.
   ```bash
   h2 ssh h1
   ```

2. ## Test per Host2 (Rifiuta traffico da Host1 e logga)
   ### Verifica del rifiuto del traffico da Host1:
   Da host1, prova a fare ping verso host2. Questo traffico dovrebbe essere rifiutato.
   ```bash
   h1 ping h2
   ```
   ### Verifica del log:
   Controlla i log su host2 per vedere se i tentativi di ping da host1 sono stati registrati.
   ```bash
   h2 cat /var/log/syslog | grep "Blocked HOST1"
   ```

3. ## Test per Host3 (Limita richieste HTTP)
   ### Verifica della limitazione delle richieste HTTP:
   Se hai un server web in esecuzione su host3, prova a effettuare ripetute richieste HTTP da host1 o host2. Dopo la prima richiesta, le successive dovrebbero essere bloccate o limitate.
   ```bash
   h1 curl h3:80
   h2 curl h3:80
   ```

## Note Aggiuntive

### Accesso agli Host per Controlli Configurazione:
Puoi accedere a ciascun host tramite la CLI di Mininet e verificare la configurazione di iptables con il comando `iptables -L`.
```bash
mininet> xterm h1
```
E poi in una nuova finestra di terminale:
```bash
iptables -L
```

### Test di Connettività Generale:
Usa il comando `pingall` in Mininet per testare la connettività di base tra tutti gli host.
