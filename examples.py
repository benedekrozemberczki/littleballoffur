"""Example runs with Little Ball of Fur."""

import networkx as nx

from littleballoffur.dataset import GraphReader

from littleballoffur.node_sampling import RandomNodeSampler, DegreeBasedSampler, PageRankBasedSampler

from littleballoffur.exploration_sampling import CommunityStructureExpansionSampler, CirculatedNeighborsRandomWalkSampler
from littleballoffur.exploration_sampling import LoopErasedRandomWalkSampler, BreadthFirstSearchSampler, DepthFirstSearchSampler, SnowBallSampler
from littleballoffur.exploration_sampling import RandomWalkSampler, RandomNodeNeighborSampler, MetropolisHastingsRandomWalkSampler
from littleballoffur.exploration_sampling import ShortestPathSampler, CommonNeighborAwareRandomWalkSampler, NonBackTrackingRandomWalkSampler
from littleballoffur.exploration_sampling import RandomWalkWithRestartSampler, RandomWalkWithJumpSampler, FrontierSampler, ForestFireSampler

from littleballoffur.edge_sampling import RandomEdgeSamplerWithPartialInduction
from littleballoffur.edge_sampling import RandomEdgeSampler, RandomNodeEdgeSampler, HybridNodeEdgeSampler, RandomEdgeSamplerWithInduction

reader = GraphReader("facebook")

graph = reader.get_graph()

#-------------------
# Snow Ball Sampler
#-------------------

sampler = SnowBallSampler()

new_graph = sampler.sample(graph)

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

#---------------------------------
# Loop Erased Random Walk Sampler
#---------------------------------

sampler = LoopErasedRandomWalkSampler()

new_graph = sampler.sample(graph)

#-------------------------------------------
# Common Neighbor Aware Random Walk Sampler
#-------------------------------------------

sampler = NonBackTrackingRandomWalkSampler()

new_graph = sampler.sample(graph)

#-------------------------------------------
# Common Neighbor Aware Random Walk Sampler
#-------------------------------------------

sampler = CommonNeighborAwareRandomWalkSampler()

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

#-------------------------------------------
# Circulated Neighbors Random Walk Sampler
#-------------------------------------------

sampler = CirculatedNeighborsRandomWalkSampler()

new_graph = sampler.sample(graph)

#-----------------------------------------------
# Community Structure Expansion Sampler Example
#-----------------------------------------------

sampler = CommunityStructureExpansionSampler()

new_graph = sampler.sample(graph)

#--------------------------
# Frontier Sampler Example
#--------------------------

sampler = FrontierSampler()

new_graph = sampler.sample(graph)

#---------------------------
# ForestFire Sampler Example
#---------------------------

sampler = ForestFireSampler()

new_graph = sampler.sample(graph)

#-----------------------------
# Random Walk Sampler Example
#-----------------------------

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

#------------------------------
# Degree Based Sampler Example
#------------------------------

sampler = DegreeBasedSampler()

new_graph = sampler.sample(graph)

#--------------------------------
# PageRank Based Sampler Example
#--------------------------------

sampler = PageRankBasedSampler()

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

#------------------------------------------
# Random Walk With Restart Sampler Example
#------------------------------------------

sampler = RandomWalkWithRestartSampler()

new_graph = sampler.sample(graph)

#-------------------------------
# Random Walk With Jump Example
#-------------------------------

sampler = RandomWalkWithJumpSampler()

new_graph = sampler.sample(graph)

#-----------------------------------------
# Metropolis Hastings Random Walk Example
#-----------------------------------------

sampler = MetropolisHastingsRandomWalkSampler()

new_graph = sampler.sample(graph)

