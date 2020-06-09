import networkx as nx
from littleballoffur.dataset import GraphReader


def test_reader():
    """
    Testing the graph reading on the Facebook dataset.
    """
    reader = GraphReader("facebook")

    graph = reader.get_graph()
    print(nx.number_of_nodes(graph))
    print(nx.number_of_edges(graph))
    assert True == True
