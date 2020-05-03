"""Example runs with Karate Club."""

import networkx as nx

from littleballoffur.dataset import GraphReader

#----------------------
# Graph reader example
#----------------------

reader = GraphReader("facebook")

graph = reader.get_graph()
