"""Example runs with Little Ball of Fur."""

import networkx as nx

from littleballoffur.dataset import GraphReader

#----------------------
# Graph reader example
#----------------------

reader = GraphReader("facebook")

graph = reader.get_graph()
