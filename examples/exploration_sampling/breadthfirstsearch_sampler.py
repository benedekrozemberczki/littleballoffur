"""Breadth first search sampler example"""

import networkx as nx

from littleballoffur.exploration_sampling import BreadthFirstSearchSampler

graph = nx.watts_strogatz_graph(1000, 10, 0)

sampler = BreadthFirstSearchSampler()

new_graph = sampler.sample(graph)


