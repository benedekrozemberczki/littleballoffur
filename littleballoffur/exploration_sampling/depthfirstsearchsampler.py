import random
import networkx as nx
from queue import LifoQueue
from littleballoffur.sampler import Sampler

class DepthFirstSearchSampler(Sampler):
    r"""An implementation of node sampling by depth first search. The starting node
    is selected randomly and neighbors are added to the last in first out queue 
    by shuffling them randomly.

    Args:
        number_of_nodes (int): Number of nodes. Default is 100.
        seed (int): Random seed. Default is 42.
    """
    def __init__(self, number_of_nodes: int=100, seed: int=42):
        self.number_of_nodes = number_of_nodes
        self.seed = seed
        self._set_seed()

    def _create_seed_set(self):
        """
        Creating a visited node set and a traversal path list.
        """
        self._queue = LifoQueue()
        start_node = random.choice(range(self._graph.number_of_nodes()))
        self._queue.put(start_node)
        self._nodes = set()
        self._path = [] 

    def _extract_edges(self):
        """
        Extracting edges from the depth first search tree.
        """
        self._edges = [[self._path[i],self._path[i+1]] for i in range(len(self._path)-1)]

    def sample(self, graph: nx.classes.graph.Graph) -> nx.classes.graph.Graph:
        """
        Sampling a graph with randomized depth first search.

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
            if source not in self._nodes:
                neighbors = [node for node in self._graph.neighbors(source)]
                random.shuffle(neighbors)
                for neighbor in neighbors:
                    self._queue.put(neighbor)
                self._nodes.add(source)
                self._path.append(source)
        self._extract_edges()
        new_graph = nx.from_edgelist(self._edges)
        return new_graph


