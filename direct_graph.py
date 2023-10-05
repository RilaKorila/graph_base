from graph import Node, Edge
from collection import defaultdict

class Path:
    def __init__(self, path_id, path):
        self.path_id = path_id
        self.path = path

class DirectGraph:
    def __init__(self, nodes, paths):
        self.nodes = nodes
        self.paths = paths
    
    def calc_edge_weight(self):
        edge_weight = defaultdict(int)

        for path in self.paths:
            for node_id1, node_id2 in zip(path[:-1], path[1:]):
                edge_id = self.get_edge_id(node_id1, node_id2)
                edge_weight[edge_id] += 1

    def get_edge_id(node_id1, node_id2):
        return 1

        