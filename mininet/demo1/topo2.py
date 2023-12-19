from mininet.topo import Topo
from mininet.net import Mininet
import pickle

class MyTopology(Topo):
    def __init__(self):
        super(MyTopology, self).__init__()

        # Add hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')

        # Add switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')

        # Add links
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s2)
        self.addLink(h4, s2)
        self.addLink(s1, s2)

if __name__ == '__main__':
    mytopo = MyTopology()

    net = Mininet(topo=mytopo)
    net.start()

    # Save the topology to a file using pickle
    with open('topo2.pkl', 'wb') as f:
        pickle.dump(mytopo, f)

    # You can access the hosts using net.get() as before
    h1 = net.get('h1')
    h2 = net.get('h2')
    h3 = net.get('h3')
    h4 = net.get('h4')

    # Example: Ping between hosts
    h1.cmd('ping -c 3', h2.IP())
    h3.cmd('ping -c 3', h4.IP())

    net.stop()
