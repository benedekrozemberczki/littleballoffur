"""Example runs with Little Ball of Fur."""

import networkx as nx

from littleballoffur.edge_sampling import RandomEdgeSamplerWithPartialInduction
from littleballoffur.edge_sampling import RandomEdgeSampler, RandomNodeEdgeSampler, HybridNodeEdgeSampler, RandomEdgeSamplerWithInduction


#--------------------------------------------
# Random Edge Sampler With Partial Induction
#--------------------------------------------

sampler = RandomEdgeSamplerWithPartialInduction()

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
