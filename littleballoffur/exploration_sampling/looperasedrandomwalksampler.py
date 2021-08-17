import random
import networkx as nx
import networkit as nk
from typing import Union
from littleballoffur.sampler import Sampler


NKGraph = type(nk.graph.Graph())
NXGraph = nx.classes.graph.Graph


class LoopErasedRandomWalkSampler(Sampler):
    r"""An implementation of node sampling by loop-erased random walks. The random
    walkers samples a fixed number of nodes. Only edges that connect so far unconnected
    nodes to the sampled node set are added to the edge set (cycles are erased). The resulting graph is always
    an undirected tree. `"For details about the algorithm see this paper." <https://link.springer.com/chapter/10.1007/978-1-4612-2168-5_12>`_

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
        self._sampled_edges = set()

    def _do_a_step(self, graph):
        """
        Doing a single random walk step.
        """
        new_node = self.backend.get_random_neighbor(graph, self._current_node)
        if (
            new_node not in self._sampled_nodes
            and self._current_node in self._sampled_nodes
        ):
            edge = sorted([self._current_node, new_node])
            self._sampled_edges.add((edge[0], edge[1]))
            self._sampled_nodes.add(new_node)
        self._current_node = new_node

    def sample(
        self, graph: Union[NXGraph, NKGraph], start_node: int = None
    ) -> Union[NXGraph, NKGraph]:
        """
        Sampling nodes with a single loop-erased random walk.

        Arg types:
            * **graph** *(NetworkX or NetworKit graph)* - The graph to be sampled from.
            * **start_node** *(int, optional)* - The start node.

        Return types:
            * **new_graph** *(NetworkX or NetworKit graph)* - The graph of sampled edges.
        """
        self._deploy_backend(graph)
        self._check_number_of_nodes(graph)
        self._create_initial_node_set(graph, start_node)
        while len(self._sampled_nodes) < self.number_of_nodes:
            self._do_a_step(graph)
        new_graph = self.backend.graph_from_edgelist(self._sampled_edges)
        new_graph = self.backend.get_subgraph(new_graph, self._sampled_nodes)
        return new_graph
