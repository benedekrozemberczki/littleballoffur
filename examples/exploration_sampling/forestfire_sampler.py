"""Loop erased random walk sampler example"""

import networkx as nx

from littleballoffur.exploration_sampling import LoopErasedRandomWalkSampler

graph = nx.watts_strogatz_graph(1000, 10, 0)

sampler = LoopErasedRandomWalkSampler()

new_graph = sampler.sample(graph)


