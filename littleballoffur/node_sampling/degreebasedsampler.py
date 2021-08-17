import random
import numpy as np
import networkx as nx
import networkit as nk
from typing import Union, List
from littleballoffur.sampler import Sampler

NKGraph = type(nk.graph.Graph())
NXGraph = nx.classes.graph.Graph


class DegreeBasedSampler(Sampler):
    r"""An implementation of degree based sampling. Nodes are sampled proportional
    to the degree centrality of nodes. `"For details about the algorithm see
    this paper." <https://arxiv.org/abs/cs/0103016>`_

    Args:
        number_of_nodes (int): Number of nodes. Default is 100.
        seed (int): Random seed. Default is 42.
    """

    def __init__(self, number_of_nodes: int = 100, seed: int = 42):
        self.number_of_nodes = number_of_nodes
        self.seed = seed
        self._set_seed()

    def _create_initial_node_set(self, graph: Union[NXGraph, NKGraph]) -> List[int]:
        """
        Choosing initial nodes.
        """
        nodes = [node for node in range(self.backend.get_number_of_nodes(graph))]
        degrees = [float(self.backend.get_degree(graph, node)) for node in nodes]
        degree_sum = sum(degrees)
        degrees = [degree / degree_sum for degree in degrees]
        sampled_nodes = np.random.choice(
            nodes, size=self.number_of_nodes, replace=False, p=degrees
        )
        return sampled_nodes

    def sample(self, graph: Union[NXGraph, NKGraph]) -> Union[NXGraph, NKGraph]:
        """
        Sampling nodes proportional to the degree.

        Arg types:
            * **graph** *(NetworkX or NetworKit graph)* - The graph to be sampled from.

        Return types:
            * **new_graph** *(NetworkX or NetworKit graph)* - The graph of sampled nodes.
        """
        self._deploy_backend(graph)
        self._check_number_of_nodes(graph)
        sampled_nodes = self._create_initial_node_set(graph)
        new_graph = self.backend.get_subgraph(graph, sampled_nodes)
        return new_graph
