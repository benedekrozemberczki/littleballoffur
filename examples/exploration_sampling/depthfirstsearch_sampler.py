"""Depth first search sampler example"""

import networkx as nx

from littleballoffur.exploration_sampling import DepthFirstSearchSampler

graph = nx.watts_strogatz_graph(1000, 10, 0)

sampler = DepthFirstSearchSampler()

new_graph = sampler.sample(graph)
