import networkx as nx

from littleballoffur import RandomWalkSampler, SnowBallSampler, ForestFireSampler

def exploration_sampler_test(sampler):
    """
    Testing the size.
    """
    graph = nx.watts_strogatz_graph(200, 10, 0)

    sub_graph = sampler.sample(graph)

    assert sub_graph.number_of_nodes() == sampler.number_of_nodes

#exploration_sampler_test(RandomWalkSampler())

#exploration_sampler_test(SnowBallSampler())
