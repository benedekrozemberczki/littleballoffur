import random
import networkx as nx
import networkit as nk
from typing import Union
from littleballoffur.sampler import Sampler

NKGraph = type(nk.graph.Graph())
NXGraph = nx.classes.graph.Graph


class RandomNodeNeighborSampler(Sampler):
    r"""An implementation of random node-neighbor sampling. The process uniformly
    samples  a fixed number of nodes first. Later it induces the neighboring nodes
    as the node set and the edges between all of the nodes. `"For details about the algorithm see this paper." <https://cs.stanford.edu/people/jure/pubs/sampling-kdd06.pdf>`_


    Args:
        number_of_nodes (int): Number of nodes. Default is 100.
        seed (int): Random seed. Default is 42.
    """

    def __init__(self, number_of_nodes: int = 100, seed: int = 42):
        self.number_of_nodes = number_of_nodes
        self.seed = seed
        self._set_seed()

    def _create_initial_node_set(self, graph):
        """
        Choosing initial nodes.
        """
        nodes = self.backend.get_nodes(graph)
        self._sampled_nodes = random.sample(nodes, self.number_of_nodes)
        neighbors = [
            neighbor
            for node in self._sampled_nodes
            for neighbor in self.backend.get_neighbors(graph, node)
        ]
        self._sampled_nodes = set(self._sampled_nodes + neighbors)

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
        self._create_initial_node_set(graph)
        new_graph = self.backend.get_subgraph(graph, self._sampled_nodes)
        return new_graph
