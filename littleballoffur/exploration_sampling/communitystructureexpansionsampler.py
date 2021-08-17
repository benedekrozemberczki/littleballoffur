import random
import numpy as np
import networkx as nx
import networkit as nk
from typing import Union
from littleballoffur.sampler import Sampler

NKGraph = type(nk.graph.Graph())
NXGraph = nx.classes.graph.Graph


class CommunityStructureExpansionSampler(Sampler):
    r"""An implementation of community structure preserving expansion sampling.
    Starting with a random source node the procedure chooses a node which is connected
    to the already sampled nodes. This node is the one with the largest community expansion
    score. The extracted subgraph is always connected. `"For details about the algorithm see this paper." <http://arun.maiya.net/papers/maiya_etal-sampcomm.pdf>`_


    Args:
        number_of_nodes (int): Number of sampled nodes. Default is 100.
        seed (int): Random seed. Default is 42.
    """

    def __init__(self, number_of_nodes: int = 100, seed: int = 42):
        self.number_of_nodes = number_of_nodes
        self.seed = seed
        self._set_seed()

    def _create_node_set(self, graph, start_node):
        """
        Choosing a seed node.
        """
        if start_node is not None:
            if start_node >= 0 and start_node < self.backend.get_number_of_nodes(graph):
                self._sampled_nodes = set([start_node])
            else:
                raise ValueError("Starting node index is out of range.")
        else:
            self._sampled_nodes = set(
                [random.choice(range(self.backend.get_number_of_nodes(graph)))]
            )

    def _make_target_set(self, graph):
        """
        Creating a new reshuffled frontier list of nodes.
        """
        self._targets = [
            neighbor
            for node in self._sampled_nodes
            for neighbor in self.backend.get_neighbors(graph, node)
        ]
        self._targets = list(set(self._targets).difference(self._sampled_nodes))
        random.shuffle(self._targets)

    def _choose_new_node(self, graph):
        """
        Choosing the node with the largest expansion.
        The randomization of the list breaks ties randomly.
        """
        largest_expansion = 0
        for node in self._targets:
            expansion = len(
                set(self.backend.get_neighbors(graph, node)).difference(
                    self._sampled_nodes
                )
            )
            if expansion >= largest_expansion:
                new_node = node
        self._sampled_nodes.add(new_node)

    def sample(
        self, graph: Union[NXGraph, NKGraph], start_node: int = None
    ) -> Union[NXGraph, NKGraph]:
        """
        Sampling nodes iteratively with a community structure expansion sampler.

        Arg types:
            * **graph** *(NetworkX or NetworKit graph)* - The graph to be sampled from.
            * **start_node** *(int, optional)* - The start node.

        Return types:
            * **new_graph** *(NetworkX or NetworKit graph)* - The graph of sampled nodes.
        """
        self._deploy_backend(graph)
        self._check_number_of_nodes(graph)
        self._create_node_set(graph, start_node)
        while len(self._sampled_nodes) < self.number_of_nodes:
            self._make_target_set(graph)
            self._choose_new_node(graph)
        new_graph = self.backend.get_subgraph(graph, self._sampled_nodes)
        return new_graph
