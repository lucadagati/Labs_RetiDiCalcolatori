#!/bin/bash

# Pulisce le regole iptables esistenti
iptables -F

# Permette il traffico in entrata per SSH (porta 22)
iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# Blocca tutto il resto del traffico in entrata
iptables -A INPUT -j DROP

# Salva le regole
iptables-save
