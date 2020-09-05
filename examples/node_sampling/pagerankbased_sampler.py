"""Pagerank based sampler example."""

from littleballoffur.node_sampling import PageRankBasedSampler

graph = nx.watts_strogatz_graph(1000, 10, 0)

sampler = PageRankBasedSampler()

new_graph = sampler.sample(graph)
