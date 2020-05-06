import random
import networkx as nx
from littleballoffur.sampler import Sampler

class FrontierSampler(Sampler):
    r"""An implementation of frontier sampling.

    Args:
        number_of_nodes (int): Number of nodes. Default is 100.
        number_of_seeds (int): Number of seed nodes. Default is 10.
        seed (int): Random seed. Default is 42.
    """
    def __init__(self, number_of_nodes=100, seed=42):
        self.number_of_nodes = number_of_nodes
        self.numer_of_seeds = number_of_seeds
        self.seed = seed
        self._set_seed()

    def _create_initial_seed_set(self):
        """
        Choosing initial nodes.
        """
        nodes = [node for node in range(self._graph.number_of_nodes())]
        self._sampled_seeds = set(random.sample(nodes, self.number_of_seeds)) 
 
