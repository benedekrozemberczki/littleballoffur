import random
import numpy as np
import networkx as nx
from littleballoffur.sampler import Sampler

class ShortestPathSampler(Sampler):
    r"""An implementation of shortest path sampling.

    Args:
        number_of_nodes (int): Number of nodes to sample. Default is 100.
        seed (int): Random seed. Default is 42.
    """
    def __init__(self, number_of_nodes=100, seed=42):
        self.number_of_nodes = number_of_nodes
        self.seed = seed
        self._set_seed()


    def _set_seed_sets(self):
        self._nodes = set()
        self._edges = set()

    def _sample_a_node(self):
        return random.choice(range(self._graph.number_of_nodes()))

    def _sample_a_pair(self):
        source = self._sample_a_node()
        target = self._sample_a_node()
        return source, target

    def sample(self, graph):
        """
        Sampling with a shortest path sampler.

        Arg types:
            * **graph** *(NetworkX graph)* - The graph to be sampled from.

        Return types:
            * **new_graph** *(NetworkX graph)* - The graph of sampled nodes.
        """
        self._check_graph(graph)
        self._graph = graph
        while len(self._nodes) < self.number_of_nodes:
            source, target = self._a_sample_pair()
            if source != target:
                path = nx.shortest_path(self._graph, source = source, target = target)
                print(path)

