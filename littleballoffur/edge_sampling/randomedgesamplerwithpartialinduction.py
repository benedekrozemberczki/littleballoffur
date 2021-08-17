import random
import networkx as nx
import networkit as nk
from typing import Union
from littleballoffur import Sampler


NKGraph = type(nk.graph.Graph())
NXGraph = nx.classes.graph.Graph


class RandomEdgeSamplerWithPartialInduction(Sampler):
    r"""An implementation of random edge sampling with partial edge set induction.
    The algorithm randomly samples edges in a streaming fashion with a fixed probability.
    Edges between nodes which are already in the sample are retained with an induction step. `"For details about the algorithm see this paper." <https://dl.acm.org/doi/10.1145/2601438>`_

    Args:
        p (float): Sampling probability. Default is 0.5.
        seed (int): Random seed. Default is 42.
    """

    def __init__(self, p: float = 0.5, seed: int = 42):
        self.p = p
        self.seed = seed
        self._set_seed()

    def _create_initial_set(self, graph):
        """
        Creatin an initial edge and node set and a reshuffled edge stream.
        """
        self._nodes = set()
        self._edges = set()
        self._edge_stream = self.backend.get_edges(graph)
        random.shuffle(self._edge_stream)

    def _insert_edge(self, edge):
        """
        Adding an edge.
        """
        self._edges.add((edge[0], edge[1]))
        self._edges.add((edge[1], edge[0]))

    def _insert_nodes(self, edge):
        """
        Adding edge endpoints to the node sets.
        """
        self._nodes.add(edge[0])
        self._nodes.add(edge[1])

    def _sample_edges(self):
        """
        Creating a subsampled edge list.
        """
        for edge in self._edge_stream:
            if edge[0] in self._nodes and edge[1] in self._nodes:
                self._insert_edge(edge)
            else:
                p = random.uniform(0, 1)
                if p < self.p:
                    self._insert_nodes(edge)
                    self._insert_edge(edge)
        self._edges = [edge for edge in self._edges]

    def sample(self, graph: Union[NXGraph, NKGraph]) -> Union[NXGraph, NKGraph]:
        """
        Sampling edges randomly with partial induction.

        Arg types:
            * **graph** *(NetworkX or NetworKit graph)* - The graph to be sampled from.

        Return types:
            * **new_graph** *(NetworkX or NetworKit graph)* - The graph of sampled edges.
        """
        self._deploy_backend(graph)
        self._create_initial_set(graph)
        self._sample_edges()
        new_graph = self.backend.graph_from_edgelist(self._edges)
        return new_graph
