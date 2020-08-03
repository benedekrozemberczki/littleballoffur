import random
import numpy as np
import networkx as nx
import networkit as nk
from typing import List, Tuple


NKGraph = type(nk.graph.Graph())
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

    def get_nodes(self, graph: NKGraph) -> List:
        """
        Given a graph return the nodes.
        """
        return graph.nodes()

    def get_edges(self, graph: NKGraph) -> List[Tuple]:
        """
        Given a graph return the edges.
        """
        return graph.edges()


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
        Given a graph, a source and target node pair get the shortes path
        """
        return nk.distance.ReverseBFS(graph, source, True, False, target).run().getPath(target)


    def get_pagerank(self, graph: NKGraph, alpha: float) -> np.array:
        """
        Given a graph return the PageRank vector.
        """
        pagerank = nk.centrality.PageRank(graph, alpha)
        pagerank.run()
        pagerank = np.array(pagerank.scores())
        pagerank = pagerank / pagerank.sum()
        return pagerank


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

    def get_nodes(self, graph: NXGraph) -> List:
        """
        Given a graph return the nodes.
        """
        return [node for node in graph.nodes()]

    def get_edges(self, graph: NXGraph) -> List[Tuple]:
        """
        Given a graph return the edges.
        """
        return [edge for edge in graph.edges()]


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


    def get_shortest_path(self, graph: NXGraph, source: int, target: int) -> List[int]:
        """
        Given a graph, a source and target node pair get the shortes path
        """
        return nx.shortest_path(graph, source, target)


    def get_pagerank(self, graph: NXGraph, alpha: float) -> np.array:
        """
        Given a graph return the PageRank vector.
        """
        pagerank = nx.pagerank_scipy(graph, alpha=alpha)
        pagerank = np.array([pagerank[node] for node in graph.nodes()])
        pagerank = pagerank / pagerank.sum()
        return pagerank
