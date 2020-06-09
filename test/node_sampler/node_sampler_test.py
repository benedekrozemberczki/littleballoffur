import networkx as nx

from littleballoffur import NodeSampler, DegreeBasedSampler, PageRankBasedSampler

def node_sampler_test(sampler):
    """
    Testing the size.
    """
    graph = nx.watts_strogatz_graph(200, 10, 0)

    sub_graph = sampler.sample(graph)

    assert sub_graph.number_of_nodes() == sampler.number_of_nodes

node_sampler_test(NodeSampler())

node_sampler_test(DegreeBasedSampler())

node_sampler_test(PageRankBasedSampler())
