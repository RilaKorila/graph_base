from collection import defaultdict

from graph import Edge, Node


class Path:
    def __init__(self, path_id, path):
        """
        path_id: 経路固有のid
        path: node_idのリスト
        """
        self.path_id = path_id
        self.path = path


class DirectEdge:
    def __init__(self, id, node1, node2):
        self.id = int(id)
        self.node_from = int(node1)
        self.node_to = int(node2)
        self.weight = 0

    def set_weight(self, weight):
        self.weight = weight


# NodeとPat
class DirectGraph:
    def __init__(self, nodes, paths):
        self.nodes = nodes
        self.paths = paths
        self.direct_edges = self.create_direct_edges()
        self.edge_id_dict = {}

        # TODO; create_direct_edgesの中での処理を検討
        for e in list(self.direct_edges):
            self.edge_id_dict[(e.node_from, e.node_to)] = e.id

        self.setup_edge_weight()

    def create_direct_edges(self):
        edge_candidates = set()
        direct_edges = set()
        for path in self.paths:
            for node1_id, node2_id in zip(path[:-1], path[1:]):
                # 有向グラフなので、(node1_id, node2_id)と(node2_id, node1_id)は別物
                edge_candidates.add((node1_id, node2_id))

        for id, (node_from, node_to) in enumerate(list(edge_candidates)):
            direct_edge = DirectEdge(id, node_from, node_to)
            direct_edges.add(direct_edge)

        return direct_edges

    def setup_edge_weight(self):
        edge_weight = defaultdict(int)

        for path in self.paths:
            for node_id1, node_id2 in zip(path[:-1], path[1:]):
                edge_id = self.edge_id_dict((node_id1, node_id2))
                edge_weight[edge_id] += 1

        for edge in self.direct_edges:
            edge.set_weight(edge_weight[edge.id])
