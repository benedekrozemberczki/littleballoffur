"""Random edge sampler example."""

import networkx as nx
from littleballoffur.edge_sampling import RandomEdgeSampler

graph = nx.watts_strogatz_graph(1000, 10, 0)

sampler = RandomEdgeSampler()

new_graph = sampler.sample(graph)
