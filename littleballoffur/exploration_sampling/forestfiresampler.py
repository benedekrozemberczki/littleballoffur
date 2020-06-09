import random
import numpy as np
import networkx as nx
from collections import deque
from littleballoffur.sampler import Sampler

class ForestFireSampler(Sampler):
    r"""An implementation of forest fire sampling.

    Args:
        number_of_nodes (int): Number of sampled nodes. Default is 100.
        p (float): Burning probability. Default is 0.4.
        seed (int): Random seed. Default is 42.
    """
    def __init__(self, number_of_nodes=100, p=0.4, seed=42):
        self.number_of_nodes = number_of_nodes
        self.p = p
        self.seed = seed
        self._set_seed()

    def _create_node_sets(self):
        """
        Create a starting set of nodes.
        """
        self._sampled_nodes = set()
        self._set_of_nodes = set(range(self._graph.number_of_nodes()))

    def _start_a_fire(self):
        """
        Starting a forest fire from a single node.
        """
        remaining_nodes = list(self._set_of_nodes.difference(self._sampled_nodes))
        seed_node = random.choice(remaining_nodes)
        self._sampled_nodes.add(seed_node)
        node_queue = deque([seed_node])
        while node_queue and (len(self._sampled_nodes) < self.number_of_nodes):
            top_node = node_queue.popleft()
            self._sampled_nodes.add(top_node)
            neighbors = {neb for neb in self._graph.neighbors(top_node)}
            unvisited_neighbors = neighbors.difference(self._sampled_nodes)
            score = np.random.geometric(self.p)
            count = min(len(unvisited_neighbors), score)
            neighbors = random.sample(unvisited_neighbors, count)
            for neighbor in neighbors:
                if len(self._sampled_nodes) > self.number_of_nodes:
                    break
                node_queue.extend([neighbor])

    def sample(self, graph):
        """
        Sampling nodes iteratively with a forest fire sampler.

        Arg types:
            * **graph** *(NetworkX graph)* - The graph to be sampled from.

        Return types:
            * **new_graph** *(NetworkX graph)* - The graph of sampled nodes.
        """
        self._check_graph(graph)
        self._check_number_of_nodes(graph)
        self._graph = graph
        self._create_node_sets()
        while len(self._sampled_nodes) < self.number_of_nodes:
            self._start_a_fire()
        new_graph = self._graph.subgraph(self._sampled_nodes)
        return new_graph
