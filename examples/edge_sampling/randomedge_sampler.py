"""Random edge sampler example."""

from littleballoffur.node_sampling import RandomEdgeSampler

graph = nx.watts_strogatz_graph(1000, 10, 0)

sampler = RandomEdgeSampler()

new_graph = sampler.sample(graph)
