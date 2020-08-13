import networkx as nx

from littleballoffur.exploration_sampling import LoopErasedRandomWalkSampler, BreadthFirstSearchSampler, DepthFirstSearchSampler

from littleballoffur.exploration_sampling import CommunityStructureExpansionSampler, CirculatedNeighborsRandomWalkSampler, SnowBallSampler
from littleballoffur.exploration_sampling import RandomWalkSampler, MetropolisHastingsRandomWalkSampler, CommonNeighborAwareRandomWalkSampler
from littleballoffur.exploration_sampling import NonBackTrackingRandomWalkSampler, RandomWalkWithRestartSampler, ForestFireSampler, SpikyBallSampler

from littleballoffur.exploration_sampling import ShortestPathSampler, RandomWalkWithJumpSampler, FrontierSampler, RandomNodeNeighborSampler
from littleballoffur.dataset import GraphReader
#-----------------------------------#
# TESTS FOR SPANNING TREE SAMPLERS. #
#-----------------------------------#


def test_loop_erased_random_walk_sampler():
    """
    Testing the number of nodes, connectivity and tree structure.
    """
    sampler = LoopErasedRandomWalkSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)

    assert new_graph.number_of_edges()+1 == new_graph.number_of_nodes()
    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == nx.classes.graph.Graph

    sampler = LoopErasedRandomWalkSampler(number_of_nodes=25)

    graph = nx.watts_strogatz_graph(100, 10, 0)

    new_graph = sampler.sample(graph)

    assert new_graph.number_of_edges()+1 == new_graph.number_of_nodes()
    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == nx.classes.graph.Graph


def test_breadth_first_search_sampler():
    """
    Testing the number of nodes, connectivity and tree structure.
    """
    sampler = BreadthFirstSearchSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)

    assert new_graph.number_of_edges()+1 == new_graph.number_of_nodes()
    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == nx.classes.graph.Graph

    sampler = BreadthFirstSearchSampler(number_of_nodes=25)

    graph = nx.watts_strogatz_graph(100, 10, 0)

    new_graph = sampler.sample(graph)

    assert new_graph.number_of_edges()+1 == new_graph.number_of_nodes()
    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == nx.classes.graph.Graph


def test_depth_first_search_sampler():
    """
    Testing the number of nodes, connectivity and tree structure.
    """
    sampler = DepthFirstSearchSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)

    assert new_graph.number_of_edges()+1 == new_graph.number_of_nodes()
    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == nx.classes.graph.Graph

    sampler = DepthFirstSearchSampler(number_of_nodes=25)

    graph = nx.watts_strogatz_graph(100, 10, 0)

    new_graph = sampler.sample(graph)

    assert new_graph.number_of_edges()+1 == new_graph.number_of_nodes()
    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == nx.classes.graph.Graph



#----------------------------------------#
# TESTS FOR CONNECTED SUBGRAPH SAMPLERS. #
#----------------------------------------#

def test_community_structure_expansion_sampler():
    """
    Testing the number of nodes and the connectivity.
    """
    sampler = CommunityStructureExpansionSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == nx.classes.graph.Graph

    sampler = CommunityStructureExpansionSampler(number_of_nodes=25)

    graph = nx.watts_strogatz_graph(100, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == nx.classes.graph.Graph


def test_circulated_neighbors_random_walk_sampler():
    """
    Testing the number of nodes and the connectivity.
    """
    sampler = CirculatedNeighborsRandomWalkSampler()

    graph = nx.watts_strogatz_graph(200, 2, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == nx.classes.graph.Graph

    sampler = CirculatedNeighborsRandomWalkSampler(number_of_nodes=25)

    graph = nx.watts_strogatz_graph(100, 2, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == nx.classes.graph.Graph


def test_snowball_sampler():
    """
    Testing the number of nodes and the connectivity.
    """
    sampler = SnowBallSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == nx.classes.graph.Graph

    sampler = SnowBallSampler(number_of_nodes=25)

    graph = nx.watts_strogatz_graph(100, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == nx.classes.graph.Graph


def test_random_walk_sampler():
    """
    Testing the number of nodes and the connectivity.
    """
    sampler = RandomWalkSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == nx.classes.graph.Graph

    sampler = RandomWalkSampler(number_of_nodes=25)

    graph = nx.watts_strogatz_graph(100, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == nx.classes.graph.Graph


def test_metropolis_hastings_random_walk_sampler():
    """
    Testing the number of nodes and the connectivity.
    """
    sampler = MetropolisHastingsRandomWalkSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == nx.classes.graph.Graph

    sampler = MetropolisHastingsRandomWalkSampler(number_of_nodes=25)

    graph = nx.watts_strogatz_graph(100, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == nx.classes.graph.Graph


def test_common_neighbor_aware_random_walk_sampler():
    """
    Testing the number of nodes and the connectivity.
    """
    sampler = CommonNeighborAwareRandomWalkSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == nx.classes.graph.Graph

    sampler = CommonNeighborAwareRandomWalkSampler(number_of_nodes=25)

    graph = nx.watts_strogatz_graph(100, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == nx.classes.graph.Graph


def test_non_back_trackin_random_walk_sampler():
    """
    Testing the number of nodes and the connectivity.
    """
    sampler = NonBackTrackingRandomWalkSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == nx.classes.graph.Graph

    sampler = NonBackTrackingRandomWalkSampler(number_of_nodes=25)

    graph = nx.watts_strogatz_graph(100, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == nx.classes.graph.Graph


def test_random_walk_with_restart_sampler():
    """
    Testing the number of nodes and the connectivity.
    """
    sampler = RandomWalkWithRestartSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0.5)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == nx.classes.graph.Graph

    sampler = RandomWalkWithRestartSampler(number_of_nodes=25)

    graph = nx.watts_strogatz_graph(100, 10, 0.5)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == nx.classes.graph.Graph


def test_forest_fire_sampler():
    """
    Testing the number of nodes and the connectivity.
    """
    sampler = ForestFireSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == nx.classes.graph.Graph

    sampler = ForestFireSampler(number_of_nodes=25)

    graph = nx.watts_strogatz_graph(100, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == nx.classes.graph.Graph

def test_edgeball_sampler():
    sampler = SpikyBallSampler(mode='edgeball')
    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)
    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert type(new_graph) == nx.classes.graph.Graph

def test_edgeball_sampler_fb():
    graph = GraphReader("facebook").get_graph()
    num_nodes = int(0.4*graph.number_of_nodes())
    sampler = SpikyBallSampler(mode='edgeball', number_of_nodes=num_nodes,
                               initial_nodes_ratio=1e-3, sampling_probability=0.1)

    new_graph = sampler.sample(graph)
    assert type(new_graph) == nx.classes.graph.Graph
    assert sampler.number_of_nodes == new_graph.number_of_nodes()

def test_fireball_sampler():
    sampler = SpikyBallSampler(mode='fireball')
    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)
    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert type(new_graph) == nx.classes.graph.Graph

def test_fireball_sampler_fb():
    graph = GraphReader("facebook").get_graph()
    num_nodes = int(0.4*graph.number_of_nodes())
    sampler = SpikyBallSampler(mode='fireball', number_of_nodes=num_nodes,
                               initial_nodes_ratio=1e-3, sampling_probability=0.1)

    new_graph = sampler.sample(graph)
    assert type(new_graph) == nx.classes.graph.Graph
    assert sampler.number_of_nodes == new_graph.number_of_nodes()

def test_hubball_sampler():
    sampler = SpikyBallSampler(mode='hubball')
    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)
    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert type(new_graph) == nx.classes.graph.Graph

def test_hubball_sampler_fb():
    graph = GraphReader("facebook").get_graph()
    num_nodes = int(0.4*graph.number_of_nodes())
    sampler = SpikyBallSampler(mode='hubball', number_of_nodes=num_nodes,
                               initial_nodes_ratio=1e-3, sampling_probability=0.1)

    new_graph = sampler.sample(graph)
    assert type(new_graph) == nx.classes.graph.Graph
    assert sampler.number_of_nodes == new_graph.number_of_nodes()

def test_coreball_sampler():
    sampler = SpikyBallSampler(mode='coreball')
    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)
    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert type(new_graph) == nx.classes.graph.Graph

def test_coreball_sampler_fb():
    graph = GraphReader("facebook").get_graph()
    num_nodes = int(0.4*graph.number_of_nodes())
    sampler = SpikyBallSampler(mode='coreball', number_of_nodes=num_nodes,
                               initial_nodes_ratio=1e-3, sampling_probability=0.1)

    new_graph = sampler.sample(graph)
    assert type(new_graph) == nx.classes.graph.Graph
    assert sampler.number_of_nodes == new_graph.number_of_nodes()

def test_firecoreball_sampler():
    sampler = SpikyBallSampler(mode='firecoreball')
    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)
    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert type(new_graph) == nx.classes.graph.Graph

def test_firecoreball_sampler_fb():
    graph = GraphReader("facebook").get_graph()
    num_nodes = int(0.4*graph.number_of_nodes())
    sampler = SpikyBallSampler(mode='firecoreball', number_of_nodes=num_nodes,
                               initial_nodes_ratio=1e-3, sampling_probability=0.1)

    new_graph = sampler.sample(graph)
    assert type(new_graph) == nx.classes.graph.Graph
    assert sampler.number_of_nodes == new_graph.number_of_nodes()

#---------------------------------------#
# TESTS FOR UNCONNECTED GRAPH SAMPLERS  #
#---------------------------------------#

def test_shortest_path_sampler():
    """
    Testing the number of nodes.
    """
    sampler = ShortestPathSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert type(new_graph) == nx.classes.graph.Graph

    sampler = ShortestPathSampler(number_of_nodes=25)

    graph = nx.watts_strogatz_graph(100, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert type(new_graph) == nx.classes.graph.Graph



def test_random_walk_with_jump_sampler():
    """
    Testing the number of nodes.
    """
    sampler = RandomWalkWithJumpSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert type(new_graph) == nx.classes.graph.Graph

    sampler = RandomWalkWithJumpSampler(number_of_nodes=25)

    graph = nx.watts_strogatz_graph(100, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert type(new_graph) == nx.classes.graph.Graph


def test_frontier_sampler():
    """
    Testing the number of nodes.
    """
    sampler = FrontierSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert type(new_graph) == nx.classes.graph.Graph

    sampler = FrontierSampler(number_of_nodes=25)

    graph = nx.watts_strogatz_graph(100, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert type(new_graph) == nx.classes.graph.Graph


def test_random_node_neighbor_sampler():
    """
    Testing the number of nodes.
    """
    sampler = RandomNodeNeighborSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes <= new_graph.number_of_nodes()
    assert type(new_graph) == nx.classes.graph.Graph

    sampler = RandomNodeNeighborSampler(number_of_nodes=25)

    graph = nx.watts_strogatz_graph(100, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes <= new_graph.number_of_nodes()
    assert type(new_graph) == nx.classes.graph.Graph
