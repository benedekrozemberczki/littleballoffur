"""Forest fire sampler example"""

import networkx as nx

from littleballoffur.exploration_sampling import ForestFireSampler

graph = nx.watts_strogatz_graph(1000, 10, 0)

sampler = ForestFireSampler()

new_graph = sampler.sample(graph)


