from pyvis.network import Network

from color import Color


# (TODO) caption-> author_nameにリファクタ
class Node:
    def __init__(self, id, x, y, cluster_id, caption, size=2):
        # node_infoから持ってくれば、captionがnullになることはないのでoption引数にはしない
        self.id = int(id)
        self.x = float(x)
        self.y = float(y)
        self.cluster_id = int(cluster_id)
        self.caption = caption
        self.size = size


class Edge:
    def __init__(self, id, node1, node2, relay_points=[]):
        self.id = int(id)
        self.node1 = int(node1)
        self.node2 = int(node2)
        self.relay_points = relay_points


# class BundledEdge:
#     def __init__(self, id, node1, node2, relay_points):
#         self.id = int(id)
#         self.node1 = int(node1)
#         self.node2 = int(node2)
#         self.relay_points = relay_points


class Cluster:
    def __init__(self, id, x, y, r, children):
        self.id = int(id)
        self.x = float(x)
        self.y = float(y)
        self.r = float(r)
        self.children = set()
        for child_id in children:
            self.children.add(int(child_id))


class Graph:
    def __init__(self, nodes, edges, clusters, color_mode, size_mode):
        self.nodes = nodes
        self.edges = edges
        self.clusters = clusters
        self.color_mode = color_mode
        self.size_mode = size_mode
        self.set_node_colors(color_mode)
        self.set_node_size(size_mode)

    def to_network(self, zoom=500, is_bundled=False, cluster_dict=None):
        """
        draw a graph with pyvis, and return a html file
        """
        network = Network(height="900px", width="900px")
        metanodes = []

        for node in self.nodes:
            network.add_node(
                node.id,
                group=node.cluster_id,
                # label=str(node.cluster_id),
                borderWidth=0,
                x=node.x * zoom,
                y=node.y * zoom,
                color=node.color,
                size=node.size,
                physics=False,
            )
            metanodes.append(node.cluster_id)

        is_bundled = False
        # draw edges
        if is_bundled:
            # node1 -- constructors -- node2
            for edge in self.edges:
                try:
                    if (
                        cluster_dict is not None
                        and cluster_dict[edge.node1] == cluster_dict[edge.node2]
                    ):
                        # both node1 and node2 are in the same cluster => NOT draw edges
                        # network.add_edge(edge.node1, edge.node2, width=0.2)
                        continue

                    else:
                        # node1 and node2 are NOT in the same cluster => draw edges
                        relay_points = edge.relay_points

                        # bundled edgesの中継地点
                        for rp in relay_points:
                            network.add_node(
                                rp.id,
                                borderWidth=0,
                                x=rp.x * zoom,
                                y=rp.y * zoom,
                                color="#a9a9a9",
                                size=0.01,
                                physics=False,
                            )

                        # node1 -- relay_points[0]
                        network.add_edge(edge.node1, relay_points[0].id, width=0.2)

                        # between relay_points
                        for i in range(len(relay_points) - 1):
                            network.add_edge(
                                relay_points[i].id, relay_points[i + 1].id, width=0.2
                            )

                        # relay_points[-1] -- node2
                        network.add_edge(relay_points[-1].id, edge.node2, width=0.2)

                except AssertionError:
                    print(edge.node1, " と ", edge.node2)
                    continue
        else:
            for edge in self.edges:
                try:
                    network.add_edge(edge.node1, edge.node2, width=0.2)
                except AssertionError:
                    print(edge.node1, " と ", edge.node2)
                    continue

        network.inherit_edge_colors(False)
        network.toggle_drag_nodes(False)
        network.toggle_physics(False)
        network.toggle_stabilization(False)

        return network

    def to_html(self, fname="test.html", is_bundled=False, cluster_dict=None):
        network = self.to_network()
        network.write_html(fname)

        return network.html

    def set_node_colors(self, color_mode):
        # 通常のmeta-nodeごとの色分け
        if color_mode == "cluster":
            color_dict = Color(num_colors=len(self.nodes)).make_color_dict()
            for node in list(self.nodes):
                node.color = color_dict[node.cluster_id]

        else:  # debug
            for node in list(self.nodes):
                node.color = "#a9a9a9"

    def set_node_size(self, size_mode):
        if size_mode == "same":
            return
