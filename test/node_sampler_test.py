import networkx as nx

from littleballoffur import RandomNodeSampler, DegreeBasedSampler, PageRankBasedSampler

def test_random_node_sampler():
    """
    Testing the size.
    """
    sampler = RandomNodeSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    sub_graph = sampler.sample(graph)

    assert sub_graph.number_of_nodes() == sampler.number_of_nodes
