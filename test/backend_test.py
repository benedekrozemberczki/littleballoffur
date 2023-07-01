import networkit as nk
import networkx as nx

from littleballoffur import NetworKitBackEnd, NetworkXBackEnd


def test_networkit_backend_basics():
    backend = NetworKitBackEnd()
    graph = nk.generators.WattsStrogatzGenerator(1000, 10, 0.0).generate()

    assert 1000 == backend.get_number_of_nodes(graph)
    assert 10000 == backend.get_number_of_edges(graph)
    assert 20 == backend.get_degree(graph, 0)


def test_networkit_backend_get_basics():
    backend = NetworKitBackEnd()
    graph = nk.graph.Graph(directed=False)

    # addMissing adds missing nodes
    graph.addEdge(0, 1, addMissing=True)
    graph.addEdge(1, 2, addMissing=True)
    graph.addEdge(2, 3, addMissing=True)
    graph.addEdge(2, 4, addMissing=True)
    graph.addEdge(2, 5, addMissing=True)

    nodes = backend.get_nodes(graph)
    edges = backend.get_edges(graph)

    assert 0 in nodes
    assert 1 in nodes
    assert 2 in nodes
    assert 3 in nodes
    assert 4 in nodes
    assert 5 in nodes

    # Edges are always sorted low to high.
    assert (0, 1) in edges
    assert (1, 2) in edges
    assert (2, 3) in edges
    assert (2, 4) in edges
    assert (2, 5) in edges


def test_networkit_backend_graph_from_edgelist():
    backend = NetworKitBackEnd()
    graph = backend.graph_from_edgelist([[0, 1], [1, 2], [2, 3], [2, 4], [2, 5]])

    nodes = backend.get_nodes(graph)
    edges = backend.get_edges(graph)

    assert 0 in nodes
    assert 1 in nodes
    assert 2 in nodes
    assert 3 in nodes
    assert 4 in nodes
    assert 5 in nodes

    assert (0, 1) in edges
    assert (1, 2) in edges
    assert (2, 3) in edges
    assert (2, 4) in edges
    assert (2, 5) in edges


def test_networkit_backend_get_iterator():
    backend = NetworKitBackEnd()
    graph = nk.graph.Graph()

    graph.addEdge(0, 1, addMissing=True)
    graph.addEdge(1, 2, addMissing=True)
    graph.addEdge(2, 3, addMissing=True)
    graph.addEdge(2, 4, addMissing=True)
    graph.addEdge(2, 5, addMissing=True)

    for node in backend.get_node_iterator(graph):
        assert node in [0, 1, 2, 3, 4, 5]
    for edge in backend.get_edge_iterator(graph):
        assert edge in [(0, 1), (1, 2), (2, 3), (2, 4), (2, 5)]


def test_networkit_backend_induction():
    backend = NetworKitBackEnd()
    graph = nk.graph.Graph()

    graph.addEdge(0, 1, addMissing=True)
    graph.addEdge(1, 2, addMissing=True)
    graph.addEdge(2, 3, addMissing=True)
    graph.addEdge(2, 4, addMissing=True)
    graph.addEdge(2, 5, addMissing=True)

    subgraph = backend.get_subgraph(graph, [2, 3, 4])
    for node in backend.get_node_iterator(subgraph):
        assert node in [2, 3, 4]

    for edge in backend.get_edge_iterator(subgraph):
        assert edge in [(2, 3), (2, 4)]


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


def test_networkit_backend_pagerank():
    backend = NetworKitBackEnd()
    graph = nk.generators.WattsStrogatzGenerator(1000, 10, 0.0).generate()

    pagerank_vector = backend.get_pagerank(graph, 0.9)

    assert pagerank_vector.shape == (1000,)


def test_networkx_backend_basics():
    backend = NetworkXBackEnd()
    graph = nx.watts_strogatz_graph(1000, 10, 0.0)

    assert 1000 == backend.get_number_of_nodes(graph)
    assert 5000 == backend.get_number_of_edges(graph)
    assert 10 == backend.get_degree(graph, 0)


def test_networkx_backend_get_basics():
    backend = NetworkXBackEnd()
    graph = nx.from_edgelist([[0, 1], [1, 2], [2, 3], [2, 4], [2, 5]])

    nodes = backend.get_nodes(graph)
    edges = backend.get_edges(graph)

    assert 0 in nodes
    assert 1 in nodes
    assert 2 in nodes
    assert 3 in nodes
    assert 4 in nodes
    assert 5 in nodes

    assert (0, 1) in edges
    assert (1, 2) in edges
    assert (2, 3) in edges
    assert (2, 4) in edges
    assert (2, 5) in edges


def test_networkx_backend_iterator_basics():
    backend = NetworkXBackEnd()
    graph = nx.from_edgelist([[0, 1], [1, 2], [2, 3], [2, 4], [2, 5]])

    for node in backend.get_node_iterator(graph):
        assert node in [0, 1, 2, 3, 4, 5]

    for edge in backend.get_edge_iterator(graph):
        assert edge in [(0, 1), (1, 2), (2, 3), (2, 4), (2, 5)]


def test_networkx_backend_induction():
    backend = NetworkXBackEnd()
    graph = nx.from_edgelist([[0, 1], [1, 2], [2, 3], [2, 4], [2, 5]])

    subgraph = backend.get_subgraph(graph, [2, 3, 4])

    for node in backend.get_node_iterator(subgraph):
        assert node in [2, 3, 4]

    for edge in backend.get_edge_iterator(subgraph):
        assert edge in [(2, 3), (2, 4)]


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


def test_networkx_backend_shortest_path():
    backend = NetworkXBackEnd()
    graph = nx.from_edgelist([[0, 1], [1, 2], [2, 3], [2, 4], [2, 5]])

    assert backend.get_shortest_path(graph, 0, 5) == [0, 1, 2, 5]
    assert backend.get_shortest_path(graph, 5, 0) == [5, 2, 1, 0]

    assert backend.get_shortest_path(graph, 3, 5) == [3, 2, 5]
    assert backend.get_shortest_path(graph, 5, 3) == [5, 2, 3]


def test_networkx_backend_pagerank():
    backend = NetworkXBackEnd()
    graph = nx.watts_strogatz_graph(1000, 10, 0.0)

    pagerank_vector = backend.get_pagerank(graph, 0.9)

    assert pagerank_vector.shape == (1000,)


def test_networkx_backend_graph_from_edgelist():
    backend = NetworkXBackEnd()
    graph = backend.graph_from_edgelist([[0, 1], [1, 2], [2, 3], [2, 4], [2, 5]])

    nodes = backend.get_nodes(graph)
    edges = backend.get_edges(graph)

    assert 0 in nodes
    assert 1 in nodes
    assert 2 in nodes
    assert 3 in nodes
    assert 4 in nodes
    assert 5 in nodes

    assert (0, 1) in edges
    assert (1, 2) in edges
    assert (2, 3) in edges
    assert (2, 4) in edges
    assert (2, 5) in edges
