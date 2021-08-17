import random
import networkx as nx
import networkit as nk
from queue import Queue
from typing import Union
from littleballoffur.sampler import Sampler

NKGraph = type(nk.graph.Graph())
NXGraph = nx.classes.graph.Graph


class SnowBallSampler(Sampler):
    r"""An implementation of node sampling by snow ball search. Starting from a
    source node the algorithm places a fixed number of neighbors in a queue of
    nodes to explore. The expansion goes on until the target number of sampled
    vertices is reached. `"For details about the algorithm see this paper."
    <https://projecteuclid.org/euclid.aoms/1177705148>`_

    Args:
        number_of_nodes (int): Number of nodes. Default is 100.
        k (int): Bound on degree. Default is 50.
        seed (int): Random seed. Default is 42.
    """

    def __init__(self, number_of_nodes: int = 100, k: int = 50, seed: int = 42):
        self.number_of_nodes = number_of_nodes
        self.k = k
        self.seed = seed
        self._set_seed()

    def _create_seed_set(self, graph, start_node):
        """
        Creating a seed set of nodes.
        """
        self._queue = Queue()
        if start_node is not None:
            if start_node >= 0 and start_node < self.backend.get_number_of_nodes(graph):
                self._queue.put(start_node)
            else:
                raise ValueError("Starting node index is out of range.")
        else:
            start_node = random.choice(range(self.backend.get_number_of_nodes(graph)))
            self._queue.put(start_node)
        self._nodes = set([start_node])

    def _get_neighbors(self, graph, source):
        """
        Get the neighbors of a node (if a node has more than k neighbors we choose randomly).
        """
        neighbors = self.backend.get_neighbors(graph, source)
        random.shuffle(neighbors)
        neighbors = neighbors[0 : min(len(neighbors), self.k)]
        return neighbors

    def sample(
        self, graph: Union[NXGraph, NKGraph], start_node: int = None
    ) -> Union[NXGraph, NKGraph]:
        """
        Sampling a graph with randomized snow ball sampling.

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
            neighbors = self._get_neighbors(graph, source)
            for neighbor in neighbors:
                if neighbor not in self._nodes:
                    self._nodes.add(neighbor)
                    self._queue.put(neighbor)
                    if len(self._nodes) >= self.number_of_nodes:
                        break
        new_graph = self.backend.get_subgraph(graph, self._nodes)
        return new_graph
