import networkx as nx
import networkit as nk
from typing import Union, List
from littleballoffur.edge_sampling import RandomEdgeSampler


NKGraph = type(nk.graph.Graph())
NXGraph = nx.classes.graph.Graph


class RandomEdgeSamplerWithInduction(RandomEdgeSampler):
    r"""An implementation of random edge sampling with edge set induction. The
    algorithm randomly samples edges with a fixed probability. Edges between nodes
    which are already in the sample are retained with an induction step. `"For details
    about the algorithm see this paper." <https://dl.acm.org/doi/10.1145/2601438>`_

    Args:
        number_of_edges (int): Number of edges. Default is 100.
        seed (int): Random seed. Default is 42.
    """

    def __init__(self, number_of_edges: int = 100, seed: int = 42):
        self.number_of_edges = number_of_edges
        self.seed = seed
        self._set_seed()

    def _induce_graph(self, graph) -> Union[NXGraph, NKGraph]:
        """
        Inducing all of the edges given the sampled edges
        """
        nodes = set([node for edge in self._sampled_edges for node in edge])
        new_graph = self.backend.get_subgraph(graph, nodes)
        return new_graph

    def sample(self, graph: Union[NXGraph, NKGraph]) -> Union[NXGraph, NKGraph]:
        """
        Sampling edges randomly with induction.

        Arg types:
            * **graph** *(NetworkX graph)* - The graph to be sampled from.

        Return types:
            * **new_graph** *(NetworkX graph)* - The graph of sampled edges.
        """
        self._deploy_backend(graph)
        self._check_number_of_edges(graph)
        self._create_initial_edge_set(graph)
        new_graph = self._induce_graph(graph)
        return new_graph
