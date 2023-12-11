# Guida alla Configurazione di un Server DHCP su Linux

## Introduzione
Questa guida è pensata per studenti e insegnanti che vogliono imparare a configurare un server DHCP in un ambiente Linux, utilizzando un'interfaccia di rete virtuale.

## Prerequisiti
- Accesso a un sistema Linux (Ubuntu/Debian è consigliato).
- Privilegi di superutente (root).

## Passaggi di Configurazione

### 1. Installazione del Server DHCP
Apri un terminale e esegui:
```bash
sudo apt-get update
sudo apt-get install isc-dhcp-server
```

### 2. Creazione di un'Interfaccia di Rete Virtuale
Carica il modulo dummy e crea un'interfaccia virtuale:

```bash
sudo modprobe dummy
sudo ip link add dummy0 type dummy
sudo ip addr add 192.168.1.1/24 dev dummy0
sudo ip link set dummy0 up
```
Questo crea un'interfaccia dummy0 con l'indirizzo IP 192.168.1.1.

### 3. Configurazione del Server DHCP
Modifica il file di configurazione DHCP:

```bash
sudo nano /etc/dhcp/dhcpd.conf
```

Aggiungi la seguente configurazione:

```bash
default-lease-time 600;
max-lease-time 7200;
authoritative;

subnet 192.168.1.0 netmask 255.255.255.0 {
    range 192.168.1.10 192.168.1.100;
    option routers 192.168.1.1;
}
```

Salva e chiudi il file.

### 4. Assegnazione dell'Interfaccia di Rete
Indica al server DHCP di ascoltare sull'interfaccia virtuale:

```bash
sudo nano /etc/default/isc-dhcp-server
Imposta INTERFACES="dummy0".
```

### 5. Avvio del Server DHCP
Avvia il servizio:

```bash
sudo service isc-dhcp-server start
```
Verifica lo stato:

```bash
sudo service isc-dhcp-server status
```

### Risoluzione dei Problemi
Se incontri problemi, controlla i log in /var/log/syslog per eventuali messaggi di errore.
