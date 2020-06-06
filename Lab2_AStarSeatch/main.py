# -*- coding: utf-8 -*-
'''
@author: Neil.YU
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: neil_yushengjian@foxmail.com
@software: PyCharm 2018.1.2
@file: main.py
@time: 2020/4/30 16:12
@desc:
'''

import numpy as np
import time
from myClass import point, node, drawResult
from AStarSearch import singleAStarSearch, bidirectionalAStarSearch


def getMap_1() -> tuple:
    # -1 denotes the unreachable point, >=0 denotes the topography of point
    Map = np.zeros((14, 17))

    # add the topography
    Map[5][6] = Map[6][6] = Map[7][7] = Map[8][7] = Map[9][7] = Map[9][8] = Map[10][8] = Map[11][8] = -1

    # set the start point and end point
    start = point(8, 4)
    end = point(9, 13)

    return Map, start, end


def getMap_2() -> tuple:
    # -1 denotes the unreachable point, >=0 denotes the topography of point
    Map = np.zeros((20, 40))

    # add the topography
    # unreachable -1
    Map[0][3] = -1
    Map[2][0] = Map[2][1] = Map[2][2] = Map[2][3] = Map[2][4] = Map[2][5] = -1
    Map[0][7] = Map[1][7] = Map[2][7] = Map[2][8] = Map[2][9] = Map[2][10] = Map[3][8] = -1
    Map[0][12] = Map[1][12] = Map[2][12] = Map[3][12] = Map[4][12] = Map[5][12] = Map[6][12] = Map[7][12] = -1
    Map[5][8] = Map[5][7] = Map[6][7] = Map[7][7] = Map[6][6] = Map[6][5] = Map[6][4] = Map[6][3] = Map[6][2] = -1
    Map[7][5] = Map[8][5] = Map[9][5] = Map[10][5] = Map[11][5] = -1
    Map[11][4] = Map[11][3] = Map[11][2] = Map[10][2] = Map[12][3] = Map[13][3] = Map[14][3] = Map[15][3] = Map[16][
        3] = -1
    Map[15][4] = Map[15][5] = Map[15][6] = Map[15][7] = Map[15][8] = Map[14][8] = Map[13][8] = Map[13][9] = Map[12][8] = \
    Map[11][8] = Map[10][8] = Map[10][7] = Map[9][7] = -1
    Map[13][11] = Map[12][12] = Map[13][12] = Map[14][12] = Map[15][12] = Map[16][12] = Map[17][12] = Map[18][12] = \
    Map[19][12] = -1
    Map[18][3] = Map[19][3] = Map[17][7] = Map[18][7] = Map[19][7] = Map[15][24] = Map[15][25] = Map[16][24] = Map[16][
        25] = -1
    Map[10][19] = Map[11][19] = Map[12][19] = Map[10][20] = Map[11][20] = Map[12][20] = Map[10][21] = Map[11][21] = \
    Map[12][21] = -1
    Map[10][28] = Map[11][31] = Map[13][31] = Map[7][36] = Map[9][36] = -1
    # desert 4
    for i in range(24, 40): Map[0][i] = 4
    for i in range(25, 40): Map[1][i] = 4
    for i in range(26, 40): Map[2][i] = 4
    for i in range(26, 37): Map[3][i] = 4
    for i in range(26, 36): Map[4][i] = 4
    for i in range(27, 33): Map[5][i] = 4
    for i in range(27, 33): Map[6][i] = 4
    for i in range(29, 33): Map[7][i] = 4
    # river 2
    Map[1][34] = Map[2][33] = Map[3][32] = Map[4][33] = Map[5][33] = Map[5][34] = Map[6][33] = Map[6][34] = Map[7][33] = \
    Map[7][34] = Map[7][35] = 2
    Map[8][32] = Map[8][33] = Map[8][34] = Map[8][35] = Map[9][32] = Map[9][33] = Map[9][34] = Map[10][32] = Map[10][
        33] = Map[11][32] = 2
    Map[10][36] = Map[10][35] = Map[11][35] = Map[11][34] = Map[12][34] = Map[12][33] = Map[13][34] = Map[13][33] = \
    Map[13][32] = Map[14][34] = Map[14][33] = Map[14][32] = 2
    Map[15][33] = Map[15][32] = Map[15][31] = Map[16][33] = Map[16][32] = Map[16][31] = Map[17][32] = Map[17][31] = \
    Map[17][30] = 2
    Map[18][31] = Map[18][30] = Map[18][29] = Map[19][30] = Map[19][29] = Map[19][28] = 2

    # set the start point and end point
    start = point(10, 4)
    end = point(0, 35)

    return Map, start, end


if __name__ == '__main__':
    # single path in Map1
    Map, start, end = getMap_1()
    a=time.time()
    path = singleAStarSearch(Map, start, end)
    b=time.time()
    print("Cost of singlePATH in Map1:")
    if path:
        print(path.F)
        print("time:"+str(b-a))
    else:
        print('No path!')
    drawResult(Map, 1, start, end, [path])

    # bidirectional path in Map1
    a=time.time()
    path, path_reverse = bidirectionalAStarSearch(Map, start, end)
    b=time.time()
    print("Cost of bidirectionalPATH in Map1:")
    if path:
        print(path.G + path_reverse.G)
        print("time:"+str(b-a))
    else:
        print('No path!')
    drawResult(Map, 1, start, end, [path, path_reverse])

    # single path in Map2
    Map, start, end = getMap_2()
    a=time.time()
    path = singleAStarSearch(Map, start, end)
    b=time.time()
    print("Cost of singlePATH in Map2:")
    if path:
        print(path.G)
        print("time:"+str(b-a))
    else:
        print('No path!')
    drawResult(Map, 2, start, end, [path])

    # bidirectional path in Map2
    a=time.time()
    path, path_reverse = bidirectionalAStarSearch(Map, start, end)
    b=time.time()
    print("Cost of bidirectionalPATH in Map2:")
    if path:
        print(path.G + path_reverse.G)
        print("time:"+str(b-a))
    else:
        print('No path!')
    drawResult(Map, 2, start, end, [path, path_reverse])
