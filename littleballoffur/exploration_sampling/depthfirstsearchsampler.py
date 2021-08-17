import random
import networkx as nx
import networkit as nk
from typing import Union
from queue import LifoQueue
from littleballoffur.sampler import Sampler

NKGraph = type(nk.graph.Graph())
NXGraph = nx.classes.graph.Graph


class DepthFirstSearchSampler(Sampler):
    r"""An implementation of node sampling by depth first search. The starting node
    is selected randomly and neighbors are added to the last in first out queue
    by shuffling them randomly.

    Args:
        number_of_nodes (int): Number of nodes. Default is 100.
        seed (int): Random seed. Default is 42.
    """

    def __init__(self, number_of_nodes: int = 100, seed: int = 42):
        self.number_of_nodes = number_of_nodes
        self.seed = seed
        self._set_seed()

    def _create_seed_set(self, graph, start_node):
        """
        Creating a visited node set and a traversal path list.
        """
        self._queue = LifoQueue()
        if start_node is not None:
            if start_node >= 0 and start_node < self.backend.get_number_of_nodes(graph):
                self._queue.put(start_node)
            else:
                raise ValueError("Starting node index is out of range.")
        else:
            start_node = random.choice(range(self.backend.get_number_of_nodes(graph)))
            self._queue.put(start_node)
        self._nodes = set()
        self._path = []

    def _extract_edges(self):
        """
        Extracting edges from the depth first search tree.
        """
        self._edges = [
            [self._path[i], self._path[i + 1]] for i in range(len(self._path) - 1)
        ]

    def sample(
        self, graph: Union[NXGraph, NKGraph], start_node: int = None
    ) -> Union[NXGraph, NKGraph]:
        """
        Sampling a graph with randomized depth first search.

        Arg types:
            * **graph** *(NetworkX or NetworKit graph)* - The graph to be sampled from.
            * **start_node** *(int, optional)* - The start node.

        Return types:
            * **new_graph** *(NetworkX or NetworKit graph)* - The graph of sampled nodes.
        """
        self._deploy_backend(graph)
        self._check_number_of_nodes(graph)
        self._create_seed_set(graph, start_node)
        while len(self._nodes) < self.number_of_nodes:
            source = self._queue.get()
            if source not in self._nodes:
                neighbors = self.backend.get_neighbors(graph, source)
                random.shuffle(neighbors)
                for neighbor in neighbors:
                    self._queue.put(neighbor)
                self._nodes.add(source)
                self._path.append(source)
        self._extract_edges()
        if len(self._edges) > 0:
            new_graph = self.backend.graph_from_edgelist(self._edges)
            new_graph = self.backend.get_subgraph(new_graph, self._nodes)
        else:
            new_graph = self.backend.get_subgraph(graph, self._nodes)
        return new_graph
