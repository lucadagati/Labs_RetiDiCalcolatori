# Verifica della Configurazione della Rete

Prima di tutto, verifica che tutte le configurazioni di rete siano corrette:

## Verifica degli indirizzi IP degli host:

```bash
h1 ifconfig
h2 ifconfig
h3 ifconfig
r0 ifconfig
```

## Verifica le tabelle di routing:

### Per gli host (h1, h2, h3):

```bash
h1 route -n
h2 route -n
h3 route -n
```

### Sul router (r0):

```bash
r0 route -n
```

## Test di Connettività e NAT

Dopo aver verificato che la configurazione sia corretta, puoi procedere con i test:

### Test di Ping tra gli Host Interni (h1, h2) e il Server Esterno (h3):

```bash
h1 ping -c 3 10.0.0.2
h2 ping -c 3 10.0.0.2
```

### Test di Ping dal Server Esterno (h3) agli Host Interni (h1, h2):

Questo test potrebbe non riuscire a seconda delle regole di iptables sul router, in quanto il NAT potrebbe non essere configurato per il traffico in entrata.

```bash
h3 ping -c 3 192.168.1.2
h3 ping -c 3 192.168.1.3
```

## Verifica delle Regole iptables sul Router:

Controlla le regole NAT e di forwarding.

```bash
r0 iptables -t nat -L -v
r0 iptables -L -v
```

## Test di Connettività Completo:

Usa il comando `pingall` in Mininet per testare la connettività complessiva.

```bash
pingall
```

## Note Aggiuntive

- **Server Web o Altri Servizi:** Se hai un server web o altri servizi in esecuzione su h3, puoi testare la connettività usando curl o strumenti simili da h1 o h2.
- **Monitoraggio del Traffico:** Puoi usare strumenti come tcpdump su vari host o sul router per monitorare il traffico e vedere come vengono applicate le regole iptables.

Questi test ti permetteranno di dimostrare come il traffico viene inoltrato e modificato attraverso il router con le regole di NAT, mostrando sia la connettività di base che gli aspetti più avanzati del controllo del traffico di rete.
