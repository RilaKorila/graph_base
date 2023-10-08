from collection import defaultdict


class Path:
    def __init__(self, path_id, path):
        """
        path_id: 経路固有のid
        path: node_idのリスト
        """
        self.path_id = path_id
        self.path = path


class DirectEdge:
    def __init__(self, id, node1, node2, weight=0):
        self.id = int(id)
        self.node_from = int(node1)
        self.node_to = int(node2)
        self.weight = weight


class DirectGraph:
    def __init__(self, nodes, paths):
        self.nodes = nodes
        self.paths = paths
        self.direct_edges = self.create_direct_edges()

    def create_direct_edges(self):
        edge_weight = defaultdict(int)

        for path in self.paths:
            for node_from, node_to in zip(path[:-1], path[1:]):
                edge_weight[(node_from, node_to)] += 1

        direct_edges = set()
        for id, node_pair in enumerate(edge_weight.keys()):
            # 有向グラフなので、(node1_id, node2_id)と(node2_id, node1_id)は別物
            direct_edges.add(DirectEdge(id, *node_pair, edge_weight[node_pair]))

        return direct_edges
