"""Random node edge sampler example."""

from littleballoffur.edge_sampling import RandomNodeEdgeSampler

graph = nx.watts_strogatz_graph(1000, 10, 0)

sampler = RandomNodeEdgeSampler()

new_graph = sampler.sample(graph)
