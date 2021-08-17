import random
import networkx as nx
import networkit as nk
from typing import Union, List
from littleballoffur.sampler import Sampler


NKGraph = type(nk.graph.Graph())
NXGraph = nx.classes.graph.Graph


class RandomNodeSampler(Sampler):
    r"""An implementation of random node sampling. Nodes are sampled with uniform
    probability. `"For details about the algorithm see this paper." <https://www.pnas.org/content/102/12/4221>`_

    Args:
        number_of_nodes (int): Number of nodes. Default is 100.
        seed (int): Random seed. Default is 42.
    """

    def __init__(self, number_of_nodes: int = 100, seed: int = 42):
        self.number_of_nodes = number_of_nodes
        self.seed = seed
        self._set_seed()

    def _create_initial_node_set(self, graph) -> List[int]:
        """
        Choosing initial nodes.
        """
        nodes = self.backend.get_nodes(graph)
        sampled_nodes = random.sample(nodes, self.number_of_nodes)
        return sampled_nodes

    def sample(self, graph: Union[NXGraph, NKGraph]) -> Union[NXGraph, NKGraph]:
        """
        Sampling nodes randomly.

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
