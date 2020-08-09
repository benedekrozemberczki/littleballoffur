import random
import networkx as nx
from littleballoffur.sampler import Sampler

class RandomNodeSampler(Sampler):
    r"""An implementation of random node sampling. Nodes are sampled with uniform
    probability. `"For details about the algorithm see this paper." <https://www.pnas.org/content/102/12/4221>`_

    Args:
        number_of_nodes (int): Number of nodes. Default is 100.
        seed (int): Random seed. Default is 42.
    """
    def __init__(self, number_of_nodes: int=100, seed: int=42):
        self.number_of_nodes = number_of_nodes
        self.seed = seed
        self._set_seed()

    def _create_initial_node_set(self):
        """
        Choosing initial nodes.
        """
        nodes = [node for node in range(self._graph.number_of_nodes())]
        self._sampled_nodes = random.sample(nodes, self.number_of_nodes)

    def sample(self, graph: nx.classes.graph.Graph) -> nx.classes.graph.Graph:
        """
        Sampling nodes randomly.

        Arg types:
            * **graph** *(NetworkX graph)* - The graph to be sampled from.

        Return types:
            * **new_graph** *(NetworkX graph)* - The graph of sampled nodes.
        """
        self._deploy_backend(graph)
        self._check_number_of_nodes(graph)
        self._graph = graph
        self._create_initial_node_set()
        new_graph = self._graph.subgraph(self._sampled_nodes)
        return new_graph
