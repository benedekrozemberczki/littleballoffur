import networkx as nx
import networkit as nk
from littleballoffur import NetworKitBackEnd, NetworkXBackEnd


def test_networkit_backend():

    backend = NetworKitBackEnd()

    graph = nk.generators.WattsStrogatzGenerator(1000, 10, 0.0).generate()

    assert 1000 == backend.get_number_of_nodes(graph)
    assert 10000 == backend.get_number_of_edges(graph)
    assert 20 == backend.get_degree(graph, 0)

    graph = nk.graph.Graph()
    graph.addEdge(0, 1, addMissing=True)
    graph.addEdge(1, 2, addMissing=True)
    graph.addEdge(2, 3, addMissing=True)
    graph.addEdge(2, 4, addMissing=True)
    graph.addEdge(2, 5, addMissing=True)

    assert [0, 2] == sorted(backend.get_neighbors(graph, 1))
    assert [1] == sorted(backend.get_neighbors(graph, 0))
    assert [1, 3, 4, 5] == sorted(backend.get_neighbors(graph, 2))


def test_networkx_backend():

    backend = NetworkXBackEnd()

    graph = nx.watts_strogatz_graph(1000, 10, 0.0)

    assert 1000 == backend.get_number_of_nodes(graph)
    assert 5000 == backend.get_number_of_edges(graph)
    assert 10 == backend.get_degree(graph, 0)

    graph = nx.from_edgelist([[0, 1], [1, 2], [2, 3], [2, 4], [2, 5]])

    assert [0, 2] == sorted(backend.get_neighbors(graph, 1))
    assert [1] == sorted(backend.get_neighbors(graph, 0))
    assert [1, 3, 4, 5] == sorted(backend.get_neighbors(graph, 2))

