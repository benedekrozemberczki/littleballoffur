import networkx as nx

from littleballoffur import RandomWalkSampler

def test_random_walk_sampler_test():

    graph = nx.watts_strogatz_graph(200, 10, 0)
    sampler = RandomWalkSampler()
    sub_graph = sampler.sample(graph)
    assert sub_graph.number_of_nodes() == sampler.number_of_nodes
    
