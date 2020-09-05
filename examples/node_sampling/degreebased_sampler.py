"""Degree based sampler example."""

from littleballoffur.node_sampling import DegreeBasedSampler

graph = nx.watts_strogatz_graph(1000, 10, 0)

sampler = DegreeBasedSampler()

new_graph = sampler.sample(graph)
