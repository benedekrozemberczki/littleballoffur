import io
import os
import numpy as np
import pandas as pd
import networkx as nx
from six.moves import urllib


class GraphReader(object):
    r"""Class to read benchmark datasets for the sampling task.

    Args:
        dataset (str): Dataset of interest. One of facebook/wikipedia/github/twitch/deezer/lastfm. Default is 'wikipedia'.
    """

    def __init__(self, dataset: str = "wikipedia"):
        self.dataset = dataset + "_edges.csv"
        self.base_url = (
            "https://github.com/benedekrozemberczki/littleballoffur/raw/master/dataset/"
        )

    def _pandas_reader(self, bytes):
        """
        Reading bytes as a Pandas dataframe.
        """
        tab = pd.read_csv(
            io.BytesIO(bytes), encoding="utf8", sep=",", dtype={"switch": np.int32}
        )
        return tab

    def _dataset_reader(self):
        """
        Reading the dataset from the web.
        """
        path = os.path.join(self.base_url, self.dataset)
        data = urllib.request.urlopen(path).read()
        data = self._pandas_reader(data)
        return data

    def get_graph(self) -> nx.classes.graph.Graph:
        r"""Getting the graph.

        Return types:
            * **graph** *(NetworkX graph)* - Graph of interest.
        """
        data = self._dataset_reader()
        graph = nx.convert_matrix.from_pandas_edgelist(data, "id_1", "id_2")
        return graph
