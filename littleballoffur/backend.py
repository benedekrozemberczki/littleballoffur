import networkx as nx
import networkit as nk


class NetworKitBackEnd(object):
    """
    Binding the NetworKit backend to serve class methods.
    """
    def __init__(self):
        self.x = 1

    def get_number_of_nodes(self, graph: nx.instances.):
        """
        Given a graph return the number of nodes.
        """
        return graph.numberOfNodes()

class NetworkXBackEnd(object):
    """
    Binding the NetworkX backend to serve class methods.
    """
    def __init__(self):
        self.x = 1

    def get_number_of_nodes(self, graph: nx.classes.graph.Graph) -> int:
        """
        Given a graph return the number of nodes.
        """
        return graph.number_of_nodes()
