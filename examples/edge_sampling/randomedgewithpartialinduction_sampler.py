"""Random edge sampler with partial induction example."""

import networkx as nx
from littleballoffur.edge_sampling import RandomEdgeSamplerWithPartialInduction

graph = nx.watts_strogatz_graph(1000, 10, 0)

sampler = RandomEdgeSamplerWithPartialInduction()

new_graph = sampler.sample(graph)
