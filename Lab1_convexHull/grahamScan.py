# -*- coding: utf-8 -*-
'''
@author: Neil.YU
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: neil_yushengjian@foxmail.com
@software: PyCharm 2018.1.2
@file: grahamScan.py
@time: 2020/4/6 16:20
@desc:
'''
from myClass import point, vector


def cos(ab: vector) -> float:
    """

    :param ab:
    :return: the cos of vector ab and vector (1,0)
    """
    ac = vector(1, 0)
    return (ab.x * ac.x + ab.y * ac.y) / (ab.norm() * ac.norm())


def cross(a: vector, b: vector) -> int:
    """

    :param a:
    :param b:
    :return: a cross b
    """
    return a.x * b.y - a.y * b.x


def distance(a: point, b: point) -> int:
    return (a.x - b.x) ** 2 + (a.y - b.y) ** 2


def quickSort(Qlist, low, high):
    if low < high:
        i = low - 1
        pivot = cos(vector(Qlist[high].x - Qlist[0].x, Qlist[high].y - Qlist[0].y))
        dis = distance(Qlist[high], Qlist[0])

        for j in range(low, high):
            if cos(vector(Qlist[j].x - Qlist[0].x, Qlist[j].y - Qlist[0].y)) > pivot:
                i = i + 1
                Qlist[i], Qlist[j] = Qlist[j], Qlist[i]
                continue
            # because we choose the min y with the possible max x as the start point
            # so we need sort the points which have the same cos value from far to near
            if cos(vector(Qlist[j].x - Qlist[0].x, Qlist[j].y - Qlist[0].y)) == pivot:
                if distance(Qlist[j], Qlist[0]) > dis:
                    i = i + 1
                    Qlist[i], Qlist[j] = Qlist[j], Qlist[i]
        Qlist[i + 1], Qlist[high] = Qlist[high], Qlist[i + 1]

        quickSort(Qlist, low, i + 1 - 1)
        quickSort(Qlist, i + 1 + 1, high)


def grahamScan(Q: set) -> set:
    P = set()
    Qlist, N = list(Q), len(Q)
    if N < 3: return P
    # choose the point which have the min of y as the start point
    for i in range(N):
        if Qlist[i].y < Qlist[0].y:
            Qlist[i], Qlist[0] = Qlist[0], Qlist[i]
            continue
        # if points have the same y then choose the point which have the max x
        if Qlist[i].y == Qlist[0].y and Qlist[i].x > Qlist[0].x:
            Qlist[i], Qlist[0] = Qlist[0], Qlist[i]
    quickSort(Qlist, 1, N - 1)

    stack = []
    stack.append(Qlist[0])
    stack.append(Qlist[1])
    stack.append(Qlist[2])
    for i in range(3, N):
        stack_len = len(stack)
        top, next_top = stack[stack_len - 1], stack[stack_len - 2]
        a = vector(Qlist[i].x - next_top.x, Qlist[i].y - next_top.y)
        b = vector(top.x - next_top.x, top.y - next_top.y)
        # delete the top(stack) on the left of the line which from next_top(stack) to Qlist[i]
        while stack_len > 2 and cross(a, b) >= 0:
            stack.pop()
            stack_len = len(stack)
            top, next_top = stack[stack_len - 1], stack[stack_len - 2]
            a = vector(Qlist[i].x - next_top.x, Qlist[i].y - next_top.y)
            b = vector(top.x - next_top.x, top.y - next_top.y)
        stack.append(Qlist[i])

    P = set(stack)
    return P
