"""Shortest path sampler example"""

import networkx as nx

from littleballoffur.exploration_sampling import ShortestPathSampler

graph = nx.watts_strogatz_graph(1000, 10, 0)

sampler = ShortestPathSampler()

new_graph = sampler.sample(graph)


