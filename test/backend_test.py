import networkx as nx
import networkit as nk
from littleballoffur import NetworKitBackEnd, NetworkXBackEnd


def test_networkit_backend_basics():

    backend = NetworKitBackEnd()

    graph = nk.generators.WattsStrogatzGenerator(1000, 10, 0.0).generate()

    assert 1000 == backend.get_number_of_nodes(graph)
    assert 10000 == backend.get_number_of_edges(graph)
    assert 20 == backend.get_degree(graph, 0)

def test_networkit_backend_neighbors():

    backend = NetworKitBackEnd()

    graph = nk.graph.Graph()
    graph.addEdge(0, 1, addMissing=True)
    graph.addEdge(1, 2, addMissing=True)
    graph.addEdge(2, 3, addMissing=True)
    graph.addEdge(2, 4, addMissing=True)
    graph.addEdge(2, 5, addMissing=True)

    assert [0, 2] == sorted(backend.get_neighbors(graph, 1))
    assert [1] == sorted(backend.get_neighbors(graph, 0))
    assert [1, 3, 4, 5] == sorted(backend.get_neighbors(graph, 2))

    random_neighbor = backend.get_random_neighbor(graph, 2)

    assert random_neighbor in [1, 3, 4, 5]
    assert random_neighbor not in [0]

    random_neighbor = backend.get_random_neighbor(graph, 1)

    assert random_neighbor in [0, 2]
    assert random_neighbor not in [3, 4, 5]

def test_networkit_backend_shortest_path():

    backend = NetworKitBackEnd()

    graph = nk.graph.Graph()
    graph.addEdge(0, 1, addMissing=True)
    graph.addEdge(1, 2, addMissing=True)
    graph.addEdge(2, 3, addMissing=True)
    graph.addEdge(2, 4, addMissing=True)
    graph.addEdge(2, 5, addMissing=True)

    assert backend.get_shortest_path(graph, 0, 5) == [0, 1, 2, 5]
    assert backend.get_shortest_path(graph, 5, 0) == [5, 2, 1, 0]

    assert backend.get_shortest_path(graph, 3, 5) == [3, 2, 5]
    assert backend.get_shortest_path(graph, 5, 3) == [5, 2, 3]


def test_networkx_backend_basics():

    backend = NetworkXBackEnd()

    graph = nx.watts_strogatz_graph(1000, 10, 0.0)

    assert 1000 == backend.get_number_of_nodes(graph)
    assert 5000 == backend.get_number_of_edges(graph)
    assert 10 == backend.get_degree(graph, 0)

def test_networkx_backend_neighbors():

    backend = NetworkXBackEnd()

    graph = nx.from_edgelist([[0, 1], [1, 2], [2, 3], [2, 4], [2, 5]])

    assert [0, 2] == sorted(backend.get_neighbors(graph, 1))
    assert [1] == sorted(backend.get_neighbors(graph, 0))
    assert [1, 3, 4, 5] == sorted(backend.get_neighbors(graph, 2))

    random_neighbor = backend.get_random_neighbor(graph, 2)

    assert random_neighbor in [1, 3, 4, 5]
    assert random_neighbor not in [0]

    random_neighbor = backend.get_random_neighbor(graph, 1)

    assert random_neighbor in [0, 2]
    assert random_neighbor not in [3, 4, 5]

    assert backend.get_shortest_path(graph, 0, 5) == [0, 1, 2, 5]
    assert backend.get_shortest_path(graph, 5, 0) == [5, 2, 1, 0]

    assert backend.get_shortest_path(graph, 3, 5) == [3, 2, 5]
    assert backend.get_shortest_path(graph, 5, 3) == [5, 2, 3]

    graph = nx.watts_strogatz_graph(1000, 10, 0.0)
    pagerank_vector = backend.get_pagerank(graph, 0.9)

    assert pagerank_vector.shape == (1000,)


