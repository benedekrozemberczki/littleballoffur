import networkx as nx
import networkit

NKGraph = type(networkit.graph.Graph())
NXGraph = nx.classes.graph.Graph


class NetworKitBackEnd(object):
    """
    Binding the NetworKit backend to serve graph operations.
    """
    def __init__(self):
        pass

    def get_number_of_nodes(self, graph: NKGraph) -> int:
        """
        Given a graph return the number of nodes.
        """
        return graph.numberOfNodes()

    def get_number_of_edges(self, graph: NKGraph) -> int:
        """
        Given a graph return the number of edges.
        """
        return graph.numberOfEdges()

    def get_degree(self, graph: NKGraph, node: int) -> int:
        """
        Given a node return the degree.
        """
        return graph.degree(node)


class NetworkXBackEnd(object):
    """
    Binding the NetworkX backend to serve graph operations.
    """
    def __init__(self):
        pass

    def get_number_of_nodes(self, graph: NXGraph) -> int:
        """
        Given a graph return the number of nodes.
        """
        return graph.number_of_nodes()

    def get_number_of_edges(self, graph: NXGraph) -> int:
        """
        Given a graph return the number of edges.
        """
        return graph.number_of_edges()

    def get_degree(self, graph: NKGraph, node: int) -> int:
        """
        Given a node return the degree.
        """
        return graph.degree[node]
