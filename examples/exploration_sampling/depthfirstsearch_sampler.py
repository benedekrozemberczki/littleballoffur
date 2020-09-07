"""Snow ball sampler example"""

import networkx as nx

from littleballoffur.exploration_sampling import SnowBallSampler

graph = nx.watts_strogatz_graph(1000, 10, 0)

sampler = SnowBallSampler()

new_graph = sampler.sample(graph)


