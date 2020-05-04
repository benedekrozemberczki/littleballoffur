"""Example runs with Little Ball of Fur."""

import networkx as nx

from littleballoffur.dataset import GraphReader
from littleballoffur.node_sampling import RandomWalkNodeSampler, RandomNodeSampler
from littleballoffur.edge_sampling import RandomEdgeSampler
 
#--------------------------------
# Random Walk Node Sampler example
#--------------------------------

reader = GraphReader("twitch")

graph = reader.get_graph()

sampler = RandomWalkNodeSampler()

new_graph = sampler.sample(graph)

#------------------------------
# Random Node Sampler example
#------------------------------

sampler = RandomNodeSampler()

new_graph = sampler.sample(graph)


#------------------------------
# Random Edge Sampler example
#------------------------------

sampler = RandomEdgeSampler()

new_graph = sampler.sample(graph)
