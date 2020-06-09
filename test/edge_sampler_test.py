import networkx as nx


from littleballoffur.edge_sampling import RandomEdgeSampler, RandomNodeEdgeSampler, HybridNodeEdgeSampler
from littleballoffur.edge_sampling import RandomEdgeSamplerWithPartialInduction, RandomEdgeSamplerWithInduction

def test_random_edge_sampler():
    """
    Testing the edge retention rate.
    """
    sampler = RandomEdgeSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_edges == new_graph.number_of_edges()

def test_random_nonde_edge_sampler():
    """
    Testing the edge retention rate.
    """
    sampler = RandomNodeEdgeSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_edges == new_graph.number_of_edges()

def test_hybrid_node_edge_sampler():
    """
    Testing the edge retention rate.
    """
    sampler = HybridNodeEdgeSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_edges == new_graph.number_of_edges()

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
