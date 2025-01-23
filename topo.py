from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import OVSSwitch, Controller, RemoteController

class MyTopo(Topo):
    def __init__(self):
        Topo.__init__(self)

        # Add switch
        s1 = self.addSwitch('s1')

        # Add hosts
        h1 = self.addHost('h1', ip="10.0.0.1/24")
        h2 = self.addHost('h2', ip="10.0.0.2/24")
        h3 = self.addHost('h3', ip="10.0.0.3/24")
        h4 = self.addHost('h4', ip="10.0.0.4/24")
        h5 = self.addHost('h5', ip="10.0.0.5/24")
        h6 = self.addHost('h6', ip="10.0.0.6/24")

        # Add links
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s1)
        self.addLink(h4, s1)
        self.addLink(h5, s1)
        self.addLink(h6, s1)

if __name__ == '__main__':  # แก้ไขให้ถูกต้อง
    setLogLevel('info')
    topo = MyTopo()
    c1 = RemoteController('c1', ip='127.0.0.1')
    net = Mininet(topo=topo, controller=c1)
    net.start()
    CLI(net)
    net.stop()