import networkx as nx

#from littleballoffur.exploration_sampling import CommunityStructureExpansionSampler, CirculatedNeighborsRandomWalkSampler

from littleballoffur.exploration_sampling import LoopErasedRandomWalkSampler, BreadthFirstSearchSampler, DepthFirstSearchSampler
#from littleballoffur.exploration_sampling import RandomWalkSampler, RandomNodeNeighborSampler, MetropolisHastingsRandomWalkSampler
#from littleballoffur.exploration_sampling import ShortestPathSampler, CommonNeighborAwareRandomWalkSampler, NonBackTrackingRandomWalkSampler
#from littleballoffur.exploration_sampling import RandomWalkWithRestartSampler, RandomWalkWithJumpSampler, FrontierSampler, ForestFireSampler, SnowBallSampler


def test_loop_erased_random_walk_sampler():
    """
    Testing the edge retention rate.
    """
    sampler = LoopErasedRandomWalkSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)

    assert new_graph.number_of_edges()+1 == new_graph.number_of_nodes()
    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
