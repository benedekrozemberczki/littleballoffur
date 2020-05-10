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


    def _set_seed_set(self):
        """
        Creating an initial set of nodes.
        """
        self._nodes = set()

    def _sample_a_node(self):
        """
        Sampling a random node.
        """
        return random.choice(range(self._graph.number_of_nodes()))

    def _sample_a_pair(self):
        """
        Sampling a pair of nodes for a shortest path.
        """
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
        self._set_seed_set()
        while len(self._nodes) < self.number_of_nodes:
            source, target = self._sample_a_pair()
            if source != target:
                path = nx.shortest_path(self._graph, source, target)
                for node in path:
                    self._nodes.add(node)
                    if len(self._nodes) > self.number_of_nodes:
                        break

        new_graph = graph.subgraph(self._nodes)
        return new_graph
                    
                     

