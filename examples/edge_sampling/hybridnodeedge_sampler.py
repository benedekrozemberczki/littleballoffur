"""Hybrid node edge sampler example."""

from littleballoffur.node_sampling import HybridNodeEdgeSampler

graph = nx.watts_strogatz_graph(1000, 10, 0)

sampler = HybridNodeEdgeSampler()

new_graph = sampler.sample(graph)
