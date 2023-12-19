#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, OVSKernelSwitch, Node
from mininet.cli import CLI
from mininet.log import setLogLevel

def setup_network():
    net = Mininet(controller=Controller, switch=OVSKernelSwitch)

    # Aggiunta di un controller
    c0 = net.addController('c0')

    # Aggiunta di uno switch
    s1 = net.addSwitch('s1')

    # Aggiunta di due host
    h1 = net.addHost('h1', ip='192.168.1.2/24')  # Host interno con server web
    h2 = net.addHost('h2', ip='10.0.0.2/24')    # Host esterno

    # Aggiunta di un router
    router = net.addHost('r0', cls=Node)
    router.cmd('sysctl -w net.ipv4.ip_forward=1')

    # Collegamenti
    net.addLink(h1, s1)
    net.addLink(router, s1)
    net.addLink(h2, s1)

    net.start()

    # Configurazione del router
    router.cmd('ifconfig r0-eth0 192.168.1.1/24')
    router.cmd('ifconfig r0-eth1 10.0.0.1/24')
    router.cmd('./router_iptables_port_forwarding.sh')

    # Configurazione di Host1 e Host2 per usare il router come gateway
    h1.cmd('route add default gw 192.168.1.1')
    h2.cmd('route add default gw 10.0.0.1')

    # Avvio dell'interfaccia a riga di comando di Mininet
    CLI(net)

    # Arresto della rete
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    setup_network()
