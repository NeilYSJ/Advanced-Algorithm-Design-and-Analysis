# -*- coding: utf-8 -*-
'''
@author: Neil.YU
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: neil_yushengjian@foxmail.com
@software: PyCharm 2018.1.2
@file: main.py
@time: 2020/4/6 14:21
@desc:
'''

import random
import time
import sys

from myClass import point, drawPoint, drawResult
from enumeration import enumeration
from grahamScan import grahamScan
from divideConquer import divideConquer


def pointSet(N: int, limit=100) -> set:
    """

    :param N: the number of points
    :param limit: the restrict of points' area
    :return: set Q which includes N points
    """
    Q = set()
    while len(Q) < N:
        a = point(random.randint(0, limit), random.randint(0, limit))
        Q.add(a)  # if point a is in Q before added, Q will no change
    return Q


if __name__ == '__main__':
    sys.setrecursionlimit(100000)  # change the depth of recursion
    x_start, x_end, x_step = 100, 200, 100

    X, Y1, Y2, Y3 = [], [], [], []

    for N in range(x_start, x_end, x_step):
        Q = pointSet(N)
        print(N)
        X.append(N)
        start = time.time()
        # enumeration
        # P1=set()
        P1 = enumeration(Q)
        end1 = time.time()
        # grahamScan
        # P2=set()
        P2 = grahamScan(Q)
        end2 = time.time()
        # divideConquer
        # P3=set()
        P3 = divideConquer(Q)
        end3 = time.time()

        print(N, end1 - start)
        print(N,end2 - end1)
        print(N,end3 - end2)

        Y1.append(end1 - start)
        Y2.append(end2 - end1)
        Y3.append(end3 - end2)
    
        drawPoint(Q, P1, P2, P3)
    print(Y1)
    print(Y2)
    print(Y3)
    #drawResult(X, Y1, Y2, Y3, x_end, int(max(Y1)))
