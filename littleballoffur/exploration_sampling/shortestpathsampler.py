import random
import networkx as nx
import networkit as nk
from typing import Union
from littleballoffur.sampler import Sampler


NKGraph = type(nk.graph.Graph())
NXGraph = nx.classes.graph.Graph


class ShortestPathSampler(Sampler):
    r"""An implementation of shortest path sampling. The procedure samples pairs
    of nodes and chooses a random shortest path between them. Vertices and edges
    on this shortest path are added to the induces subgraph that is extracted.
    `"For details about the algorithm see this paper." <https://www.sciencedirect.com/science/article/pii/S0378437115000321>`_

    Args:
        number_of_nodes (int): Number of nodes to sample. Default is 100.
        seed (int): Random seed. Default is 42.
    """

    def __init__(self, number_of_nodes: int = 100, seed: int = 42):
        self.number_of_nodes = number_of_nodes
        self.seed = seed
        self._set_seed()

    def _set_seed_set(self):
        """
        Creating an initial set of nodes.
        """
        self._nodes = set()

    def _sample_a_node(self, graph):
        """
        Sampling a random node.
        """
        return random.choice(range(self.backend.get_number_of_nodes(graph)))

    def _sample_a_pair(self, graph):
        """
        Sampling a pair of nodes for a shortest path.
        """
        source = self._sample_a_node(graph)
        target = self._sample_a_node(graph)
        return source, target

    def sample(self, graph: Union[NXGraph, NKGraph]) -> Union[NXGraph, NKGraph]:
        """
        Sampling with a shortest path sampler.

        Arg types:
            * **graph** *(NetworkX or NetworKit graph)* - The graph to be sampled from.

        Return types:
            * **new_graph** *(NetworkX or NetworKit graph)* - The graph of sampled nodes.
        """
        self._deploy_backend(graph)
        self._set_seed_set()
        while len(self._nodes) < self.number_of_nodes:
            source, target = self._sample_a_pair(graph)
            if source != target:
                path = self.backend.get_shortest_path(graph, source, target)
                for node in path:
                    self._nodes.add(node)
                    if len(self._nodes) >= self.number_of_nodes:
                        break

        new_graph = self.backend.get_subgraph(graph, self._nodes)
        return new_graph
