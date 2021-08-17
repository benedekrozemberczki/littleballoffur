import random
import numpy as np
import networkx as nx
import networkit as nk
from typing import Union
from littleballoffur.sampler import Sampler


NKGraph = type(nk.graph.Graph())
NXGraph = nx.classes.graph.Graph


class CommonNeighborAwareRandomWalkSampler(Sampler):
    r"""An implementation of node sampling by common neighbor aware random walks.
    The random walker is biased to visit neighbors that have a lower number of
    common neighbors. This way the sampling procedure is able to escape tightly
    knit communities and visit new ones. `"For details about the algorithm see this paper." <https://ieeexplore.ieee.org/document/8731555>`_

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

    def _create_sampler(self, graph):
        self._sampler = {}

    def _get_node_scores(self, graph, node):
        if node in self._sampler:  # no need to recompute
            return
        neighbors = set(self.backend.get_neighbors(graph, node))
        scores = []
        for neighbor in neighbors:
            fringe = set(self.backend.get_neighbors(graph, neighbor))
            overlap = len(neighbors.intersection(fringe))
            scores.append(
                1.0
                - (overlap)
                / min(
                    self.backend.get_degree(graph, node),
                    self.backend.get_degree(graph, neighbor),
                )
            )
        self._sampler[node] = {}
        self._sampler[node]["neighbors"] = list(neighbors)
        self._sampler[node]["scores"] = scores / np.sum(scores)

    def _do_a_step(self, graph):
        """
        Doing a single random walk step.
        """
        self._get_node_scores(graph, self._current_node)
        self._current_node = sample = np.random.choice(
            self._sampler[self._current_node]["neighbors"],
            1,
            replace=False,
            p=self._sampler[self._current_node]["scores"],
        )[0]
        self._sampled_nodes.add(self._current_node)

    def sample(
        self, graph: Union[NXGraph, NKGraph], start_node: int = None
    ) -> Union[NXGraph, NKGraph]:
        """
        Sampling nodes with a single common neighbor aware random walk.

        Arg types:
            * **graph** *(NetworkX or NetworKit graph)* - The graph to be sampled from.
            * **start_node** *(int, optional)* - The start node.

        Return types:
            * **new_graph** *(NetworkX or NetworKit graph)* - The graph of sampled nodes.
        """
        self._deploy_backend(graph)
        self._check_number_of_nodes(graph)
        self._create_initial_node_set(graph, start_node)
        self._create_sampler(graph)
        while len(self._sampled_nodes) < self.number_of_nodes:
            self._do_a_step(graph)
        new_graph = self.backend.get_subgraph(graph, self._sampled_nodes)
        return new_graph
