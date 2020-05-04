import random
import networkx as nx
from littleballoffur.edge_sampling import RandomEdgeSampler

class RandomEdgeSamplerWithInduction(RandomEdgeSampler):


    def _induce_graph(self):
        """
        Inducing all of the edges given the sampled edges
        """
        nodes = set([node for edge in self.sampled_edges for node in edge])
        new_graph = self._graph.subgraph(nodes)
        return new_graph

    def sample(self, graph):
        """
        Sampling edges randomly with induction.

        Arg types:
            * **graph** *(NetworkX graph)* - The graph to be sampled from.

        Return types:
            * **new_graph* *(NetworkX graph)* - The graph of sampled edges.
        """
        self._check_graph(graph)
        self._check_number_of_edges(graph)
        self._graph = graph
        self._create_initial_edge_set()
        new_graph = self._induce_graph()
        return new_graph
