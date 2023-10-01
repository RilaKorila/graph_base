import csv
import math

import numpy as np




class Color:
    """
    num_colors: 用意する色数を指定(default=300)
    """

    def make_color_dict(self, num_colors=700, start=100, end=16777000):
        """
        input: 用意する色数を指定

        return: {色番号: 「#000000」の色表記} を持つ辞書を返す
        """
        color_dict = {}
        # 100から16777000の間をnum_colors(メタノード数: 何色の辞書を作るか) で分割
        cols = np.linspace(start, end, num_colors).tolist()
        cols = list(map(math.floor, cols))

        for k in range(num_colors):
            color = hex(cols[k])
            # color 0xが先頭につくのでカット
            color = color[2:]
            # 6桁になるまで0で埋める
            while len(color) < 6:
                color = "0" + color

            # カラーコードの先頭に#をつける
            color = "#" + color
            color_dict[k] = color

        return color_dict

     