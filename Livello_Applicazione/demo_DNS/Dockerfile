# Usa l'immagine base di Ubuntu 20.04
FROM ubuntu:20.04

# Installa bind9 e utilità
RUN apt-get update && apt-get install -y bind9

# Copia i file di configurazione nel container
COPY named.conf.local /etc/bind/named.conf.local
COPY db.demo.local /etc/bind/db.demo.local

# Esponi la porta 53
EXPOSE 54/udp 54/tcp

# Avvia BIND in foreground
CMD ["/usr/sbin/named", "-g"]
