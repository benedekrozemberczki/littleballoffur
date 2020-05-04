"""Example runs with Little Ball of Fur."""

import networkx as nx

from littleballoffur.dataset import GraphReader
from littleballoffur.node_sampling import RandomWalkNodeSampler, RandomNodeSampler
 
#--------------------------------
# Random Walk Node Sampler example
#--------------------------------

reader = GraphReader("twitch")

graph = reader.get_graph()

print(nx.transitivity(graph))

sampler = RandomWalkNodeSampler()

new_graph = sampler.sample(graph)

print(nx.transitivity(new_graph))

#------------------------------
# Random Node Sampler example
#------------------------------

sampler = RandomNodeSampler()

new_graph = sampler.sample(graph)

print(nx.transitivity(new_graph))
