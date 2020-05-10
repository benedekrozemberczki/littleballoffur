import random
import numpy as np
import networkx as nx
from collections import deque
from littleballoffur.sampler import Sampler

class CirculatedNeighborsRandomWalkSampler(Sampler):
    r"""An implementation of circulated neighbor random walk sampling.

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
        self._sampled_nodes = set()
        self._current_node = random.choice(range(self._graph.number_of_nodes()))
        self._sampled_nodes.add(self._current_node)


    def _do_shuffling(self, node):
        """
        Shuffling the neighbors of a node in the circulated map.

        Arg types:
            * **node** *(int)* - The node considered.
        """
        self._circulated_map[node] = [neighbor for neighbor in self._graph.neighbors(node)]
        random.shuffle(self._circulated_map[node])

    def _create_circulated_map(self):
        self._circulated_map = {}
        for node in self._graph.nodes():
            self._do_shuffling(node)

    def _make_a_step(self):
        if len(self._circulated_map[self._current_node]) == 0:
            self._do_shuffling(self._current_node)
        self._current_node = self._circulated_map[self._current_node].pop()
        self._sampled_nodes.add(self._current_node)


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
        self._create_circulated_map()
        while len(self._sampled_nodes) < self.number_of_nodes:
             self._make_a_step()
        new_graph = graph.subgraph(self._sampled_nodes)
        return new_graph
