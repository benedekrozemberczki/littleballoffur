import random
import networkx as nx
from littleballoffur.sampler import Sampler

class RandomWalkNodeSampler(Sampler):
    """
    
    """
    def __init__(self, number_of_nodes=100, seed=42):
        self.seed = seed
        self.number_of_nodes = number_of_nodes
        self._set_seed()

    def _set_seed(self)
        """
        Creating the initial random seed.
        """
        random.seed(self.seed)

    def _create_initial_node_set(self):
        """
        Choosing an initial node.
        """
        self._current_node = random.choice(range(self._graph.number_of_nodes()))
        self._sampled_nodes = set([self._current_node])

    def _do_a_step(self):
        """
        Doing a single random walk step.
        """
        neighbors = self._graph.neighbors(self._current_node)
        self._current_node = random.choice([neighbor for neighbor in neighbors])
        self._sampled_nodes.add(self._current_node)

    def sample(self, graph):
        """
        Sampling nodes with random walks.

        Arg types:
            * **graph** *(NetworkX graph)* - The graph to be sampled from.

        Return types:
            * **new_graph* *(NetworkX graph)* - The graph of sampled nodes.
        """
        self._graph = graph
        self._create_initial_node_set()
        while len(self._sampled_nodes) < self.number_of_nodes:
            self._do_a_step()
        new_graph = self._graph.subgraph(self._sampled_nodes)
        return new_graph
        


