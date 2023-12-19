#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, OVSKernelSwitch, Node
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import Link

def setup_network():
    net = Mininet(controller=Controller, switch=OVSKernelSwitch)

    # Aggiunta di un controller
    c0 = net.addController('c0')

    # Aggiunta di due switch
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')  # Switch aggiuntivo per separare le reti

    # Aggiunta di tre host
    h1 = net.addHost('h1', ip='192.168.1.2/24')
    h2 = net.addHost('h2', ip='192.168.1.3/24')
    h3 = net.addHost('h3', ip='10.0.0.2/24')  # Server esterno

    # Aggiunta di un router con due interfacce di rete
    router = net.addHost('r0', cls=Node)
    router.cmd('sysctl -w net.ipv4.ip_forward=1')

    # Collegamenti
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(router, s1)  # Collegamento del router al primo switch
    net.addLink(router, s2)  # Collegamento del router al secondo switch
    net.addLink(h3, s2)      # Collegamento del server esterno al secondo switch

    net.start()

    # Configurazione del router con due interfacce di rete
    router.cmd('ifconfig r0-eth0 192.168.1.1/24')
    router.cmd('ifconfig r0-eth1 10.0.0.1/24')
    router.cmd('./router_iptables.sh')

    # Configurazione degli host per usare il router come gateway
    h1.cmd('route add default gw 192.168.1.1')
    h2.cmd('route add default gw 192.168.1.1')
    h3.cmd('route add default gw 10.0.0.1')  # Configurazione del gateway per h3

    # Avvio dell'interfaccia a riga di comando di Mininet
    CLI(net)

    # Arresto della rete
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    setup_network()
