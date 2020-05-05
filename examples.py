"""Example runs with Little Ball of Fur."""

import networkx as nx

from littleballoffur.dataset import GraphReader
from littleballoffur.node_sampling import RandomNodeSampler
from littleballoffur.expansion_sampling import RandomWalkSampler
from littleballoffur.edge_sampling import RandomEdgeSampler, RandomEdgeSamplerWithInduction
 
#---------------------------------
# Random Walk Sampler Example
#---------------------------------

reader = GraphReader("twitch")

graph = reader.get_graph()

sampler = RandomWalkSampler()

new_graph = sampler.sample(graph)

#-----------------------------
# Random Node Sampler Example
#-----------------------------

sampler = RandomNodeSampler()

new_graph = sampler.sample(graph)

#-----------------------------
# Random Edge Sampler Example
#-----------------------------

sampler = RandomEdgeSampler()

new_graph = sampler.sample(graph)

#--------------------------------------------
# Random Edge Sampler With Induction Example
#--------------------------------------------

sampler = RandomEdgeSamplerWithInduction()

new_graph = sampler.sample(graph)
