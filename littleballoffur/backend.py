import networkx as nx
import networkit

NKGraph = type(networkit.graph.Graph())
NXGraph = nx.classes.graph.Graph


class NetworKitBackEnd(object):
    """
    Binding the NetworKit backend to serve class methods.
    """
    def __init__(self):
        self.x = 1

    def get_number_of_nodes(self, graph: NKGraph) -> int:
        """
        Given a graph return the number of nodes.
        """
        return graph.numberOfNodes()

    def get_number_of_edges(self, graph: NKGraph) -> int:
        """
        Given a graph return the number of nodes.
        """
        return graph.numberOfEdges()


class NetworkXBackEnd(object):
    """
    Binding the NetworkX backend to serve class methods.
    """
    def __init__(self):
        self.x = 1

    def get_number_of_edges(self, graph: NXGraph) -> int:
        """
        Given a graph return the number of nodes.
        """
        return graph.number_of_edges()
