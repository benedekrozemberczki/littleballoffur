"""Diffusion sampler example"""

import networkx as nx

from littleballoffur.exploration_sampling import DiffusionSampler

graph = nx.watts_strogatz_graph(1000, 10, 0)

sampler = DiffusionSampler()

new_graph = sampler.sample(graph)


