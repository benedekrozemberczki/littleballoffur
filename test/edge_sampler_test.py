import networkx as nx
import networkit as nk
from littleballoffur.edge_sampling import (
    RandomEdgeSampler,
    RandomNodeEdgeSampler,
    HybridNodeEdgeSampler,
)
from littleballoffur.edge_sampling import (
    RandomEdgeSamplerWithPartialInduction,
    RandomEdgeSamplerWithInduction,
)


NKGraph = type(nk.graph.Graph())
NXGraph = nx.classes.graph.Graph


def test_random_edge_sampler():
    """
    Testing the edge retention rate.
    """
    sampler = RandomEdgeSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_edges == new_graph.number_of_edges()
    assert type(new_graph) == NXGraph

    sampler = RandomEdgeSampler(number_of_edges=25)

    graph = nx.watts_strogatz_graph(100, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_edges == new_graph.number_of_edges()
    assert type(new_graph) == NXGraph

    sampler = RandomEdgeSampler()

    graph = nk.generators.WattsStrogatzGenerator(200, 10, 0.0).generate()

    new_graph = sampler.sample(graph)

    assert sampler.number_of_edges == new_graph.numberOfEdges()
    assert type(new_graph) == NKGraph

    sampler = RandomEdgeSampler(number_of_edges=25)

    graph = nk.generators.WattsStrogatzGenerator(100, 10, 0.0).generate()

    new_graph = sampler.sample(graph)

    assert sampler.number_of_edges == new_graph.numberOfEdges()
    assert type(new_graph) == NKGraph


def test_random_nonde_edge_sampler():
    """
    Testing the edge retention rate.
    """
    sampler = RandomNodeEdgeSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_edges == new_graph.number_of_edges()
    assert type(new_graph) == NXGraph

    sampler = RandomNodeEdgeSampler(number_of_edges=25)

    graph = nx.watts_strogatz_graph(100, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_edges == new_graph.number_of_edges()
    assert type(new_graph) == NXGraph

    sampler = RandomNodeEdgeSampler()

    graph = nk.generators.WattsStrogatzGenerator(200, 10, 0.0).generate()

    new_graph = sampler.sample(graph)

    assert sampler.number_of_edges == new_graph.numberOfEdges()
    assert type(new_graph) == NKGraph

    sampler = RandomNodeEdgeSampler(number_of_edges=25)

    graph = nk.generators.WattsStrogatzGenerator(200, 10, 0.0).generate()

    new_graph = sampler.sample(graph)

    assert sampler.number_of_edges == new_graph.numberOfEdges()
    assert type(new_graph) == NKGraph


def test_hybrid_node_edge_sampler():
    """
    Testing the edge retention rate.
    """
    sampler = HybridNodeEdgeSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_edges == new_graph.number_of_edges()
    assert type(new_graph) == NXGraph

    sampler = HybridNodeEdgeSampler(number_of_edges=25)

    graph = nx.watts_strogatz_graph(100, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_edges == new_graph.number_of_edges()
    assert type(new_graph) == NXGraph

    sampler = HybridNodeEdgeSampler()

    graph = nk.generators.WattsStrogatzGenerator(200, 10, 0.0).generate()

    new_graph = sampler.sample(graph)

    assert sampler.number_of_edges == new_graph.numberOfEdges()
    assert type(new_graph) == NKGraph

    sampler = HybridNodeEdgeSampler(number_of_edges=25)

    graph = nk.generators.WattsStrogatzGenerator(200, 10, 0.0).generate()

    new_graph = sampler.sample(graph)

    assert sampler.number_of_edges == new_graph.numberOfEdges()
    assert type(new_graph) == NKGraph


def test_induction_samplers():
    """
    Testing the density of induced subgraphs
    """
    induced_sampler = RandomEdgeSamplerWithInduction()
    partially_induced_sampler = RandomEdgeSamplerWithPartialInduction()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    induced_graph = induced_sampler.sample(graph)
    partially_induced_graph = partially_induced_sampler.sample(graph)

    assert nx.density(partially_induced_graph) <= nx.density(induced_graph)
    assert type(induced_graph) == NXGraph
    assert type(partially_induced_graph) == NXGraph

    induced_sampler = RandomEdgeSamplerWithInduction()
    partially_induced_sampler = RandomEdgeSamplerWithPartialInduction()

    graph = nx.watts_strogatz_graph(100, 10, 0)

    induced_graph = induced_sampler.sample(graph)
    partially_induced_graph = partially_induced_sampler.sample(graph)

    assert nx.density(partially_induced_graph) <= nx.density(induced_graph)
    assert type(induced_graph) == NXGraph
    assert type(partially_induced_graph) == NXGraph

    induced_sampler = RandomEdgeSamplerWithInduction()
    partially_induced_sampler = RandomEdgeSamplerWithPartialInduction()

    graph = nk.generators.WattsStrogatzGenerator(200, 10, 0.0).generate()

    induced_graph = induced_sampler.sample(graph)
    partially_induced_graph = partially_induced_sampler.sample(graph)

    assert type(induced_graph) == NKGraph
    assert type(partially_induced_graph) == NKGraph

    induced_sampler = RandomEdgeSamplerWithInduction()
    partially_induced_sampler = RandomEdgeSamplerWithPartialInduction()

    graph = nk.generators.WattsStrogatzGenerator(100, 10, 0.0).generate()

    induced_graph = induced_sampler.sample(graph)
    partially_induced_graph = partially_induced_sampler.sample(graph)

    assert type(induced_graph) == NKGraph
    assert type(partially_induced_graph) == NKGraph
