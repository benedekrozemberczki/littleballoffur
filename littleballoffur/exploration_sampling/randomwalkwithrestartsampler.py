import random
import networkx as nx
from littleballoffur.sampler import Sampler

class RandomWalkWithRestartSampler(Sampler):
    r"""An implementation of node sampling by random walks with restart. The 
    process is a discrete random walker on nodes which teleports back to the
    staring node with a fixed probability. This results in a connected subsample
    from the original input graph. `"For details about the algorithm see this 
    paper." <https://cs.stanford.edu/people/jure/pubs/sampling-kdd06.pdf>`_

    Args:
        number_of_nodes (int): Number of nodes. Default is 100.
        seed (int): Random seed. Default is 42.
        p (float): Restart probability. Default is 0.1.
    """
    def __init__(self, number_of_nodes=100, seed=42, p=0.1):
        self.number_of_nodes = number_of_nodes
        self.seed = seed
        self.p = p
        self._set_seed()

    def _create_initial_node_set(self):
        """
        Choosing an initial node.
        """
        self._current_node = random.choice(range(self._graph.number_of_nodes()))
        self._initial_node = self._current_node
        self._sampled_nodes = set([self._current_node])

    def _do_a_step(self):
        """
        Doing a single random walk step.
        """
        score = random.uniform(0, 1)
        if score < self.p:
            self._current_node = self._initial_node
        else:
            neighbors = self._graph.neighbors(self._current_node)
            self._current_node = random.choice([neighbor for neighbor in neighbors])
            self._sampled_nodes.add(self._current_node)

    def sample(self, graph):
        """
        Sampling nodes with a single random walk that restarts.

        Arg types:
            * **graph** *(NetworkX graph)* - The graph to be sampled from.

        Return types:
            * **new_graph** *(NetworkX graph)* - The graph of sampled nodes.
        """
        self._check_graph(graph)
        self._check_number_of_nodes(graph)
        self._graph = graph
        self._create_initial_node_set()
        while len(self._sampled_nodes) < self.number_of_nodes:
            self._do_a_step()
        new_graph = self._graph.subgraph(self._sampled_nodes)
        return new_graph
