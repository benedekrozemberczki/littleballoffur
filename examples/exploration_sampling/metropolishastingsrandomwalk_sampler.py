"""Metropolis Hastings random walk sampler example"""

import networkx as nx

from littleballoffur.exploration_sampling import MetropolisHastingsRandomWalkSampler

graph = nx.watts_strogatz_graph(1000, 10, 0)

sampler = MetropolisHastingsRandomWalkSampler()

new_graph = sampler.sample(graph)


