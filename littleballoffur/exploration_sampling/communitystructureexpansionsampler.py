import random
import numpy as np
import networkx as nx
from collections import deque
from littleballoffur.sampler import Sampler

class CommunityStructureExpansionSampler(Sampler):
    r"""An implementation of community structure preserving expansion sampling.

    Args:
        number_of_nodes (int): Number of sampled nodes. Default is 100.
        seed (int): Random seed. Default is 42.
    """
    def __init__(self, number_of_nodes=100, seed=42):
        self.number_of_nodes = number_of_nodes
        self.seed = seed
        self._set_seed()

    def _create_node_set(self):
        """
        Choosing a seed node.
        """
        self._sampled_nodes = set([random.choice(range(self._graph.number_of_nodes()))])

    def sample(self, graph):
        """
        Sampling nodes iteratively with a forest fire sampler.

        Arg types:
            * **graph** *(NetworkX graph)* - The graph to be sampled from.

        Return types:
            * **new_graph** *(NetworkX graph)* - The graph of sampled nodes.
        """
        self._check_graph(graph)
        self._check_number_of_nodes(graph)
        self._graph = graph
        self._create_node_sets()
