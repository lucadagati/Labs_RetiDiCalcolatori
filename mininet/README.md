# Istruzioni per la Configurazione delle Regole iptables

1. ## Blocco del Traffico In Entrata su una Specifica Porta
   Per bloccare tutto il traffico in entrata su, ad esempio, la porta TCP 80 (HTTP), usa la seguente regola:
   ```bash
   iptables -A INPUT -p tcp --dport 80 -j DROP
   ```

2. ## Consentire il Traffico In Entrata su una Specifica Porta
   Per consentire il traffico su una porta specifica (ad esempio, la porta SSH, 22):
   ```bash
   iptables -A INPUT -p tcp --dport 22 -j ACCEPT
   ```

3. ## Bloccare il Traffico da un Indirizzo IP Specifico
   Per bloccare tutto il traffico proveniente da un certo indirizzo IP:
   ```bash
   iptables -A INPUT -s 192.168.1.10 -j DROP
   ```

4. ## Limitare il Numero di Connessioni
   Per limitare il numero di connessioni in entrata per prevenire attacchi DoS:
   ```bash
   iptables -A INPUT -p tcp --dport 80 -m limit --limit 10/min -j ACCEPT
   iptables -A INPUT -p tcp --dport 80 -j DROP
   ```

5. ## Redirezione del Traffico
   Per redirigere il traffico che arriva su una porta verso un'altra porta:
   ```bash
   iptables -t nat -A PREROUTING -p tcp --dport 8080 -j REDIRECT --to-port 80
   ```

6. ## Log del Traffico
   Per registrare in un log tutto il traffico in entrata:
   ```bash
   iptables -A INPUT -j LOG --log-prefix "INPUT: "
   ```

7. ## Bloccare tutto il Traffico tranne che su Porte Specifiche
   Per esempio, bloccare tutto tranne che il traffico SSH e HTTP:
   ```bash
   iptables -A INPUT -p tcp -m multiport ! --dports 22,80 -j DROP
   ```
