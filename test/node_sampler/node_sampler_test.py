import networkx as nx

from littleballoffur import NodeSampler, DegreeBasedSampler, PageRankBasedSampler

def node_sampler_test():
    """
    Testing the size.
    """
    sampler = NodeSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    sub_graph = sampler.sample(graph)

    assert sub_graph.number_of_nodes() == sampler.number_of_nodes
