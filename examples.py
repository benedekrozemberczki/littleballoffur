"""Example runs with Little Ball of Fur."""

import networkx as nx

from littleballoffur.exploration_sampling import BreadthFirstSearchSampler, DepthFirstSearchSampler
from littleballoffur.exploration_sampling import RandomNodeNeighborSampler
from littleballoffur.exploration_sampling import ShortestPathSampler

from littleballoffur.edge_sampling import RandomEdgeSamplerWithPartialInduction
from littleballoffur.edge_sampling import RandomEdgeSampler, RandomNodeEdgeSampler, HybridNodeEdgeSampler, RandomEdgeSamplerWithInduction

#----------------------------
# Depth First Search Sampler
#----------------------------

sampler = DepthFirstSearchSampler(number_of_nodes=graph.number_of_nodes())

new_graph = sampler.sample(graph)

#------------------------------
# Breadth First Search Sampler
#------------------------------

sampler = BreadthFirstSearchSampler(number_of_nodes=graph.number_of_nodes())

new_graph = sampler.sample(graph)


#--------------------------------------------
# Random Edge Sampler With Partial Induction
#--------------------------------------------

sampler = RandomEdgeSamplerWithPartialInduction()

new_graph = sampler.sample(graph)

#------------------------
# Shortest Path Sampler
#------------------------

sampler = ShortestPathSampler()

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

#----------------------------------
# Random Node Edge Sampler Example
#----------------------------------

sampler = RandomNodeEdgeSampler()

new_graph = sampler.sample(graph)

#----------------------------------
# Hybrid Node Edge Sampler Example
#----------------------------------

sampler = HybridNodeEdgeSampler()

new_graph = sampler.sample(graph)

#--------------------------------------
# Random Node Neighbor Sampler Example
#--------------------------------------

sampler = RandomNodeNeighborSampler()

new_graph = sampler.sample(graph)
