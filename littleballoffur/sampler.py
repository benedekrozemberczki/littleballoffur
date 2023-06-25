import random
from typing import Union

import networkit as nk
import networkx as nx
import numpy as np

from littleballoffur.backend import NetworKitBackEnd, NetworkXBackEnd

NKGraph = type(nk.graph.Graph())
NXGraph = nx.classes.graph.Graph


class Sampler(object):
    """Sampler base class with constructor and private methods."""

    def __init__(self):
        """Creating a sampler."""
        pass

    def sample(self):
        """Sample from a model."""
        pass

    def _set_seed(self):
        """Creating the initial random seed."""
        random.seed(self.seed)
        np.random.seed(self.seed)

    def _deploy_backend(self, graph: Union[NKGraph, NXGraph]):
        """Chechking the input type."""
        if isinstance(graph, NKGraph):
            self.backend = NetworKitBackEnd()
            self.backend.check_graph(graph)
        elif isinstance(graph, NXGraph):
            self.backend = NetworkXBackEnd()
            self.backend.check_graph(graph)
        else:
            raise ValueError("Not a NetworKit or NetworkX graph.")

    def _check_networkx_graph(self, graph):
        """Chechking the input type."""
        assert isinstance(graph, nx.classes.graph.Graph), "This is not a NetworkX graph."

    def _check_directedness(self, graph):
        """Checking the undirected nature of a single graph."""
        directed = nx.is_directed(graph)
        assert directed is False, "Graph is directed."

    def _check_indexing(self, graph):
        """Checking the consecutive numeric indexing."""
        numeric_indices = [index for index in range(graph.number_of_nodes())]
        if hasattr(self, "backend") and isinstance(self.backend, NetworKitBackEnd):
            node_indices = sorted([node for node in self.backend.get_nodes(graph)])
        elif hasattr(self, "backend") and isinstance(self.backend, NetworkXBackEnd):
            node_indices = sorted([node for node in graph.nodes()])
        else:
            node_indices = sorted([node for node in graph.nodes()])
        assert numeric_indices == node_indices, "The node indexing is wrong."

    def _check_graph(self, graph: nx.classes.graph.Graph):
        """Check the Little Ball of Fur assumptions about the graph."""
        self._check_networkx_graph(graph)
        self._check_directedness(graph)
        self._check_indexing(graph)

    def _check_number_of_nodes(self, graph):
        """Checking the size of the graph - nodes."""
        if self.number_of_nodes > self.backend.get_number_of_nodes(graph):
            raise ValueError("The number of nodes is too large. Please see requirements.")

    def _check_number_of_edges(self, graph):
        """Checking the size of the graph -- edges."""
        if self.number_of_edges > self.backend.get_number_of_edges(graph):
            raise ValueError("The number of edges is too large. Please see requirements.")
