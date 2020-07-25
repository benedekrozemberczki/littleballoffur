import random
import networkit
import networkx as nx
from typing import List


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
        Given a graph and node return the degree.
        """
        return graph.degree(node)

    def get_neighbors(self, graph: NKGraph, node: int) -> List[int]:
        """
        Given a graph and node return the neighbors.
        """
        return graph.neighbors(node)

    def get_random_neighbor(self, graph: NKGraph, node: int) -> int:
        """
        Given a graph and node returns a random neighbor.
        """
        return graph.randomNeighbor(node)

   def get_shortest_path(self, graph: NKGraph, source: int, target: int) -> List[int]:
       """
       Given a graph, a source and target node get the shortes path
       """
       return nk.distance.ReverseBFS(graph, source, True, False, target).run().getPath(target)


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

    def get_degree(self, graph: NXGraph, node: int) -> int:
        """
        Given a graph and node return the degree.
        """
        return graph.degree[node]

    def get_neighbors(self, graph: NXGraph, node: int) -> List[int]:
        """
        Given a graph and node return the neighbors.
        """
        return [node for node in graph.neighbors(node)]


    def get_random_neighbor(self, graph: NXGraph, node: int) -> int:
        """
        Given a graph and node returns a random neighbor.
        """
        neighbors = self.get_neighbors(graph, node)
        return random.choice(neighbors)
