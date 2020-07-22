import networkx as nx
import networkit as nk


class NetworKitBackEnd(object):
    """
    Binding the NetworKit backend to serve class methods.
    """
    def __init__(self):
        self.x = 1

    def get_x(self):
        return self.x

class NetworkXBackEnd(object):
    """
    Binding the NetworkX backend to serve class methods.
    """
    def __init__(self):
        self.x = 1

    def get_x(self):
        return self.x
