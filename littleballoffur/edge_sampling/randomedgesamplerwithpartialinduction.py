import random
import networkx as nx
from littleballoffur import Sampler

class RandomEdgeSamplerWithPartialInduction(Sampler):
    r"""An implementation of random edge sampling with partial edge set induction.

    Args:
        p (float): Sampling probability. Default is 0.5.
        seed (int): Random seed. Default is 42.
    """
    def __init__(self, p=0.5, seed=42):
        self.p = p
        self.seed = seed
        self._set_seed()

    def sample(self, graph):
        """
        Sampling edges randomly with partial induction.

        Arg types:
            * **graph** *(NetworkX graph)* - The graph to be sampled from.

        Return types:
            * **new_graph** *(NetworkX graph)* - The graph of sampled edges.
        """
        self._check_graph(graph)
        self._check_number_of_edges(graph)
        self._graph = graph
        self._create_initial_set()
