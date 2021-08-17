import random
import networkx as nx
import networkit as nk
from typing import Union
from littleballoffur.sampler import Sampler


NKGraph = type(nk.graph.Graph())
NXGraph = nx.classes.graph.Graph


class NonBackTrackingRandomWalkSampler(Sampler):
    r"""An implementation of node sampling by non back-tracking random walks.
    The process generates a random walk in which the random walker cannot make steps
    backwards. This way the tottering behaviour of random walkers can be avoided.
    `"For details about the algorithm see this paper." <https://dl.acm.org/doi/10.1145/2318857.2254795>`_


    Args:
        number_of_nodes (int): Number of nodes. Default is 100.
        seed (int): Random seed. Default is 42.
    """

    def __init__(self, number_of_nodes: int = 100, seed: int = 42):
        self.number_of_nodes = number_of_nodes
        self.seed = seed
        self._set_seed()

    def _create_initial_node_set(self, graph, start_node):
        """
        Choosing an initial node.
        """
        if start_node is not None:
            if start_node >= 0 and start_node < self.backend.get_number_of_nodes(graph):
                self._current_node = start_node
                self._sampled_nodes = set([self._current_node])
            else:
                raise ValueError("Starting node index is out of range.")
        else:
            self._current_node = random.choice(
                range(self.backend.get_number_of_nodes(graph))
            )
            self._sampled_nodes = set([self._current_node])
        self._previous_node = -1

    def _do_a_step(self, graph):
        """
        Doing a single non back-tracking random walk step.
        """
        neighbors = self.backend.get_neighbors(graph, self._current_node)
        self._target_node = random.choice(neighbors)
        if self.backend.get_degree(graph, self._current_node) > 1:
            while self._target_node == self._previous_node:
                self._target_node = random.choice(neighbors)
        self._previous_node = self._current_node
        self._current_node = self._target_node
        self._sampled_nodes.add(self._current_node)

    def sample(
        self, graph: Union[NXGraph, NKGraph], start_node: int = None
    ) -> Union[NXGraph, NKGraph]:
        """
        Sampling nodes with a single non back-tracking random walk.

        Arg types:
            * **graph** *(NetworkX or NetworKit graph)* - The graph to be sampled from.
            * **start_node** *(int, optional)* - The start node.

        Return types:
            * **new_graph** *(NetworkX or NetworKit graph)* - The graph of sampled edges.
        """
        self._deploy_backend(graph)
        self._check_number_of_nodes(graph)
        self._create_initial_node_set(graph, start_node)
        while len(self._sampled_nodes) < self.number_of_nodes:
            self._do_a_step(graph)
        new_graph = self.backend.get_subgraph(graph, self._sampled_nodes)
        return new_graph
