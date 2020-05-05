import random
import networkx as nx
from littleballoffur.sampler import Sampler

class RandomEdgeSampler(Sampler):
    r"""An implementation of random edge sampling.

    Args:
        number_of_edges (int): Number of edges. Default is 100.
        seed (int): Random seed. Default is 42.
    """
    def __init__(self, number_of_edges=100, seed=42):
        self.number_of_edges = number_of_edges
        self.seed = seed
        self._set_seed()

    def _create_initial_edge_set(self):
        """
        Choosing initial edges.
        """
        edges = [edge for edge in self._graph.edges()]
        self._sampled_edges = random.sample(edges, self.number_of_edges)

    def sample(self, graph):
        """
        Sampling edges randomly.

        Arg types:
            * **graph** *(NetworkX graph)* - The graph to be sampled from.

        Return types:
            * **new_graph** *(NetworkX graph)* - The graph of sampled edges.
        """
        self._check_graph(graph)
        self._check_number_of_edges(graph)
        self._graph = graph
        self._create_initial_edge_set()
        new_graph = nx.from_edgelist(self._sampled_edges)
        return new_graph
