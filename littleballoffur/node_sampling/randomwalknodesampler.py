import random
import networkx as nx
from littleballoffur.sampler import Sampler

class RandomWalkNodeSampler(Sampler):

    def __init__(self, number_of_nodes=100, seed=42):
        random.seed(42)
        self.number_of_nodes = number_of_nodes

    def _create_initial_node_set(self):
        self._current_node = random.choice(range(self._graph.number_of_nodes()))
        self._sampled_nodes = set([self._current_node])

    def _do_a_step(self):
        neighbors = self._graph.neighbors(self._current_node)
        self._current_node = random.choice([neighbor for neighbor in neighbors])
        self._sampled_nodes.add(self._current_node)
        

    def sample(self, graph):
        self._graph = graph
        self._create_initial_node_set()
        while len(self._sampled_nodes) < self.number_of_nodes:
            self._do_a_step()
        new_graph = self._graph.subgraph(self._sampled_nodes)
        return new_graph
        


