"""Community structure expansion sampler example"""

import networkx as nx

from littleballoffur.exploration_sampling import CommunityStructureExpansionSampler

graph = nx.watts_strogatz_graph(1000, 10, 0)

sampler = CommunityStructureExpansionSampler()

new_graph = sampler.sample(graph)


