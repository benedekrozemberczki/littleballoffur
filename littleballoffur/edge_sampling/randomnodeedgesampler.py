import random
import networkx as nx
from littleballoffur.sampler import Sampler

class RandomNodeEdgeSampler(Sampler):
    r"""An implementation of random node-edge sampling.

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
        self._sampled_edges = set()
        while len(self._sampled_edges) < self.number_of_edges:
            source_node = random.choice(range(self._graph.number_of_nodes()))
            target_node = random.choice([node for node in self._graph.neighbors(source_node)])
            edge = sorted([source_node, target_node])
            edge = tuple(edge)
            self._sampled_edges.add(edge)
            

    def sample(self, graph):
        """
        Sampling edges randomly from randomly sampled nodes.

        Arg types:
            * **graph** *(NetworkX graph)* - The graph to be sampled from.

        Return types:
            * **new_graph* *(NetworkX graph)* - The graph of sampled edges.
        """
        self._check_graph(graph)
        self._check_number_of_edges(graph)
        self._graph = graph
        self._create_initial_edge_set()
        new_graph = nx.from_edgelist(self._sampled_edges)
        return new_graph
