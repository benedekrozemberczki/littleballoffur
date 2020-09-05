"""Random walk sampler example"""

import networkx as nx

from littleballoffur.exploration_sampling import RandomWalkSampler

graph = nx.watts_strogatz_graph(1000, 10, 0)

sampler = RandomWalkSampler()

new_graph = sampler.sample(graph)


