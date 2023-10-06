from graph import Node, Edge
from collection import defaultdict

class Path:
    def __init__(self, path_id, path):
        self.path_id = path_id
        self.path = path

class DirectGraph:
    def __init__(self, nodes, edges, paths):
        self.nodes = nodes
        self.edges = edges
        self.paths = paths
        self.edge_id_dict = {}

        for e in list(self.edges):
            pair = (e.node1, e.node2) if e.node1 >  e.node2 else (e.node2, e.node1)
            self.edge_id_dict[pair] = e.id
    
    def calc_edge_weight(self):
        self.edge_weight = defaultdict(int)

        for path in self.paths:
            for node_id1, node_id2 in zip(path[:-1], path[1:]):
                edge_id = self.edge_id_dict((node_id1, node_id2))
                self.edge_weight[edge_id] += 1

    def set_edge_weight(self):
        for edge in self.edges:
            edge.weight = self.edge_weight[edge.id]
