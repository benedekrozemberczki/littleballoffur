import random
import networkx as nx
from littleballoffur import Sampler

class RandomEdgeSamplerWithPartialInduction(Sampler):
    r"""An implementation of random edge sampling with partial edge set induction.

    Args:
        p (float): Sampling probability. Default is 0.5.
        seed (int): Random seed. Default is 42.
    """
    def __init__(self, p=0.5, seed=42):
        self.p = p
        self.seed = seed
        self._set_seed()

    def _create_initial_set(self):
        """
        Creatin an initial edge and node set and a reshuffled edge stream.
        """
        self._nodes = set()
        self._edges = set()
        self._edge_stream = [edge for edge in self._graph.edges()]
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

    def sample(self, graph):
        """
        Sampling edges randomly with partial induction.

        Arg types:
            * **graph** *(NetworkX graph)* - The graph to be sampled from.

        Return types:
            * **new_graph** *(NetworkX graph)* - The graph of sampled edges.
        """
        self._check_graph(graph)
        self._check_number_of_edges(graph)
        self._graph = graph
        self._create_initial_set()
        self._sample_edges()
        new_graph = nx.from_edgelist(self._edges)
        return new_graph
