import random
from littleballoffur.sampler import Sampler


class SpikyBallSampler(Sampler):
    def __init__(self, number_of_nodes=100, sampling_probability=0.4, initial_nodes_ratio=0.1, seed=42, max_hops=100000):
        self.number_of_nodes = number_of_nodes
        self.sampling_probability = sampling_probability
        self.initial_nodes_ratio = initial_nodes_ratio
        self.max_hops = max_hops
        self.seed = seed
        self._set_seed()

    def _create_node_sets(self):
        """
        Create a starting set of nodes.
        """
        self._sampled_nodes = set()
        self._set_of_nodes = set(range(self._graph.number_of_nodes()))
        num_initial_nodes = max(int(self._graph.number_of_nodes()*self.initial_nodes_ratio), 1)
        self._seed_nodes = random.choices(self._set_of_nodes, k=num_initial_nodes)


    def _process_hops(self):
        hop_cnt = 0
        last_layer_nodes = self._seed_nodes
        while hop_cnt < self.max_hops and len(self._sampled_nodes) < self.number_of_nodes:
            new_nodes = set()
            for node in last_layer_nodes:
                new_nodes.update(self._graph.neighbors(node))
            confirmed_nodes = new_nodes.intersection(self._sampled_nodes)
            self._sampled_nodes.update(confirmed_nodes)
            next_layer_nodes = new_nodes.difference(confirmed_nodes)
            # TODO add attributed sampling and variants
            last_layer_nodes = random.choices(next_layer_nodes,
                                              k=int(self.sampling_probability*len(next_layer_nodes)))
            hop_cnt += 1


    def sample(self, graph):
        self._check_graph(graph)
        self._check_number_of_nodes(graph)
        self._graph = graph
        self._create_node_sets()
        self._sampled_nodes.update(self._seed_nodes)
        self._process_hops()
        new_graph = self._graph.subgraph(self._sample_nodes)
        return new_graph
