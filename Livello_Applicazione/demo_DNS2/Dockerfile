FROM ubuntu:latest
RUN apt-get update && apt-get install -y bind9 bind9utils bind9-doc
EXPOSE 53/udp 53/tcp
ENTRYPOINT ["/usr/sbin/named", "-g", "-c", "/etc/bind/named.conf", "-u", "bind"]
