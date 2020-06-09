import networkx as nx

from littleballoffur import Sampler

class MetaSampler(Sampler):
      """
      Meta sampler class.
      """
      def __init__(self, seed):
          self.seed = seed

      def fit(self, graph):
          """
          Returning the original graph.
          """
          self._set_seed()
          self._check_graph()
          return graph

def test_sampler():
    """
    Testing the sampler base class.
    """
    sampler = MetaSampler()
    new_graph = sampler.sample(graph)

    assert sampler.seed == 42
    

