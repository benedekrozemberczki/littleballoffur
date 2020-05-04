import random
import networkx as nx
from littleballoffur.sampler import Sampler

class RandomWalkNodeSampler(Sampler):

    def __init__(self, number_of_nodes=100, seed=42):
        random.seed(42)
        self.number_of_nodes = number_of_nodes

    def _create_initial_node_set(self):
        self.current_node = random.choice(range(self.graph.number_of_nodes()))
        self._sampled_nodes = set([self.current_node])

    def _do_a_step():
        neighbors = self.graph.neighbors(node)
        print(neighbors)
        

    def sample(self, graph):
        self._graph = graph
        self._create_initial_node_set()
        while len(sampled_nodes) < self.number_of_nodes:
            self._do_a_step()


