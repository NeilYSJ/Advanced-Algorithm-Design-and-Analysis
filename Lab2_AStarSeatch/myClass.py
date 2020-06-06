# -*- coding: utf-8 -*-
'''
@author: Neil.YU
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: neil_yushengjian@foxmail.com
@software: PyCharm 2018.1.2
@file: myClass.py
@time: 2020/5/1 00:15
@desc:
'''

import math
import numpy as np
from PIL import Image, ImageDraw, ImageFont


class point(object):
    def __init__(self, row, column):
        self.row, self.column = row, column


class node(object):
    def __init__(self, parent, n: point, topography: int, end: point, reverse: bool):
        self.row, self.column = n.row, n.column
        self.parent = parent
        self.reverse = reverse  # whether the path is reverse
        if parent == None:
            self.G = 0
            self.H = 0
        else:
            self.G = parent.G + math.sqrt(
                (self.row - parent.row) ** 2 + (self.column - parent.column) ** 2) + topography
            # self.H=abs(self.row-end.row)+abs(self.column-end.column)
            self.H = math.sqrt((self.row - end.row) ** 2 + (self.column - end.column) ** 2)
        self.F = self.G + self.H

    def __lt__(self, other):
        return self.F < other.F

    def __str__(self):
        return '(' + str(self.row) + ',' + str(self.column) + ')'


def drawResult(Map: np.array, order: int, start: point, end: point, path_list: list):
    """
    the left upper corner is the base point (0,0)
    X-axis pointing right, Y-axis pointing down
    :param Map: the topography of Map
    :param path: the end node with the information of path
    :param order: the order of Map
    :param bidirectional:
    :return:
    """
    im = Image.new('RGB', (Map.shape[1] * 100, Map.shape[0] * 100))
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype('Times New Roman.ttf', 80)
    # draw the grid and topography
    for i in range(Map.shape[1]):
        draw.line((i * 100, 0, i * 100, Map.shape[0] * 100), fill='#000000', width=5)  # black
        for j in range(Map.shape[0]):
            if Map[j][i] == -1:
                color = '#696969'  # grey
            elif Map[j][i] == 2:
                color = '#00BFFF'  # blue
            elif Map[j][i] == 4:
                color = '#FFD700'  # yellow
            else:
                color = '#FFFAFA'  # white
            draw.rectangle((i * 100, j * 100, (i + 1) * 100, (j + 1) * 100), fill=color)
    for j in range(Map.shape[0]):
        draw.line((0, j * 100, Map.shape[1] * 100, j * 100,), fill='#000000', width=5)  # black
    # draw the start point
    draw.text((start.column * 100 + 25, start.row * 100 + 5), 'S', fill='#000000', font=font)  # black
    # draw the end point
    draw.text((end.column * 100 + 25, end.row * 100 + 5), 'T', fill='#000000', font=font)  # black
    # draw the path or path_reverse
    color = '#FF0000'  # red
    for path in path_list:
        draw.ellipse((path.column * 100 + 40, path.row * 100 + 40, path.column * 100 + 60, path.row * 100 + 60),
                     fill=color)
        old_path, path = path, path.parent
        while path:
            draw.line(
                (old_path.column * 100 + 50, old_path.row * 100 + 50, path.column * 100 + 50, path.row * 100 + 50),
                fill=color, width=10)
            old_path, path = path, path.parent
        draw.ellipse(
            (old_path.column * 100 + 40, old_path.row * 100 + 40, old_path.column * 100 + 60, old_path.row * 100 + 60),
            fill=color)
        color = '#00FF00'  # green
    # im.show()
    if len(path_list) == 1:
        im.save(str(order) + '_SinglePATH.png', 'PNG')
    else:
        im.save(str(order) + '_BidirectionalPATH.png', 'PNG')
