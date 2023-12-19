#!/bin/bash

# Pulisce le regole iptables esistenti
iptables -F

# Limite di richieste HTTP per prevenire attacchi DoS
iptables -A INPUT -p tcp --dport 80 -m limit --limit 1/min -j ACCEPT
iptables -A INPUT -p tcp --dport 80 -j REJECT

# Permette tutto il resto del traffico in entrata
iptables -A INPUT -j ACCEPT

# Salva le regole
iptables-save
