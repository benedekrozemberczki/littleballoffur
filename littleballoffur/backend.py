import networkx as nx
import networkit as nk

NKGraph = networkit._NetworKit.Graph
NXGraph = nx.classes.graph.Graph


class NetworKitBackEnd(object):
    """
    Binding the NetworKit backend to serve class methods.
    """
    def __init__(self):
        self.x = 1

    def get_number_of_nodes(self, graph: NKGraph):
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

    def get_number_of_nodes(self, graph: NXGraph) -> int:
        """
        Given a graph return the number of nodes.
        """
        return graph.number_of_nodes()
