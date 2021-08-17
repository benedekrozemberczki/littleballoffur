import random
import networkx as nx
import networkit as nk
from typing import Union
from littleballoffur.sampler import Sampler


NKGraph = type(nk.graph.Graph())
NXGraph = nx.classes.graph.Graph


class CirculatedNeighborsRandomWalkSampler(Sampler):
    r"""An implementation of circulated neighbor random walk sampling. The process
    simulates a random walker. Vertices of a neighbourhood are randomly reshuffled
    after all of them is sampled from the vicinity of a node. This way the walker
    can escape closely knit communities. `"For details about the algorithm see
    this paper." <https://dl.acm.org/doi/10.5555/2794367.2794373>`_

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

    def _do_shuffling(self, graph, node):
        """
        Shuffling the neighbors of a node in the circulated map.

        Arg types:
            * **node** *(int)* - The node considered.
        """
        self._circulated_map[node] = self.backend.get_neighbors(graph, node)
        random.shuffle(self._circulated_map[node])

    def _create_circulated_map(self, graph):
        """
        Creating an initial random shuffle node-neighbor map.
        """
        self._circulated_map = {}
        for node in self.backend.get_node_iterator(graph):
            self._do_shuffling(graph, node)

    def _make_a_step(self, graph):
        """
        Doing a single step of the circulated neighbor random walk.
        """
        if len(self._circulated_map[self._current_node]) == 0:
            self._do_shuffling(graph, self._current_node)
        self._current_node = self._circulated_map[self._current_node].pop()
        self._sampled_nodes.add(self._current_node)

    def sample(
        self, graph: Union[NXGraph, NKGraph], start_node: int = None
    ) -> Union[NXGraph, NKGraph]:
        """
        Sampling nodes iteratively with a circulated neighbor random walk sampler.

        Arg types:
            * **graph** *(NetworkX or NetworKit graph)* - The graph to be sampled from.
            * **start_node** *(int, optional)* - The start node.

        Return types:
            * **new_graph** *(NetworkX or NetworKit graph)* - The graph of sampled nodes.
        """
        self._deploy_backend(graph)
        self._check_number_of_nodes(graph)
        self._create_node_set(graph, start_node)
        self._create_circulated_map(graph)
        while len(self._sampled_nodes) < self.number_of_nodes:
            self._make_a_step(graph)
        new_graph = self.backend.get_subgraph(graph, self._sampled_nodes)
        return new_graph
