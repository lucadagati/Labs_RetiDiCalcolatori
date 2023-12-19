#!/bin/bash

# Abilita l'IP forwarding
echo 1 > /proc/sys/net/ipv4/ip_forward

# Pulisce le regole iptables esistenti
iptables -F
iptables -t nat -F

# Regole di MASQUERADE per il NAT
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE

# Consenti il forwarding tra le interfacce
iptables -A FORWARD -i eth1 -o eth0 -j ACCEPT
iptables -A FORWARD -i eth0 -o eth1 -m state --state RELATED,ESTABLISHED -j ACCEPT
