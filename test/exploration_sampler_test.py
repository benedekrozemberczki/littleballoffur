import networkx as nx
import networkit as nk

from littleballoffur.exploration_sampling import (
    LoopErasedRandomWalkSampler,
    BreadthFirstSearchSampler,
    DepthFirstSearchSampler,
)

from littleballoffur.exploration_sampling import (
    CommunityStructureExpansionSampler,
    CirculatedNeighborsRandomWalkSampler,
    SnowBallSampler,
)
from littleballoffur.exploration_sampling import (
    RandomWalkSampler,
    MetropolisHastingsRandomWalkSampler,
    CommonNeighborAwareRandomWalkSampler,
)
from littleballoffur.exploration_sampling import (
    NonBackTrackingRandomWalkSampler,
    RandomWalkWithRestartSampler,
    ForestFireSampler,
    SpikyBallSampler,
)

from littleballoffur.exploration_sampling import DiffusionSampler, DiffusionTreeSampler

from littleballoffur.exploration_sampling import (
    ShortestPathSampler,
    RandomWalkWithJumpSampler,
    FrontierSampler,
    RandomNodeNeighborSampler,
)
from littleballoffur.dataset import GraphReader

NKGraph = type(nk.graph.Graph())
NXGraph = nx.classes.graph.Graph

# -----------------------------------#
# TESTS FOR SPANNING TREE SAMPLERS. #
# -----------------------------------#


def test_loop_erased_random_walk_sampler_1():
    """
    Testing the number of nodes, connectivity and tree structure.
    """
    sampler = LoopErasedRandomWalkSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)

    assert new_graph.number_of_edges() + 1 == new_graph.number_of_nodes()
    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == NXGraph


def test_loop_erased_random_walk_sampler_2():

    sampler = LoopErasedRandomWalkSampler(number_of_nodes=25)

    graph = nx.watts_strogatz_graph(100, 10, 0)

    new_graph = sampler.sample(graph)

    assert new_graph.number_of_edges() + 1 == new_graph.number_of_nodes()
    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == NXGraph


def test_loop_erased_random_walk_sampler_3():

    sampler = LoopErasedRandomWalkSampler()

    graph = nk.nxadapter.nx2nk(nx.watts_strogatz_graph(200, 10, 0))

    new_graph = sampler.sample(graph)

    assert new_graph.numberOfEdges() + 1 == new_graph.numberOfNodes()
    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph

    new_graph = sampler.sample(graph, 0)

    assert new_graph.numberOfEdges() + 1 == new_graph.numberOfNodes()
    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph

    new_graph = sampler.sample(graph, 199)

    assert new_graph.numberOfEdges() + 1 == new_graph.numberOfNodes()
    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph

    new_graph = sampler.sample(graph, 20)

    assert new_graph.numberOfEdges() + 1 == new_graph.numberOfNodes()
    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph


def test_loop_erased_random_walk_sampler_4():

    sampler = LoopErasedRandomWalkSampler(number_of_nodes=25)

    graph = nk.nxadapter.nx2nk(nx.watts_strogatz_graph(200, 10, 0))

    new_graph = sampler.sample(graph)
    assert new_graph.numberOfEdges() + 1 == new_graph.numberOfNodes()
    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph


def test_breadth_first_search_sampler():
    """
    Testing the number of nodes, connectivity and tree structure.
    """
    sampler = BreadthFirstSearchSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)

    assert new_graph.number_of_edges() + 1 == new_graph.number_of_nodes()
    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == NXGraph

    sampler = BreadthFirstSearchSampler(number_of_nodes=25)

    graph = nx.watts_strogatz_graph(100, 10, 0)

    new_graph = sampler.sample(graph)

    assert new_graph.number_of_edges() + 1 == new_graph.number_of_nodes()
    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == NXGraph

    sampler = BreadthFirstSearchSampler()

    graph = nk.nxadapter.nx2nk(nx.watts_strogatz_graph(200, 10, 0))

    new_graph = sampler.sample(graph)

    assert new_graph.numberOfEdges() + 1 == new_graph.numberOfNodes()
    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph

    new_graph = sampler.sample(graph, 0)

    assert new_graph.numberOfEdges() + 1 == new_graph.numberOfNodes()
    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph

    new_graph = sampler.sample(graph, 173)

    assert new_graph.numberOfEdges() + 1 == new_graph.numberOfNodes()
    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph

    new_graph = sampler.sample(graph, 199)

    assert new_graph.numberOfEdges() + 1 == new_graph.numberOfNodes()
    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph

    sampler = BreadthFirstSearchSampler(number_of_nodes=25)

    graph = nk.nxadapter.nx2nk(nx.watts_strogatz_graph(200, 10, 0))

    new_graph = sampler.sample(graph)

    assert new_graph.numberOfEdges() + 1 == new_graph.numberOfNodes()
    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph

    sampler = BreadthFirstSearchSampler(number_of_nodes=1)

    graph = nk.nxadapter.nx2nk(nx.watts_strogatz_graph(200, 10, 0))

    new_graph = sampler.sample(graph)

    assert new_graph.numberOfEdges() + 1 == new_graph.numberOfNodes()
    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph


def test_depth_first_search_sampler():
    """
    Testing the number of nodes, connectivity and tree structure.
    """
    sampler = DepthFirstSearchSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)

    assert new_graph.number_of_edges() + 1 == new_graph.number_of_nodes()
    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == nx.classes.graph.Graph

    sampler = DepthFirstSearchSampler(number_of_nodes=25)

    graph = nx.watts_strogatz_graph(100, 10, 0)

    new_graph = sampler.sample(graph)

    assert new_graph.number_of_edges() + 1 == new_graph.number_of_nodes()
    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == nx.classes.graph.Graph

    sampler = DepthFirstSearchSampler()

    graph = nk.nxadapter.nx2nk(nx.watts_strogatz_graph(200, 10, 0))

    new_graph = sampler.sample(graph)

    assert new_graph.numberOfEdges() + 1 == new_graph.numberOfNodes()
    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph

    new_graph = sampler.sample(graph, 0)

    assert new_graph.numberOfEdges() + 1 == new_graph.numberOfNodes()
    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph

    new_graph = sampler.sample(graph, 57)

    assert new_graph.numberOfEdges() + 1 == new_graph.numberOfNodes()
    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph

    new_graph = sampler.sample(graph, 199)

    assert new_graph.numberOfEdges() + 1 == new_graph.numberOfNodes()
    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph

    sampler = DepthFirstSearchSampler(number_of_nodes=25)

    graph = nk.nxadapter.nx2nk(nx.watts_strogatz_graph(200, 10, 0))

    new_graph = sampler.sample(graph)

    assert new_graph.numberOfEdges() + 1 == new_graph.numberOfNodes()
    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph

    sampler = DepthFirstSearchSampler(number_of_nodes=1)

    graph = nk.nxadapter.nx2nk(nx.watts_strogatz_graph(200, 10, 0))

    new_graph = sampler.sample(graph)

    assert new_graph.numberOfEdges() + 1 == new_graph.numberOfNodes()
    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph


# ----------------------------------------#
# TESTS FOR CONNECTED SUBGRAPH SAMPLERS. #
# ----------------------------------------#


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

    sampler = CommunityStructureExpansionSampler(number_of_nodes=25)

    graph = nx.watts_strogatz_graph(100, 10, 0)

    new_graph = sampler.sample(graph, 0)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == nx.classes.graph.Graph

    new_graph = sampler.sample(graph, 27)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == nx.classes.graph.Graph

    new_graph = sampler.sample(graph, 99)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == nx.classes.graph.Graph

    sampler = CommunityStructureExpansionSampler()

    graph = nk.nxadapter.nx2nk(nx.watts_strogatz_graph(200, 10, 0))

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph

    sampler = CommunityStructureExpansionSampler(number_of_nodes=25)

    graph = nk.nxadapter.nx2nk(nx.watts_strogatz_graph(100, 10, 0))

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph


def test_circulated_neighbors_random_walk_sampler():
    """
    Testing the number of nodes and the connectivity.
    """
    sampler = CirculatedNeighborsRandomWalkSampler()

    graph = nx.watts_strogatz_graph(200, 2, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == NXGraph

    sampler = CirculatedNeighborsRandomWalkSampler(number_of_nodes=25)

    graph = nx.watts_strogatz_graph(100, 2, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == NXGraph

    sampler = CirculatedNeighborsRandomWalkSampler()

    graph = nk.nxadapter.nx2nk(nx.watts_strogatz_graph(200, 10, 0))

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph

    new_graph = sampler.sample(graph, 0)

    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph

    new_graph = sampler.sample(graph, 199)

    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph

    new_graph = sampler.sample(graph, 92)

    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph

    sampler = CirculatedNeighborsRandomWalkSampler(number_of_nodes=25)

    graph = nk.nxadapter.nx2nk(nx.watts_strogatz_graph(100, 10, 0))

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph


def test_snowball_sampler():
    """
    Testing the number of nodes and the connectivity.
    """
    sampler = SnowBallSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == NXGraph

    sampler = SnowBallSampler(number_of_nodes=25)

    graph = nx.watts_strogatz_graph(100, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == NXGraph

    sampler = SnowBallSampler()

    graph = nk.nxadapter.nx2nk(nx.watts_strogatz_graph(200, 10, 0))

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph

    new_graph = sampler.sample(graph, 0)

    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph

    new_graph = sampler.sample(graph, 111)

    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph

    new_graph = sampler.sample(graph, 199)

    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph

    sampler = SnowBallSampler(number_of_nodes=25)

    graph = nk.nxadapter.nx2nk(nx.watts_strogatz_graph(150, 10, 0))

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph


def test_random_walk_sampler():
    """
    Testing the number of nodes and the connectivity.
    """
    sampler = RandomWalkSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == NXGraph

    sampler = RandomWalkSampler(number_of_nodes=25)

    graph = nx.watts_strogatz_graph(100, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == NXGraph

    sampler = RandomWalkSampler()

    graph = nk.nxadapter.nx2nk(nx.watts_strogatz_graph(200, 10, 0))

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph

    sampler = RandomWalkSampler(number_of_nodes=25)

    graph = nk.nxadapter.nx2nk(nx.watts_strogatz_graph(100, 10, 0))

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph

    sampler = RandomWalkSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph, 17)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == NXGraph

    sampler = RandomWalkSampler(number_of_nodes=25)

    graph = nx.watts_strogatz_graph(100, 10, 0)

    new_graph = sampler.sample(graph, 17)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == NXGraph

    new_graph = sampler.sample(graph, 0)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == NXGraph

    new_graph = sampler.sample(graph, 99)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == NXGraph


def test_diffusion_sampler():
    """
    Testing the number of nodes and the connectivity.
    """
    sampler = DiffusionSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == NXGraph

    sampler = DiffusionSampler(number_of_nodes=25)

    graph = nx.watts_strogatz_graph(100, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == NXGraph

    sampler = DiffusionSampler()

    graph = nk.nxadapter.nx2nk(nx.watts_strogatz_graph(200, 10, 0))

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph

    sampler = DiffusionSampler(number_of_nodes=25)

    graph = nk.nxadapter.nx2nk(nx.watts_strogatz_graph(100, 10, 0))

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph

    sampler = DiffusionSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph, 17)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == NXGraph

    sampler = DiffusionSampler(number_of_nodes=25)

    graph = nx.watts_strogatz_graph(100, 10, 0)

    new_graph = sampler.sample(graph, 17)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == NXGraph

    new_graph = sampler.sample(graph, 0)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == NXGraph

    new_graph = sampler.sample(graph, 99)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == NXGraph


def test_diffusion_tree_sampler():
    """
    Testing the number of nodes and the connectivity.
    """
    sampler = DiffusionTreeSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == NXGraph

    sampler = DiffusionTreeSampler(number_of_nodes=25)

    graph = nx.watts_strogatz_graph(100, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == NXGraph

    sampler = DiffusionTreeSampler()

    graph = nk.nxadapter.nx2nk(nx.watts_strogatz_graph(200, 10, 0))

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph

    sampler = DiffusionTreeSampler(number_of_nodes=25)

    graph = nk.nxadapter.nx2nk(nx.watts_strogatz_graph(100, 10, 0))

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph

    sampler = DiffusionTreeSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph, 17)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == NXGraph

    sampler = DiffusionTreeSampler(number_of_nodes=25)

    graph = nx.watts_strogatz_graph(100, 10, 0)

    new_graph = sampler.sample(graph, 17)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == NXGraph

    new_graph = sampler.sample(graph, 0)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == NXGraph

    new_graph = sampler.sample(graph, 99)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == NXGraph


def test_metropolis_hastings_random_walk_sampler():
    """
    Testing the number of nodes and the connectivity.
    """
    sampler = MetropolisHastingsRandomWalkSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == NXGraph

    sampler = MetropolisHastingsRandomWalkSampler(number_of_nodes=25)

    graph = nx.watts_strogatz_graph(100, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == NXGraph

    sampler = MetropolisHastingsRandomWalkSampler()

    graph = nk.nxadapter.nx2nk(nx.watts_strogatz_graph(200, 10, 0))

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph

    new_graph = sampler.sample(graph, 0)

    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph

    new_graph = sampler.sample(graph, 151)

    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph

    new_graph = sampler.sample(graph, 199)

    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph

    sampler = MetropolisHastingsRandomWalkSampler(number_of_nodes=25)

    graph = nk.nxadapter.nx2nk(nx.watts_strogatz_graph(100, 10, 0))

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph


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

    sampler = CommonNeighborAwareRandomWalkSampler()

    graph = nk.nxadapter.nx2nk(nx.watts_strogatz_graph(200, 10, 0))

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph

    new_graph = sampler.sample(graph, 0)

    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph

    new_graph = sampler.sample(graph, 123)

    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph

    new_graph = sampler.sample(graph, 199)

    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph

    sampler = CommonNeighborAwareRandomWalkSampler(number_of_nodes=25)

    graph = nk.nxadapter.nx2nk(nx.watts_strogatz_graph(100, 10, 0))

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph


def test_non_back_tracking_random_walk_sampler():
    """
    Testing the number of nodes and the connectivity.
    """
    sampler = NonBackTrackingRandomWalkSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == NXGraph

    sampler = NonBackTrackingRandomWalkSampler(number_of_nodes=25)

    graph = nx.watts_strogatz_graph(100, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == NXGraph

    sampler = NonBackTrackingRandomWalkSampler()

    graph = nk.nxadapter.nx2nk(nx.watts_strogatz_graph(200, 10, 0))

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph

    new_graph = sampler.sample(graph, 0)

    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph

    new_graph = sampler.sample(graph, 131)

    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph

    new_graph = sampler.sample(graph, 199)

    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph

    sampler = NonBackTrackingRandomWalkSampler(number_of_nodes=25)

    graph = nk.nxadapter.nx2nk(nx.watts_strogatz_graph(100, 10, 0))

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph


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

    sampler = RandomWalkWithRestartSampler()

    graph = nk.nxadapter.nx2nk(nx.watts_strogatz_graph(200, 10, 0))

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph

    new_graph = sampler.sample(graph, 0)

    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph

    new_graph = sampler.sample(graph, 54)

    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph

    new_graph = sampler.sample(graph, 199)

    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph

    sampler = RandomWalkWithRestartSampler(number_of_nodes=50)

    graph = nk.nxadapter.nx2nk(nx.watts_strogatz_graph(200, 10, 0))

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph


def test_forest_fire_sampler():
    """
    Testing the number of nodes and the connectivity.
    """
    sampler = ForestFireSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == NXGraph

    sampler = ForestFireSampler(number_of_nodes=25)

    graph = nx.watts_strogatz_graph(100, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == NXGraph

    sampler = ForestFireSampler()

    graph = nk.nxadapter.nx2nk(nx.watts_strogatz_graph(200, 10, 0))

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph

    sampler = ForestFireSampler(number_of_nodes=25)

    graph = nk.nxadapter.nx2nk(nx.watts_strogatz_graph(100, 10, 0))

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph

    sampler = ForestFireSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == NXGraph

    sampler = ForestFireSampler(number_of_nodes=25)

    graph = nx.gnm_random_graph(100, 2000)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)
    assert type(new_graph) == NXGraph

    sampler = ForestFireSampler()

    graph = nk.nxadapter.nx2nk(nx.gnm_random_graph(100, 2000))

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph

    sampler = ForestFireSampler(number_of_nodes=25)

    graph = nk.nxadapter.nx2nk(nx.gnm_random_graph(100, 2000))

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert 1 == nk.components.ConnectedComponents(new_graph).run().numberOfComponents()
    assert type(new_graph) == NKGraph


def test_edgeball_sampler():
    sampler = SpikyBallSampler(mode="edgeball")
    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)
    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert type(new_graph) == nx.classes.graph.Graph


def test_edgeball_sampler_fb():
    graph = GraphReader("facebook").get_graph()
    num_nodes = int(0.2 * graph.number_of_nodes())
    sampler = SpikyBallSampler(
        mode="edgeball",
        number_of_nodes=num_nodes,
        initial_nodes_ratio=1e-3,
        sampling_probability=0.1,
    )

    new_graph = sampler.sample(graph)
    assert type(new_graph) == nx.classes.graph.Graph
    assert sampler.number_of_nodes == new_graph.number_of_nodes()


def test_fireball_sampler():
    sampler = SpikyBallSampler(mode="fireball")
    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)
    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert type(new_graph) == nx.classes.graph.Graph


def test_fireball_sampler_fb():
    graph = GraphReader("facebook").get_graph()
    num_nodes = int(0.2 * graph.number_of_nodes())
    sampler = SpikyBallSampler(
        mode="fireball",
        number_of_nodes=num_nodes,
        initial_nodes_ratio=1e-3,
        sampling_probability=0.1,
    )

    new_graph = sampler.sample(graph)
    assert type(new_graph) == nx.classes.graph.Graph
    assert sampler.number_of_nodes == new_graph.number_of_nodes()


def test_hubball_sampler():
    sampler = SpikyBallSampler(mode="hubball", distrib_coeff=2)
    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)
    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert type(new_graph) == nx.classes.graph.Graph


def test_hubball_sampler_fb():
    graph = GraphReader("facebook").get_graph()
    num_nodes = int(0.2 * graph.number_of_nodes())
    sampler = SpikyBallSampler(
        mode="hubball",
        number_of_nodes=num_nodes,
        initial_nodes_ratio=1e-3,
        sampling_probability=0.01,
        distrib_coeff=2,
    )

    new_graph = sampler.sample(graph)
    assert type(new_graph) == nx.classes.graph.Graph
    assert sampler.number_of_nodes == new_graph.number_of_nodes()


def test_coreball_sampler():
    sampler = SpikyBallSampler(mode="coreball", distrib_coeff=2)
    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)
    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert type(new_graph) == nx.classes.graph.Graph


def test_coreball_sampler_fb():
    graph = GraphReader("facebook").get_graph()
    num_nodes = int(0.2 * graph.number_of_nodes())
    sampler = SpikyBallSampler(
        mode="coreball",
        number_of_nodes=num_nodes,
        initial_nodes_ratio=1e-3,
        sampling_probability=0.01,
        distrib_coeff=2,
    )

    new_graph = sampler.sample(graph)
    assert type(new_graph) == nx.classes.graph.Graph
    assert sampler.number_of_nodes == new_graph.number_of_nodes()


def test_firecoreball_sampler():
    sampler = SpikyBallSampler(mode="firecoreball", distrib_coeff=2)
    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)
    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert type(new_graph) == nx.classes.graph.Graph


def test_firecoreball_sampler_fb():
    graph = GraphReader("facebook").get_graph()
    num_nodes = int(0.2 * graph.number_of_nodes())
    sampler = SpikyBallSampler(
        mode="firecoreball",
        number_of_nodes=num_nodes,
        initial_nodes_ratio=1e-3,
        sampling_probability=0.1,
        distrib_coeff=2,
    )

    new_graph = sampler.sample(graph)
    assert type(new_graph) == nx.classes.graph.Graph
    assert sampler.number_of_nodes == new_graph.number_of_nodes()


# ---------------------------------------#
# TESTS FOR UNCONNECTED GRAPH SAMPLERS  #
# ---------------------------------------#


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

    sampler = ShortestPathSampler()

    graph = nk.nxadapter.nx2nk(nx.watts_strogatz_graph(200, 10, 0))

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert type(new_graph) == NKGraph

    sampler = ShortestPathSampler(number_of_nodes=25)

    graph = nk.nxadapter.nx2nk(nx.watts_strogatz_graph(100, 10, 0))

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert type(new_graph) == NKGraph


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

    new_graph = sampler.sample(graph, 0)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert type(new_graph) == nx.classes.graph.Graph

    new_graph = sampler.sample(graph, 13)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert type(new_graph) == nx.classes.graph.Graph

    new_graph = sampler.sample(graph, 42)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert type(new_graph) == nx.classes.graph.Graph

    sampler = RandomWalkWithJumpSampler()

    graph = nk.nxadapter.nx2nk(nx.watts_strogatz_graph(200, 10, 0))

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert type(new_graph) == NKGraph

    sampler = RandomWalkWithJumpSampler(number_of_nodes=25)

    graph = nk.nxadapter.nx2nk(nx.watts_strogatz_graph(100, 10, 0))

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert type(new_graph) == NKGraph


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

    sampler = FrontierSampler()

    graph = nk.nxadapter.nx2nk(nx.watts_strogatz_graph(200, 10, 0))

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert type(new_graph) == NKGraph

    sampler = FrontierSampler(number_of_nodes=25)

    graph = nk.nxadapter.nx2nk(nx.watts_strogatz_graph(100, 10, 0))

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.numberOfNodes()
    assert type(new_graph) == NKGraph


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

    sampler = RandomNodeNeighborSampler()

    graph = nk.nxadapter.nx2nk(nx.watts_strogatz_graph(200, 10, 0))

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes <= new_graph.numberOfNodes()
    assert type(new_graph) == NKGraph

    sampler = RandomNodeNeighborSampler(number_of_nodes=25)

    graph = nk.nxadapter.nx2nk(nx.watts_strogatz_graph(100, 10, 0))

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes <= new_graph.numberOfNodes()
    assert type(new_graph) == NKGraph
