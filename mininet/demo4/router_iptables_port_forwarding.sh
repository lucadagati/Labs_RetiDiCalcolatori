#!/bin/bash

# Abilita l'IP forwarding
echo 1 > /proc/sys/net/ipv4/ip_forward

# Pulisce le regole iptables esistenti
iptables -F
iptables -t nat -F

# Regole di MASQUERADE per il NAT
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE

# Port forwarding dalla porta 8080 del router alla porta 80 di Host1
# Assumi che l'IP interno di Host1 sia 192.168.1.2
iptables -t nat -A PREROUTING -p tcp --dport 8080 -j DNAT --to-destination 192.168.1.2:80

# Consenti il forwarding per il port forwarding
iptables -A FORWARD -p tcp -d 192.168.1.2 --dport 80 -j ACCEPT
