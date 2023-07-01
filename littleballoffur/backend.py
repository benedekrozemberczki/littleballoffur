import random
from typing import List, Tuple

import networkit as nk
import networkx as nx
import numpy as np

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
        return [node for node in self.get_node_iterator(graph)]

    def get_edges(self, graph: NKGraph) -> List[Tuple]:
        """
        Given a graph return the edges.
        """
        return [edge for edge in self.get_edge_iterator(graph)]

    def get_node_iterator(self, graph: NKGraph):
        """
        Given a graph return the node iterator.
        """
        return graph.iterNodes()

    def get_edge_iterator(self, graph: NKGraph):
        """
        Given a graph return the edge iterator.
        """
        return graph.iterEdges()

    def get_degree(self, graph: NKGraph, node: int) -> int:
        """
        Given a graph and node return the degree.
        """
        return graph.degree(node)

    def get_subgraph(self, graph: NKGraph, nodes: List[int]) -> NKGraph:
        """
        Given a graph and set of inducing nodes return a subgraph.
        """
        return nk.graphtools.subgraphFromNodes(graph, nodes)

    def get_neighbors(self, graph: NKGraph, node: int) -> List[int]:
        """
        Given a graph and node return the neighbors.
        """
        return [node for node in graph.iterNeighbors(node)]

    def get_random_neighbor(self, graph: NKGraph, node: int) -> int:
        """
        Given a graph and node returns a random neighbor.
        """
        return nk.graphtools.randomNeighbor(graph, node)

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

    def is_weighted(self, graph: NKGraph) -> bool:
        return graph.isWeighted()

    def get_edge_weight(self, graph: NKGraph, u: int, v: int) -> float:
        return graph.weight(u, v)

    def graph_from_edgelist(self, edges: List) -> NKGraph:
        """
        Given an edge list generate a graph.
        """
        new_graph = nk.graph.Graph(directed=False)
        for edge in edges:
            new_graph.addEdge(edge[0], edge[1], addMissing=True)
        return new_graph

    def _check_networkit_graph(self, graph: NKGraph):
        """Chechking the input type."""
        assert isinstance(graph, NKGraph), "This is not a NetworKit graph."

    def _check_connectivity(self, graph: NKGraph):
        """Checking the connected nature of a single graph."""
        connected = nk.components.ConnectedComponents(graph).run().numberOfComponents()
        assert connected == 1, "Graph is not connected."

    def _check_directedness(self, graph: NXGraph):
        """Checking the undirected nature of a single graph."""
        directed = graph.isDirected()
        assert directed == False, "Graph is directed."

    def _check_indexing(self, graph: NKGraph):
        """Checking the consecutive numeric indexing."""
        numeric_indices = [index for index in range(graph.numberOfNodes())]
        node_indices = sorted([node for node in self.get_nodes(graph)])
        assert numeric_indices == node_indices, "The node indexing is wrong."

    def check_graph(self, graph: NKGraph):
        """Check the Little Ball of Fur assumptions about the graph."""
        self._check_networkit_graph(graph)
        self._check_directedness(graph)
        self._check_indexing(graph)


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
        return [node for node in self.get_node_iterator(graph)]

    def get_edges(self, graph: NXGraph) -> List[Tuple]:
        """
        Given a graph return the edges.
        """
        return [edge for edge in graph.edges()]

    def get_node_iterator(self, graph: NXGraph):
        """
        Given a graph return the node iterator.
        """
        return graph.nodes()

    def get_edge_iterator(self, graph: NXGraph):
        """
        Given a graph return the edge iterator.
        """
        return graph.edges()

    def get_degree(self, graph: NXGraph, node: int) -> int:
        """
        Given a graph and node return the degree.
        """
        return graph.degree[node]

    def get_subgraph(self, graph: NXGraph, nodes: List[int]) -> NXGraph:
        """
        Given a graph and set of inducing nodes return a subgraph.
        """
        return graph.subgraph(nodes)

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
        pagerank = nx.pagerank(graph, alpha=alpha)
        pagerank = np.array([pagerank[node] for node in graph.nodes()])
        pagerank = pagerank / pagerank.sum()
        return pagerank

    def is_weighted(self, graph: NXGraph) -> bool:
        return nx.is_weighted(graph)

    def get_edge_weight(self, graph: NXGraph, u: int, v: int) -> float:
        return graph.get_edge_data(u, v)["weight"]

    def graph_from_edgelist(self, edges: List) -> NXGraph:
        """
        Given an edge list generate a graph.
        """
        graph = nx.from_edgelist(edges)
        return graph

    def _check_networkx_graph(self, graph: NXGraph):
        """Chechking the input type."""
        assert isinstance(graph, NXGraph), "This is not a NetworkX graph."

    def _check_connectivity(self, graph: NXGraph):
        """Checking the connected nature of a single graph."""
        connected = nx.is_connected(graph)
        assert connected, "Graph is not connected."

    def _check_directedness(self, graph: NXGraph):
        """Checking the undirected nature of a single graph."""
        directed = nx.is_directed(graph)
        assert directed == False, "Graph is directed."

    def _check_indexing(self, graph: NXGraph):
        """Checking the consecutive numeric indexing."""
        numeric_indices = [index for index in range(graph.number_of_nodes())]
        node_indices = sorted([node for node in graph.nodes()])
        assert numeric_indices == node_indices, "The node indexing is wrong."

    def check_graph(self, graph: NXGraph):
        """Check the Little Ball of Fur assumptions about the graph."""
        self._check_networkx_graph(graph)
        self._check_directedness(graph)
        self._check_indexing(graph)
