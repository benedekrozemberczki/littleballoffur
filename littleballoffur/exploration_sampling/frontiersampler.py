import random
import numpy as np
import networkx as nx
from littleballoffur.sampler import Sampler

class FrontierSampler(Sampler):
    r"""An implementation of frontier sampling.

    Args:
        number_of_seeds (int): Number of seed nodes. Default is 3.
        number_of_nodes (int): Number of sampling steps. Default is 100.
        seed (int): Random seed. Default is 42.
    """
    def __init__(self, number_of_seeds=3, number_of_nodes=100, seed=42):
        self.number_of_seeds = number_of_seeds
        self.number_of_nodes = number_of_nodes
        self.seed = seed
        self._set_seed()


    def _reweight(self):
        self._seed_weights = [self._graph.degree(seed) for seed in self._seeds]
        weight_sum = np.sum(self._seed_weights)
        self._seed_weights = [float(weight)/weight_sum for weight in self._seed_weights]

    def _create_initial_seed_set(self):
        """
        Choosing initial nodes.
        """
        nodes = [node for node in range(self._graph.number_of_nodes())]
        self._seeds = random.sample(nodes, self.number_of_seeds)

    def _do_update(self):
        sample = np.random.choice(self._seeds, 1, replace=False, p=self._seed_weights)[0]
        index = self._seeds.index(sample)
        new_seed = random.choice([neb for neb in self._graph.neighbors(sample)])
        self._edges.add((sample, new_seed))
        self._nodes.add(sample)
        self._nodes.add(new_seed)
        self._seeds[index] = new_seed

 
    def sample(self, graph):
        self._check_graph(graph)
        self._check_number_of_nodes(graph)
        self._nodes = set()
        self._edges = set()
        self._graph = graph
        self._create_initial_seed_set()
        while len(self._nodes) < self.number_of_nodes:
            self._reweight()
            self._do_update()
        new_graph = nx.from_edgelist(self._edges)
        print(nx.transitivity(new_graph))
