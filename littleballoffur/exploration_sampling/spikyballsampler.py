import copy
import itertools
import numpy as np
import networkx as nx
import networkit as nk
from typing import Union
from collections import deque
from littleballoffur.sampler import Sampler
from littleballoffur.helpers import Edge


NKGraph = type(nk.graph.Graph())
NXGraph = nx.classes.graph.Graph


class SpikyBallSampler(Sampler):
    r"""An implementation of spiky ball sampling. The procedure is a filtered
    breadth-first search sampling method where the expansion is is performed
    over a random subset of neighbors. `"For details about the algorithm see
    this paper." <https://www.mdpi.com/1999-4893/13/11/275>`_

    Args:
        number_of_nodes (int): Number of sampled nodes. Default is 100.
        sampling_probability (float): Edge sampling probability. Default is 0.1.
        initial_nodes_ratio (float): Initial ratio of sampled nodes. Default is 0.1.
        seed (int): Random seed. Default is 42.
        max_hops (int): Number of hops. Default is 100000.
        mode (str): Sampling procedure, one of:  (:obj:`"edgeball"`, :obj:`"hubball"`, :obj:`"coreball"`,
                     :obj:`"fireball"`, :obj:`"firecoreball"`). Default is 'fireball'.
        max_visited_nodes_backlog (int): Maximal number of nodes in restart queue. Default is 100.
        restart_hop_size (int): Mimimal number of nodes to pop from restart queue. Default is 10.
        distrib_coeff (float): Proposal distribution power coefficient. Default is 1.0.
    """

    def __init__(
        self,
        number_of_nodes: int = 100,
        sampling_probability: float = 0.2,
        initial_nodes_ratio: float = 0.1,
        seed: int = 42,
        max_hops: int = 100000,
        mode: str = "fireball",
        max_visited_nodes_backlog: int = 100,
        restart_hop_size: int = 10,
        distrib_coeff: float = 1.0,
    ):
        self.number_of_nodes = number_of_nodes
        self.sampling_probability = sampling_probability
        self.initial_nodes_ratio = initial_nodes_ratio
        self.max_hops = max_hops
        self.seed = seed
        self.mode = mode
        self.max_visited_nodes_backlog = max_visited_nodes_backlog
        self.restart_hop_size = restart_hop_size
        self.distrib_coeff = distrib_coeff
        self._set_modes()
        self._set_seed()

    def _set_modes(self):
        self._mode_computations = {
            "edgeball": {"source": False, "target": False},
            "hubball": {"source": True, "target": False},
            "coreball": {"source": False, "target": True},
            "fireball": {"source": True, "target": False},
            "firecoreball": {"source": True, "target": True},
        }

    def _get_edge_weight(self, u, v):
        if self._is_weighted_graph:
            weight = self.backend.get_edge_weight(self._graph, u, v)
        else:
            weight = 1.0
        return weight

    def _create_node_sets(self):
        """
        Create a starting set of nodes.
        """
        self._sampled_nodes = set()
        num_nodes = self.backend.get_number_of_nodes(self._graph)
        self._set_of_nodes = set(range(num_nodes))
        num_initial_nodes = max(int(self.number_of_nodes * self.initial_nodes_ratio), 1)
        self._seed_nodes = set(
            np.random.choice(list(self._set_of_nodes), num_initial_nodes, replace=False)
        )
        self._visited_nodes = deque(maxlen=self.max_visited_nodes_backlog)
        self._sampled_nodes.update(self._seed_nodes)

    def _get_degree(self, edge_list, selector):
        return {
            k: sum(map(lambda x: x.weight, g))
            for k, g in itertools.groupby(sorted(edge_list, key=selector), selector)
        }

    def _get_new_edges(self, nodes):
        edge_list = []
        for node in nodes:
            new_neighbors = set(
                self.backend.get_neighbors(self._graph, node)
            ).difference(self._sampled_nodes)
            for e in new_neighbors:
                edge_list.append(Edge(node, e, self._get_edge_weight(node, e)))

        if self._mode_computations[self.mode]["source"]:
            source_degree = self._get_degree(edge_list, lambda x: x.source)
        else:
            source_degree = {}

        if self._mode_computations[self.mode]["target"]:
            target_degree = self._get_degree(edge_list, lambda x: x.target)
        else:
            target_degree = {}

        for e in edge_list:
            e.source_degree = source_degree.get(e.source, 1.0)
            e.target_degree = target_degree.get(e.target, 1.0)
        edges_data = {
            "raw": edge_list,
            "weight": list(map(lambda x: x.weight, edge_list)),
            "source_degree": list(map(lambda x: x.source_degree, edge_list)),
            "target_degree": list(map(lambda x: x.target_degree, edge_list)),
        }
        return edges_data

    def _get_probability_density_generic(
        self, edges_data, source_coef, weight_coef, target_coef
    ):
        if self._mode_computations[self.mode]["source"]:
            p = np.array(edges_data["source_degree"]) ** source_coef
        else:
            p = np.ones(len(edges_data["source_degree"]))

        p *= np.array(edges_data["weight"]) ** weight_coef

        if self._mode_computations[self.mode]["target"]:
            p *= np.array(edges_data["target_degree"]) ** target_coef
        p_norm = p / np.sum(p)
        return p_norm

    def _get_probability_density(self, edges_data, coeff):
        if self.mode == "edgeball":
            source_coeff, edge_coeff, target_coeff = 0, 1, 0
        elif self.mode == "hubball":
            source_coeff, edge_coeff, target_coeff = coeff, 1, 0
        elif self.mode == "coreball":
            source_coeff, edge_coeff, target_coeff = 0, 1, coeff
        elif self.mode == "fireball":
            source_coeff, edge_coeff, target_coeff = -1, 1, 0
        elif self.mode == "firecoreball":
            source_coeff, edge_coeff, target_coeff = -1, 1, coeff
        else:
            raise ValueError("Unknown ball type.")

        return self._get_probability_density_generic(
            edges_data, source_coeff, edge_coeff, target_coeff
        )

    def _process_hops(self):
        hop_count = 0
        layer_nodes = self._seed_nodes.copy()
        while (
            hop_count < self.max_hops
            and len(self._sampled_nodes) < self.number_of_nodes
        ):
            edges_data = self._get_new_edges(layer_nodes)
            p_norm = self._get_probability_density(edges_data, self.distrib_coeff)
            new_nodes = [edge.target for edge in edges_data["raw"]]
            if len(new_nodes) == 0:
                layer_nodes = [
                    self._visited_nodes.popleft()
                    for k in range(min(self.restart_hop_size, len(self._visited_nodes)))
                ]
                continue

            sampled_edges = np.random.choice(
                new_nodes,
                max(round(self.sampling_probability * len(new_nodes)), 1),
                p=p_norm,
                replace=False,
            )
            layer_nodes = set(sampled_edges)
            self._visited_nodes.extendleft(set(new_nodes).difference(layer_nodes))
            remaining = min(
                self.number_of_nodes - len(self._sampled_nodes), len(layer_nodes)
            )
            layer_nodes = list(layer_nodes)[:remaining]
            self._sampled_nodes.update(layer_nodes)
            hop_count = hop_count + 1

    def _assign_graph(self, graph: Union[NXGraph, NKGraph]):
        """
        Assigning the source graph and making a decision about weighting.
        """
        self._graph = graph
        self._is_weighted_graph = self.backend.is_weighted(graph)

    def sample(self, graph: Union[NXGraph, NKGraph]) -> Union[NXGraph, NKGraph]:
        """
        Sampling nodes iteratively with a spiky ball sampler.

        Arg types:
            * **graph** *(NetworkX or NetworKit graph)* - The graph to be sampled from.

        Return types:
            * **new_graph** *(NetworkX or NetworKit graph)* - The graph of sampled nodes.
        """
        self._deploy_backend(graph)
        self._check_number_of_nodes(graph)
        self._assign_graph(graph)
        self._create_node_sets()
        self._process_hops()
        new_graph = self.backend.get_subgraph(graph, self._sampled_nodes)
        return new_graph
