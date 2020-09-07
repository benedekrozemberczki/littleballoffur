"""Benchmark dataset reader."""

from littleballoffur.dataset import GraphReader

reader = GraphReader("facebook")

graph = reader.get_graph()

