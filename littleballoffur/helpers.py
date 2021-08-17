class Edge:
    def __init__(self, source, target, weight=1):
        self.source = source
        self.target = target
        self.weight = weight
        self.source_degree = 0
        self.target_degree = 0
