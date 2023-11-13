FROM ubuntu:20.04

# Evita l'interazione durante l'installazione dei pacchetti
ENV DEBIAN_FRONTEND=noninteractive

# Installa Postfix e telnet (utile per i test)
RUN apt-get update && apt-get install -y \
    postfix \
    telnet \
    rsyslog

# Configurazione di Postfix per il relay senza restrizioni
RUN echo "smtpd_relay_restrictions = permit_mynetworks permit_sasl_authenticated defer_unauth_destination" >> /etc/postfix/main.cf && \
    echo "mynetworks = 0.0.0.0/0" >> /etc/postfix/main.cf

# Avvia i servizi
CMD service rsyslog start && service postfix start && tail -F /var/log/mail.log
