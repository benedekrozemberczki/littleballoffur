import networkx as nx

from littleballoffur import Sampler


class MetaSampler(Sampler):
    """
    Meta sampler class.
    """

    def __init__(self, seed):
        self.seed = seed

    def sample(self, graph):
        """
        Returning the original graph.
        """
        self._set_seed()
        self._check_graph(graph)
        return graph


def test_sampler():
    """
    Testing the sampler base class.
    """
    sampler = MetaSampler(seed=42)

    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)  # noqa: F841

    assert sampler.seed == 42
