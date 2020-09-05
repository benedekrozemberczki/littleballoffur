"""Random walk with jump sampler example"""

import networkx as nx

from littleballoffur.exploration_sampling import RandomWalkWithJumpSampler

graph = nx.watts_strogatz_graph(1000, 10, 0)

sampler = RandomWalkWithJumpSampler()

new_graph = sampler.sample(graph)


