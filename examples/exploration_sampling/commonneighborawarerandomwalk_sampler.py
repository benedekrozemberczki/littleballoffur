"""Common neighbor aware random walk sampler example"""

import networkx as nx

from littleballoffur.exploration_sampling import CommonNeighborAwareRandomWalkSampler

graph = nx.watts_strogatz_graph(1000, 10, 0)

sampler = CommonNeighborAwareRandomWalkSampler()

new_graph = sampler.sample(graph)


