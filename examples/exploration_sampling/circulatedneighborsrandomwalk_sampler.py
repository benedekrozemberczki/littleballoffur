"""Circulated neighbors random walk sampler example"""

import networkx as nx

from littleballoffur.exploration_sampling import CirculatedNeighborsRandomWalkSampler

graph = nx.watts_strogatz_graph(1000, 10, 0)

sampler = CirculatedNeighborsRandomWalkSampler()

new_graph = sampler.sample(graph)


