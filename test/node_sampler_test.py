import networkx as nx

from littleballoffur import RandomNodeSampler, DegreeBasedSampler, PageRankBasedSampler

def test_random_node_sampler():
    """
    Testing the size of the sample.
    """
    sampler = RandomNodeSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    sub_graph = sampler.sample(graph)

    assert sub_graph.number_of_nodes() == sampler.number_of_nodes
    assert type(sub_graph) == nx.classes.graph.Graph


def test_degree_based_sampler():
    """
    Testing the size of the sample.
    """
    sampler = DegreeBasedSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    sub_graph = sampler.sample(graph)

    assert sub_graph.number_of_nodes() == sampler.number_of_nodes
    assert type(sub_graph) == nx.classes.graph.Graph


def test_pagerank_based_sampler():
    """
    Testing the size of the sample.
    """
    sampler = PageRankBasedSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    sub_graph = sampler.sample(graph)

    assert sub_graph.number_of_nodes() == sampler.number_of_nodes
    assert type(sub_graph) == nx.classes.graph.Graph
