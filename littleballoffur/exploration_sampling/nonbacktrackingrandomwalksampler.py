import random
import networkx as nx
from littleballoffur.sampler import Sampler

class NonBackTrackingRandomWalkSampler(Sampler):
    r"""An implementation of node sampling by non back-tracking random walks.
    The process generates a random walk in which the random walker cannot make steps
    backwards. This way the tottering behaviour of random walkers can be avoided. `"For details about the algorithm see this paper." <https://ieeexplore.ieee.org/document/8731555>`_


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
        Choosing an initial node.
        """
        self._current_node = random.choice(range(self._graph.number_of_nodes()))
        self._sampled_nodes = set([self._current_node])
        self._previous_node = -1

    def _do_a_step(self):
        """
        Doing a single non back-tracking random walk step.
        """
        neighbors = [neighbor for neighbor in self._graph.neighbors(self._current_node)]
        self._target_node = random.choice(neighbors)
        if self._graph.degree(self._current_node) > 1:
            while self._target_node == self._previous_node:
                self._target_node = random.choice(neighbors)
        self._previous_node = self._current_node
        self._current_node = self._target_node
        self._sampled_nodes.add(self._current_node)

    def sample(self, graph):
        """
        Sampling nodes with a single non back-tracking random walk.

        Arg types:
            * **graph** *(NetworkX graph)* - The graph to be sampled from.

        Return types:
            * **new_graph** *(NetworkX graph)* - The graph of sampled nodes.
        """
        self._check_graph(graph)
        self._check_number_of_nodes(graph)
        self._graph = graph
        self._create_initial_node_set()
        while len(self._sampled_nodes) < self.number_of_nodes:
            self._do_a_step()
        new_graph = self._graph.subgraph(self._sampled_nodes)
        return new_graph
