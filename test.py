import math

from direct_graph import DirectGraph, Path
from graph import Node


# pathを持つサンプルグラフデータ
def generate_sample_graph(num_nodes=15):
    # path0: 1 -> 2 -> 3
    # path1: 2 -> 4 -> 5
    # path2: 3 -> 4 -> 5 -> 6
    # path3: 5 -> 6 -> 7 -> 8
    # path4: 1 -> 3 -> 6 -> 8 -> 11 -> 13
    # path5: 2 -> 5 -> 7 -> 9 -> 12 -> 14
    paths = [
        Path(0, [1, 7, 3]),
        Path(1, [3, 10, 5, 6]),
        Path(2, [5, 6, 11, 8]),
        Path(3, [1, 3, 12, 8, 11, 13]),
        Path(4, [2, 14, 7, 9, 12, 1]),
    ]

    node_coordinates = gen_coodinates(num_nodes)
    nodes = {
        Node(i, node_coordinates[i][0], node_coordinates[i][1], 0, str(i))
        for i in range(num_nodes)
    }
    direct_graph = DirectGraph(nodes, paths)

    return direct_graph


def gen_coodinates(num_nodes, radius=200, center_x=350.0, center_y=400.0):
    node_coordinates = []

    for i in range(num_nodes):
        angle = 2 * math.pi * i / num_nodes
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        node_coordinates.append((x, y))

    return node_coordinates
