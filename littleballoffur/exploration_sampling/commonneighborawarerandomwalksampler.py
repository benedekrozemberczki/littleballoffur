import random
import numpy as np
import networkx as nx
from littleballoffur.sampler import Sampler

class CommonNeighborAwareRandomWalkSampler(Sampler):
    r"""An implementation of node sampling by common neighbor aware random walks.

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


    def _create_sampler(self):
        self._sampler = {}
        for node in self._graph.nodes():
            neighbors = [neighbor for neighbor in self._graph.neighbors(node)]
            neighbors = set(neighbors)
            print(neighbors)
            scores = []
            for neighbor in neighbors:
                fringe = set([neb for neb in self._graph.neighbors(neighbor)])
                overlap = len(neighbors.intersection(fringe))
                scores.append((overlap+1)/min(self._graph.degree(node)+1,self._graph.degree(neighbor)+1))
            scores = np.array(scores)/sum(scores)
            self._sampler[node] = {}
            self._sampler[node]["neighbors"] = neighbors
            self._sampler[node]["scores"] = scores
        

    def _do_a_step(self):
        """
        Doing a single random walk step.
        """
        self._current_node = sample = np.random.choice(self._sampler[node]["neighbors"], 1, replace=False, p=self._sampler[node]["scores"])[0]
        self._sampled_nodes.add(self._current_node)

    def sample(self, graph):
        """
        Sampling nodes with a single common neighbor aware random walk.

        Arg types:
            * **graph** *(NetworkX graph)* - The graph to be sampled from.

        Return types:
            * **new_graph** *(NetworkX graph)* - The graph of sampled nodes.
        """
        self._check_graph(graph)
        self._check_number_of_nodes(graph)
        self._graph = graph
        self._create_initial_node_set()
        self._create_sampler()
        while len(self._sampled_nodes) < self.number_of_nodes:
            self._do_a_step()
        new_graph = self._graph.subgraph(self._sampled_nodes)
        return new_graph
