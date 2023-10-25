#!/usr/bin/env python
from mininet.topo import Topo

class MyTopo(Topo):
    def __init__(self):
        # initilaize topology
        Topo.__init__(self)

        self.addSwitch("s1")
        self.addSwitch("s2")

        self.addHost("h1")
        self.addHost("h2")
        self.addHost("h3")
        self.addHost("h4")

        self.addLink("s1", "h1")
        self.addLink("s1", "h2")
        self.addLink("s2", "h3")
        self.addLink("s2", "h4")
        self.addLink("s1", "s2")

topos = {'mytopo': (lambda: MyTopo())}
