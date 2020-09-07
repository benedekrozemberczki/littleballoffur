"""Random node neighbor sampler example"""

import networkx as nx

from littleballoffur.exploration_sampling import RandomNodeNeighborSampler

graph = nx.watts_strogatz_graph(1000, 10, 0)

sampler = RandomNodeNeighborSampler()

new_graph = sampler.sample(graph)


