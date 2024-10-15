# Usa l'immagine base di Ubuntu 20.04
FROM ubuntu:20.04

# Installa bind9 e utilità necessarie
RUN apt-get update && apt-get install -y bind9 bind9utils bind9-doc nano net-tools dnsutils


# Crea la directory necessaria e assegna i permessi corretti
RUN mkdir -p /run/named && chown bind:bind /run/named
RUN chown -R bind:bind /etc/bind && chmod 777 /etc/bind/rndc.key


# Copia i file di configurazione nel container
COPY named.conf.local /etc/bind/named.conf.local
COPY db.demo.local /etc/bind/db.demo.local
COPY named.conf.options /etc/bind/named.conf.options

# Assegna i permessi corretti ai file di configurazione
RUN chown -R bind:bind /etc/bind

# Espone la porta 53 per il DNS (TCP e UDP)
EXPOSE 53/udp 53/tcp

# Avvia BIND in foreground per evitare che il container si chiuda
CMD ["/usr/sbin/named", "-g", "-c", "/etc/bind/named.conf"]
