import random
import networkx as nx
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

    def _make_target_set(self):
        """
        Creating a new reshuffled frontier list of nodes.
        """
        self._targets = [neighbor for node in self._sampled_nodes for neighbor in self._graph.neighbors(node)]
        self._targets = list(set(self._targets).difference(self._sampled_nodes))
        random.shuffle(self._targets)

    def _choose_new_node(self):
        """
        Choosing the node with the largest expansion.
        The randomization of the list breaks ties randomly.
        """
        largest_expansion = 0
        for node in self._targets:
            expansion = len(set(self._graph.neighbors(node)).difference(self._sampled_nodes))
            if expansion >= largest_expansion:
                new_node = node
        self._sampled_nodes.add(new_node)

    def sample(self, graph):
        """
        Sampling nodes iteratively with a community structure expansion sampler.

        Arg types:
            * **graph** *(NetworkX graph)* - The graph to be sampled from.

        Return types:
            * **new_graph** *(NetworkX graph)* - The graph of sampled nodes.
        """
        self._check_graph(graph)
        self._check_number_of_nodes(graph)
        self._graph = graph
        self._create_node_set()
        while len(self._sampled_nodes) < self.number_of_nodes:
            self._make_target_set()
            self._choose_new_node()
        new_graph = self._graph.subgraph(self._sampled_nodes)
        return new_graph
