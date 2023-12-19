#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, OVSKernelSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel

def setup_network():
    net = Mininet(controller=Controller, switch=OVSKernelSwitch)

    # Aggiunta di un controller
    c0 = net.addController('c0')

    # Aggiunta di due switch
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')

    # Aggiunta di tre host
    host1 = net.addHost('h1')
    host2 = net.addHost('h2')
    host3 = net.addHost('h3')

    # Collegamenti
    net.addLink(host1, s1)
    net.addLink(host2, s2)
    net.addLink(host3, s2)
    net.addLink(s1, s2)

    # Avvio della rete
    net.start()

    # Applicazione degli script iptables
    host1.cmd('./host1_iptables.sh')
    host2.cmd('./host2_iptables.sh')
    host3.cmd('./host3_iptables.sh')

    # Avvio dell'interfaccia a riga di comando di Mininet
    CLI(net)

    # Arresto della rete
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    setup_network()
