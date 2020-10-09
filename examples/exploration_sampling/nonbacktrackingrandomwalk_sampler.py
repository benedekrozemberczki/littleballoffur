"""Non back-tracking random walk sampler example"""

import networkx as nx

from littleballoffur.exploration_sampling import NonBackTrackingRandomWalkSampler

graph = nx.watts_strogatz_graph(1000, 10, 0)

sampler = NonBackTrackingRandomWalkSampler()

new_graph = sampler.sample(graph)


