# -*- coding: utf-8 -*-
'''
@author: Neil.YU
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: neil_yushengjian@foxmail.com
@software: PyCharm 2018.1.2
@file: divideConquer.py
@time: 2020/4/6 16:21
@desc:
'''

from myClass import point
from grahamScan import grahamScan, quickSort


def median(Qlist: list) -> int:
    min, max = Qlist[0].x, Qlist[0].x
    for q in Qlist:
        if q.x > max: max = q.x
        if q.x < min: min = q.x
    return (min + max) // 2


def divideAndConquer(Qlist: list) -> list:
    N = len(Qlist)
    if N < 3: return Qlist
    flag = 1  # whether there is a line
    for i in range(N):
        if Qlist[i].x != Qlist[0].x:
            flag = 0
            break
    if N == 3 or flag:
        # choose the point which have the min of y as the first point
        for i in range(N):
            if Qlist[i].y < Qlist[0].y: Qlist[i], Qlist[0] = Qlist[0], Qlist[i]
        quickSort(Qlist, 1, N - 1)
        return Qlist
    # Divide
    x_median = median(Qlist)
    # Conquer
    QL = divideAndConquer([q for q in Qlist if q.x <= x_median])
    QR = divideAndConquer([q for q in Qlist if q.x > x_median])
    # Merge
    if len(QR) > 0:
        QR_ymax, tip = QR[0], 0
        for q in range(0, len(QR)):
            if QR_ymax.y < QR[q].y:
                QR_ymax, tip = QR[q], q
            else:
                break
        # QR[0] denotes u and QR[tip] denotes v
        new_Q = QL + QR[:tip + 1] + QR[len(QR) - 1:tip:-1]
    else:
        new_Q = QL

    return list(grahamScan(set(new_Q)))


def divideConquer(Q: set) -> set:
    Qlist = list(Q)
    P = divideAndConquer(Qlist)

    return set(P)
