"""Random walk with restart sampler example"""

import networkx as nx

from littleballoffur.exploration_sampling import RandomWalkWithRestartSampler

graph = nx.watts_strogatz_graph(1000, 10, 0)

sampler = RandomWalkWithRestartSampler()

new_graph = sampler.sample(graph)


