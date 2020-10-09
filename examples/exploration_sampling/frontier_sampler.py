"""Frontier sampler example"""

import networkx as nx

from littleballoffur.exploration_sampling import FrontierSampler

graph = nx.watts_strogatz_graph(1000, 10, 0)

sampler = FrontierSampler()

new_graph = sampler.sample(graph)


