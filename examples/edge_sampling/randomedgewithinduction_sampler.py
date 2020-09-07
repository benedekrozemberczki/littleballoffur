"""Random edge sampler with induction example."""

import networkx as nx
from littleballoffur.edge_sampling import RandomEdgeSamplerWithInduction

graph = nx.watts_strogatz_graph(1000, 10, 0)

sampler = RandomEdgeSamplerWithInduction()

new_graph = sampler.sample(graph)
