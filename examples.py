"""Example runs with Little Ball of Fur."""

import networkx as nx

from littleballoffur.dataset import GraphReader
from littleballoffur.node_sampling import RandomWalkNodeSampler 
 
#----------------------
# Graph reader example
#----------------------

reader = GraphReader("twitch")

graph = reader.get_graph()
