import random
from littleballoffur.sampler import Sampler
import networkx as nx
import numpy as np
import itertools

class SpikyBallSampler(Sampler):
    def __init__(self, number_of_nodes: int=100, sampling_probability: float=0.2, initial_nodes_ratio: float=0.1,
                 seed: int=42, max_hops: int=100000, mode: str='fireball'):
        self.number_of_nodes = number_of_nodes
        self.sampling_probability = sampling_probability
        self.initial_nodes_ratio = initial_nodes_ratio
        self.max_hops = max_hops
        self.seed = seed
        self.mode = mode
        self._set_seed()

    def _create_node_sets(self):
        """
        Create a starting set of nodes.
        """
        self._sampled_nodes = set()
        self._set_of_nodes = set(range(self._graph.number_of_nodes()))
        num_initial_nodes = max(int(self._graph.number_of_nodes()*self.initial_nodes_ratio), 1)
        self._seed_nodes = set(np.random.choice(list(self._set_of_nodes), num_initial_nodes, replace=False))

    def _get_new_edges(self, nodes):
        # build edge list
        edges = {}
        for node in nodes:
            # get new edges but remove those pointing to already sampled nodes
            new_neighbors = set(self._graph.neighbors(node)).difference(self._sampled_nodes)
            edges[node] = {}
            edges[node]['neighbors'] = new_neighbors
            edges[node]['weights'] = [self._graph.get_edge_data(node, e)['weight'] for e in new_neighbors]
            edges[node]['degree'] = sum(edges[node]['weights'])
        return edges

    def _get_probability_density(self, edges_data):
        if self.mode == 'spikyball':
            p = np.fromiter(itertools.chain.from_iterable([edges_data[k]['weights'] for k in edges_data.keys()]), float)
        elif self.mode == 'fireball':
            p = np.fromiter(itertools.chain.from_iterable(
                [np.array(edges_data[k]['weights']) / edges_data[k]['degree'] for k in edges_data.keys()]), float)
        else:
            raise ValueError('Unknown sampling mode')
        # normalize
        p_norm = p / np.sum(p)
        return p_norm

    def _process_hops(self):
        hop_cnt = 0
        layer_nodes = self._seed_nodes.copy()

        while hop_cnt < self.max_hops and len(self._sampled_nodes) < self.number_of_nodes:
            edges_data = self._get_new_edges(layer_nodes)
            p_norm = self._get_probability_density(edges_data)
            new_nodes = list(itertools.chain.from_iterable([edges_data[k]['neighbors'] for k in edges_data.keys()]))
            layer_nodes = set(np.random.choice(new_nodes, max(int(self.sampling_probability*len(new_nodes)), 1), p=p_norm,
                                               replace=False))
            remaining = min(self.number_of_nodes - len(self._sampled_nodes), len(layer_nodes))
            layer_nodes = list(layer_nodes)[:remaining]
            self._sampled_nodes.update(layer_nodes)
            hop_cnt += 1

    def sample(self, graph: nx.classes.graph.Graph) -> nx.classes.graph.Graph:
        self._check_graph(graph)
        self._check_number_of_nodes(graph)
        weighted = nx.is_weighted(graph)
        self._graph = graph if weighted else graph.copy()
        if not weighted:  # set all edges weights to 1
            nx.set_edge_attributes(self._graph, 1.0, 'weight')
        self._create_node_sets()
        self._sampled_nodes.update(self._seed_nodes)
        self._process_hops()

        new_graph = self._graph.subgraph(self._sampled_nodes)
        return new_graph
