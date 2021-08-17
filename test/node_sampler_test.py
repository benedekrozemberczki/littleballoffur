import networkx as nx
import networkit as nk
from littleballoffur import RandomNodeSampler, DegreeBasedSampler, PageRankBasedSampler

NKGraph = type(nk.graph.Graph())
NXGraph = nx.classes.graph.Graph


def test_random_node_sampler():
    """
    Testing the size of the sample.
    """
    sampler = RandomNodeSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    sub_graph = sampler.sample(graph)

    assert sub_graph.number_of_nodes() == sampler.number_of_nodes
    assert type(sub_graph) == NXGraph

    sampler = RandomNodeSampler(number_of_nodes=10)

    graph = nx.watts_strogatz_graph(100, 10, 0)

    sub_graph = sampler.sample(graph)

    assert sub_graph.number_of_nodes() == sampler.number_of_nodes
    assert type(sub_graph) == NXGraph

    sampler = RandomNodeSampler()

    graph = nk.generators.WattsStrogatzGenerator(200, 10, 0.0).generate()

    sub_graph = sampler.sample(graph)

    assert sub_graph.numberOfNodes() == sampler.number_of_nodes
    assert type(sub_graph) == NKGraph

    sampler = RandomNodeSampler(number_of_nodes=10)

    graph = nk.generators.WattsStrogatzGenerator(100, 10, 0.0).generate()

    sub_graph = sampler.sample(graph)

    assert sub_graph.numberOfNodes() == sampler.number_of_nodes
    assert type(sub_graph) == NKGraph


def test_degree_based_sampler():
    """
    Testing the size of the sample.
    """
    sampler = DegreeBasedSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    sub_graph = sampler.sample(graph)

    assert sub_graph.number_of_nodes() == sampler.number_of_nodes
    assert type(sub_graph) == nx.classes.graph.Graph

    sampler = DegreeBasedSampler(number_of_nodes=10)

    graph = nx.watts_strogatz_graph(100, 10, 0)

    sub_graph = sampler.sample(graph)

    assert sub_graph.number_of_nodes() == sampler.number_of_nodes
    assert type(sub_graph) == nx.classes.graph.Graph

    sampler = DegreeBasedSampler()

    graph = nk.generators.WattsStrogatzGenerator(200, 10, 0.0).generate()

    sub_graph = sampler.sample(graph)

    assert sub_graph.numberOfNodes() == sampler.number_of_nodes
    assert type(sub_graph) == NKGraph

    sampler = DegreeBasedSampler(number_of_nodes=10)

    graph = nk.generators.WattsStrogatzGenerator(100, 10, 0.0).generate()

    sub_graph = sampler.sample(graph)

    assert sub_graph.numberOfNodes() == sampler.number_of_nodes
    assert type(sub_graph) == NKGraph


def test_pagerank_based_sampler():
    """
    Testing the size of the sample.
    """
    sampler = PageRankBasedSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    sub_graph = sampler.sample(graph)

    assert sub_graph.number_of_nodes() == sampler.number_of_nodes
    assert type(sub_graph) == nx.classes.graph.Graph

    sampler = PageRankBasedSampler(number_of_nodes=10)

    graph = nx.watts_strogatz_graph(100, 10, 0)

    sub_graph = sampler.sample(graph)

    assert sub_graph.number_of_nodes() == sampler.number_of_nodes
    assert type(sub_graph) == nx.classes.graph.Graph

    sampler = PageRankBasedSampler()

    graph = nk.generators.WattsStrogatzGenerator(200, 10, 0.0).generate()

    sub_graph = sampler.sample(graph)

    assert sub_graph.numberOfNodes() == sampler.number_of_nodes
    assert type(sub_graph) == NKGraph

    sampler = PageRankBasedSampler(number_of_nodes=10)

    graph = nk.generators.WattsStrogatzGenerator(100, 10, 0.0).generate()

    sub_graph = sampler.sample(graph)

    assert sub_graph.numberOfNodes() == sampler.number_of_nodes
    assert type(sub_graph) == NKGraph
