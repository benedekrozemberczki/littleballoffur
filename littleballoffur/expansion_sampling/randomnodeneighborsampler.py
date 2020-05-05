import random
import networkx as nx
from littleballoffur.sampler import Sampler

class RandomNodeNeighborSampler(Sampler):
    r"""An implementation of random node sampling.

    Args:
        number_of_nodes (int): Number of nodes. Default is 100.
        seed (int): Random seed. Default is 42.
    """
    def __init__(self, number_of_nodes=100, seed=42):
        self.number_of_nodes = number_of_nodes
        self.seed = seed
        self._set_seed()

    def _create_initial_node_set(self):
        """
        Choosing initial nodes.
        """
        nodes = [node for node in range(self._graph.number_of_nodes())]
        self._sampled_nodes = random.sample(nodes, self.number_of_nodes)

    def sample(self, graph):
        """
        Sampling nodes randomly.

        Arg types:
            * **graph** *(NetworkX graph)* - The graph to be sampled from.

        Return types:
            * **new_graph* *(NetworkX graph)* - The graph of sampled nodes.
        """
        self._check_graph(graph)
        self._check_number_of_nodes(graph)
        self._graph = graph
        self._create_initial_node_set()
        new_graph = self._graph.subgraph(self._sampled_nodes)
        return new_graph
