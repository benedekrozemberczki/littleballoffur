import random
import numpy as np
import networkx as nx
from littleballoffur.sampler import Sampler

class PageRankBasedSampler(Sampler):
    r"""An implementation of PageRank based sampling. Nodes are sampled proportional
    to the PageRank score of nodes. `"For details about the algorithm see 
    this paper." <https://cs.stanford.edu/people/jure/pubs/sampling-kdd06.pdf>`_

    Args:
        number_of_nodes (int): Number of nodes. Default is 100.
        seed (int): Random seed. Default is 42.
    """
    def __init__(self, number_of_nodes: int=100, seed: int=42):
        self.number_of_nodes = number_of_nodes
        self.seed = seed
        self._set_seed()

    def _create_initial_node_set(self):
        """
        Choosing initial nodes.
        """
        nodes = [node for node in range(self._graph.number_of_nodes())]
        page_rank = nx.pagerank_scipy(self._graph)
        page_rank_sum = sum(page_rank.values())
        probabilities = [page_rank[node]/page_rank_sum for node in nodes]
        self._sampled_nodes = np.random.choice(nodes, size=self.number_of_nodes, replace=False, p=probabilities)

    def sample(self, graph: nx.classes.graph.Graph) -> nx.classes.graph.Graph:
        """
        Sampling nodes randomly.

        Arg types:
            * **graph** *(NetworkX graph)* - The graph to be sampled from.

        Return types:
            * **new_graph** *(NetworkX graph)* - The graph of sampled nodes.
        """
        self._check_graph(graph)
        self._check_number_of_nodes(graph)
        self._graph = graph
        self._create_initial_node_set()
        new_graph = self._graph.subgraph(self._sampled_nodes)
        return new_graph
