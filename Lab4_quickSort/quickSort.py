# -*- coding: utf-8 -*-
'''
@author: Neil.YU
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: neil_yushengjian@foxmail.com
@software: PyCharm 2018.1.2
@file: quickSort.py
@time: 2020/5/2 13:36
@desc:
'''

import random


def quickSort(data: list, p: int, r: int) -> None:
    if p < r:
        q = Rand_Partition(data, p, r)
        quickSort(data, p, q - 1)
        quickSort(data, q + 1, r)


def Rand_Partition(data: list, p: int, r: int) -> int:
    i = random.randint(p, r)
    data[i], data[r] = data[r], data[i]
    pivot = data[r]
    i = p - 1
    for j in range(p, r):
        if data[j] <= pivot:
            i = i + 1
            data[i], data[j] = data[j], data[i]
    data[i + 1], data[r] = data[r], data[i + 1]

    return i + 1


def quickSort_plus(data: list, p: int, r: int) -> None:
    if p < r:
        a, b = Trisection(data, p, r)
        quickSort(data, p, a - 1)
        quickSort(data, b + 1, r)


def Trisection(data: list, p: int, r: int) -> tuple:
    """

    :param data:
    :param p:
    :param r:
    :return: the scope of the pivot
    """
    i = random.randint(p, r)
    data[i], data[p] = data[p], data[i]
    pivot = data[p]

    i, j, k = p + 1, r, p
    while i <= j:
        if data[i] < pivot:
            data[i], data[k] = data[k], data[i]
            i, k = i + 1, k + 1
        elif data[i] > pivot:
            data[j], data[i] = data[i], data[j]
            j -= 1
        else:
            i += 1

    return k, j


def quickSort_insertSort(data: list, p: int, r: int, k: int) -> None:
    if r - p > k:
        a, b = Trisection(data, p, r)
        quickSort_insertSort(data, p, a - 1, k)
        quickSort_insertSort(data, b + 1, r, k)
    else:
        insertSort(data, p, r)


def insertSort(data: list, p: int, r: int) -> None:
    for i in range(p + 1, r + 1):
        for j in range(i, p, -1):
            if data[j] < data[j - 1]:
                data[j], data[j - 1] = data[j - 1], data[j]
            else:
                break
