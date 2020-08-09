import random
import networkx as nx
import networkit as nk
from typing import Union
from queue import Queue 
from littleballoffur.sampler import Sampler


NKGraph = type(nk.graph.Graph())
NXGraph = nx.classes.graph.Graph


class BreadthFirstSearchSampler(Sampler):
    r"""An implementation of node sampling by breadth first search. The starting node
    is selected randomly and neighbors are added to the queue by shuffling them randomly.

    Args:
        number_of_nodes (int): Number of nodes. Default is 100.
        seed (int): Random seed. Default is 42.
    """
    def __init__(self, number_of_nodes: int=100, seed: int=42):
        self.number_of_nodes = number_of_nodes
        self.seed = seed
        self._set_seed()


    def _create_seed_set(self, graph):
        """
        Creating seed sets of nodes and edges.
        """
        self._queue = Queue()
        start_node = random.choice(range(self.backend.get_number_of_nodes(graph)))
        self._queue.put(start_node)
        self._nodes = set([start_node])
        self._edges = set()  


    def sample(self, graph: Union[NXGraph, NKGraph]) -> Union[NXGraph, NKGraph]:
        """
        Sampling a graph with randomized breadth first search.

        Arg types:
            * **graph** *(NetworkX or NetworKit graph)* - The graph to be sampled from.

        Return types:
            * **new_graph** *(NetworkX or NetworKit graph)* - The graph of sampled nodes.
        """
        self._deploy_backend(graph)
        self._check_number_of_nodes(graph)
        self._create_seed_set(graph)
        while len(self._nodes) < self.number_of_nodes:
            source = self._queue.get()
            neighbors = self.backend.get_neighbors(graph, source)
            random.shuffle(neighbors)
            for neighbor in neighbors:
                if neighbor not in self._nodes:
                    self._nodes.add(neighbor)
                    self._edges.add((source, neighbor))
                    self._queue.put(neighbor)
                    if len(self._nodes) >= self.number_of_nodes:
                        break
        new_graph = self.backend.graph_from_edgelist(self._edges)
        new_graph = self.backend.get_subgraph(new_graph, self._sampled_nodes)
        return new_graph


