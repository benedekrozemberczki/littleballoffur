"""Diffusion-tree sampler example"""

import networkx as nx

from littleballoffur.exploration_sampling import DiffusionTreeSampler

graph = nx.watts_strogatz_graph(1000, 10, 0)

sampler = DiffusionTreeSampler()

new_graph = sampler.sample(graph)

