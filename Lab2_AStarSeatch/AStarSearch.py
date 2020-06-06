# -*- coding: utf-8 -*-
'''
@author: Neil.YU
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: neil_yushengjian@foxmail.com
@software: PyCharm 2018.1.2
@file: AStarSearch.py
@time: 2020/5/1 00:18
@desc:
'''
import heapq
import numpy as np
from myClass import point, node


def singleAStarSearch(Map: np.array, start: point, end: point) -> node:
    """

    :param Map: the topography of Map
    :param start: the start point
    :param end: the end point
    :return: the end node with the information of path
    """
    visitedMap = np.zeros(Map.shape)
    heap = []
    n = node(None, start, 0, end, False)
    # if the point n is the end point then over
    while (n.row != end.row or n.column != end.column):
        # find the possible area
        row_low = n.row - 1 if n.row > 0 else n.row
        row_high = n.row + 1 if n.row < Map.shape[0] - 1 else n.row
        column_low = n.column - 1 if n.column > 0 else n.column
        column_high = n.column + 1 if n.column < Map.shape[1] - 1 else n.column
        # extend the path from point n
        for i in range(row_low, row_high + 1):
            for j in range(column_low, column_high + 1):
                # skip the point n ,visited point and unreachable point
                if (i == n.row and j == n.column) or visitedMap[i][j] or Map[i][j] < 0: continue
                # push the new node into heap and mark it as visited
                heapq.heappush(heap, node(n, point(i, j), Map[i][j], end, False))
                visitedMap[i][j] = 1
        # if no path can arrive at the end point then return None
        if len(heap) == 0: return None
        n = heapq.heappop(heap)

    return n


def bidirectionalAStarSearch(Map: np.array, start: point, end: point) -> tuple:
    """

    :param Map:
    :param start:
    :param end:
    :return:
    """
    visitedMap = np.zeros(Map.shape)
    visitedMap_reverse = np.zeros(Map.shape)

    heap, heap_reverse = [node(None, start, 0, end, False)], [node(None, end, 0, start, True)]
    n = heapq.heappop(heap) if heap[0] < heap_reverse[0] else heapq.heappop(heap_reverse)
    # if the point is visited in the another path then break
    while True:
        # if point belong to the path from end to start
        if n.reverse:
            if visitedMap[n.row][n.column]:
                break
            # find the possible area
            row_low = n.row - 1 if n.row > 0 else n.row
            row_high = n.row + 1 if n.row < Map.shape[0] - 1 else n.row
            column_low = n.column - 1 if n.column > 0 else n.column
            column_high = n.column + 1 if n.column < Map.shape[1] - 1 else n.column
            # extend the path from point n
            for i in range(row_low, row_high + 1):
                for j in range(column_low, column_high + 1):
                    # skip the point n ,visited point and unreachable point
                    if (i == n.row and j == n.column) or visitedMap_reverse[i][j] or Map[i][j] < 0: continue
                    new_node = node(n, point(i, j), Map[i][j], start, True)
                    heapq.heappush(heap_reverse, new_node)
                    visitedMap_reverse[i][j] = 1
        # if point belong to the path from start to end
        else:
            if visitedMap_reverse[n.row][n.column]:
                break
            # find the possible area
            row_low = n.row - 1 if n.row > 0 else n.row
            row_high = n.row + 1 if n.row < Map.shape[0] - 1 else n.row
            column_low = n.column - 1 if n.column > 0 else n.column
            column_high = n.column + 1 if n.column < Map.shape[1] - 1 else n.column
            # extend the path from point n
            for i in range(row_low, row_high + 1):
                for j in range(column_low, column_high + 1):
                    # skip the point n ,visited point and unreachable point
                    if (i == n.row and j == n.column) or visitedMap[i][j] or Map[i][j] < 0: continue
                    new_node = node(n, point(i, j), Map[i][j], end, False)
                    heapq.heappush(heap, new_node)
                    visitedMap[i][j] = 1
        # if no path can arrive at the end point then return None
        if len(heap) == 0 or len(heap_reverse) == 0: return None, None
        n = heapq.heappop(heap) if heap[0] < heap_reverse[0] else heapq.heappop(heap_reverse)

    # if point belong to the path from end to start
    if n.reverse:
        for m in heap:
            if m.row == n.row and m.column == n.column:
                return m, n
    # if point belong to the path from start to end
    else:
        for m in heap_reverse:
            if m.row == n.row and m.column == n.column:
                return n, m
