# Usa una versione leggera di Debian come immagine di base
FROM debian:stable-slim

# Installa lftp, un client FTP/SFTP/HTTP più versatile di ftp
RUN apt-get update && \
    apt-get install -y lftp

# Imposta il punto di ingresso per il client FTP
ENTRYPOINT ["lftp"]
