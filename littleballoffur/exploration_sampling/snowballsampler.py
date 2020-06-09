import random
import networkx as nx
from queue import Queue 
from littleballoffur.sampler import Sampler

class SnowBallSampler(Sampler):
    r"""An implementation of node sampling by snow ball search.

    Args:
        number_of_nodes (int): Number of nodes. Default is 100.
        k (int): Bound on degree. Default is 50.
        seed (int): Random seed. Default is 42.
    """
    def __init__(self, number_of_nodes=100, k=50, seed=42):
        self.number_of_nodes = number_of_nodes
        self.k = k
        self.seed = seed
        self._set_seed()


    def _create_seed_set(self):
        """
        Creating a seed set of nodes.
        """
        self._queue = Queue()
        start_node = random.choice(range(self._graph.number_of_nodes()))
        self._queue.put(start_node)
        self._nodes = set([start_node])


    def _get_neighbors(self, source):
        """
        Get the neighbors of a node (if a node has more than k neighbors we choose randomly).
        """
        neighbors = [node for node in self._graph.neighbors(source)]
        random.shuffle(neighbors)
        neighbors = neighbors[0:min(len(neighbors), self.k)]
        return neighbors


    def sample(self, graph):
        """
        Sampling a graph with randomized snow ball sampling.

        Arg types:
            * **graph** *(NetworkX graph)* - The graph to be sampled from.

        Return types:
            * **new_graph** *(NetworkX graph)* - The graph of sampled nodes.
        """
        self._check_graph(graph)
        self._check_number_of_nodes(graph)
        self._graph = graph
        self._create_seed_set()
        while len(self._nodes) < self.number_of_nodes:
            source = self._queue.get()
            neighbors = self._get_neighbors(source)
            for neighbor in neighbors:
                if neighbor not in self._nodes:
                    self._nodes.add(neighbor)
                    self._queue.put(neighbor)
                    if len(self._nodes) >= self.number_of_nodes:
                        break
        new_graph = self._graph.subgraph(self._nodes)
        return new_graph


