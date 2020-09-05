"""Random node sampler."""

from littleballoffur.node_sampling import RandomNodeSampler

graph = nx.watts_strogatz_graph(1000, 10, 0)

sampler = RandomNodeSampler()

new_graph = sampler.sample(graph)
