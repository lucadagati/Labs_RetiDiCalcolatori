# Usa una versione leggera di Debian come immagine di base
FROM debian:stable-slim

# Installa vsftpd e qualsiasi altra dipendenza necessaria
RUN apt-get update && \
    apt-get install -y vsftpd

# Crea la directory secure_chroot_dir che vsftpd aspetta di trovare
RUN mkdir -p /var/run/vsftpd/empty

# Crea un utente per FTP con una home directory e setta le permissions
RUN useradd -m ftpuser -s /bin/bash && \
    echo "ftpuser:ftppassword" | chpasswd

# Creazione di una directory per i file FTP con i permessi appropriati
RUN mkdir /home/ftpuser/ftp && \
    chown nobody:nogroup /home/ftpuser/ftp && \
    chmod a-w /home/ftpuser/ftp && \
    mkdir /home/ftpuser/ftp/files && \
    chown ftpuser:ftpuser /home/ftpuser/ftp/files

# Configura vsftpd
COPY vsftpd.conf /etc/vsftpd.conf

# Espone le porte per il comando e le connessioni dati
EXPOSE 20-21 10090-10100

# Imposta il comando per eseguire vsftpd in foreground
CMD ["vsftpd", "/etc/vsftpd.conf"]
