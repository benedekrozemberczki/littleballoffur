import random
import numpy as np
import networkx as nx
from littleballoffur.sampler import Sampler

class ForestFireSampler(Sampler):
    r"""An implementation of frontier sampling.

    Args:
        number_of_nodes (int): Number of sampled nodes. Default is 100.
        p (float): Burning probability. Default is 0.15.
        seed (int): Random seed. Default is 42.
    """
    def __init__(self, number_of_nodes=3, p=0.15, seed=42):
        self.number_of_nodes = number_of_nodes
        self.p = p
        self.seed = seed
        self._set_seed()

    def sample(self, graph):
        """
        Sampling nodes and edges with a forest fire sampler.

        Arg types:
            * **graph** *(NetworkX graph)* - The graph to be sampled from.

        Return types:
            * **new_graph** *(NetworkX graph)* - The graph of sampled nodes.
        """
        self._nodes = set()
        self._edges = set()
        self._check_graph(graph)
        self._check_number_of_nodes(graph)
        self._graph = graph
