import random
import networkx as nx
import networkit as nk
from typing import Union
from littleballoffur.sampler import Sampler

NKGraph = type(nk.graph.Graph())
NXGraph = nx.classes.graph.Graph


class RandomNodeEdgeSampler(Sampler):
    r"""An implementation of random node-edge sampling. The algorithm first randomly
    samples a node. From this node it samples an edge with a neighbor. `"For details about the algorithm see
    this paper." <http://www.cs.ucr.edu/~michalis/PAPERS/sampling-networking-05.pdf>`_

    Args:
        number_of_edges (int): Number of edges. Default is 100.
        seed (int): Random seed. Default is 42.
    """

    def __init__(self, number_of_edges: int = 100, seed: int = 42):
        self.number_of_edges = number_of_edges
        self.seed = seed
        self._set_seed()

    def _create_initial_edge_set(self, graph: Union[NXGraph, NKGraph]):
        """
        Choosing initial edges.
        """
        self._sampled_edges = set()
        while len(self._sampled_edges) < self.number_of_edges:
            source_node = random.choice(range(self.backend.get_number_of_nodes(graph)))
            target_node = random.choice(self.backend.get_neighbors(graph, source_node))
            edge = sorted([source_node, target_node])
            edge = tuple(edge)
            self._sampled_edges.add(edge)

    def sample(self, graph: Union[NXGraph, NKGraph]) -> Union[NXGraph, NKGraph]:
        """
        Sampling edges randomly from randomly sampled nodes.

        Arg types:
            * **graph** *(NetworkX or NetworKit graph)* - The graph to be sampled from.

        Return types:
            * **new_graph** *(NetworkX or NetworKit graph)* - The graph of sampled edges.
        """
        self._deploy_backend(graph)
        self._check_number_of_edges(graph)
        self._create_initial_edge_set(graph)
        new_graph = self.backend.graph_from_edgelist(self._sampled_edges)
        return new_graph
