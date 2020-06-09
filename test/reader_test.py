import networkx as nx
from littleballoffur.dataset import GraphReader


def test_reader():
    """
    Testing the graph reading on the Facebook dataset.
    """
    reader = GraphReader("facebook")

    graph = reader.get_graph()

    assert nx.number_of_nodes(graph) == 22470
    assert nx.number_of_edges(graph) == 171002
    assert nx.is_connected(graph) == True
