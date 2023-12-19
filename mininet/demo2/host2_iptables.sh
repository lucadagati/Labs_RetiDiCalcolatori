#!/bin/bash

# Pulisce le regole iptables esistenti
iptables -F

# Indirizzo IP di Host1 (sostituire con l'indirizzo IP effettivo di Host1)
HOST1_IP="192.168.1.1"

# Rifiuta e logga il traffico proveniente da Host1
iptables -A INPUT -s $HOST1_IP -j LOG --log-prefix "Blocked HOST1: "
iptables -A INPUT -s $HOST1_IP -j REJECT

# Permette tutto il resto del traffico in entrata
iptables -A INPUT -j ACCEPT

# Salva le regole
iptables-save
