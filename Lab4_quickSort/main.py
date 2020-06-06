# -*- coding: utf-8 -*-
'''
@author: Neil.YU
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: neil_yushengjian@foxmail.com
@software: PyCharm 2018.1.2
@file: main.py
@time: 2020/5/1 20:06
@desc:
'''

import random
import time
import operator
import sys
import copy
import numpy as np
from draw import drawT, drawResult, drawResult_plus, drawResult_insert
from quickSort import quickSort, quickSort_plus, quickSort_insertSort


def dataGeneration(N: int, rate: int) -> list:
    """

    :param N: the number of data
    :param rate: 0.1*rate denote the repetition rate of data
    :return:
    """
    if rate == 10:
        return [random.randint(0, N)] * N
    if rate == 0:
        return random.sample(range(0, N), N)

    M = int(N * 0.1 * rate)
    no_repeat = random.sample(range(0, N), N - M + 1)
    # select N-M numbers from no_repeat
    index = random.randint(0, len(no_repeat) - 1)
    repeat = [no_repeat[index]] * (M - 1)
    # disorder the data
    data = no_repeat + repeat
    random.shuffle(data)

    return data


def testT(N: int):
    T, t = [], []
    for k in range(0, 100, 4):
        print(k)
        data = dataGeneration(N, 0)
        T.append(k)
        start = time.time()
        quickSort_insertSort(data, 0, N - 1, k)
        end = time.time()
        t.append(end - start)
    drawT(T, t, 'quickSort_insertSort')


if __name__ == '__main__':
    sys.setrecursionlimit(1000000)  # change the depth of recursion
    N = 10 ** 4
    # testT(N)

    rate, t_system, t_lab, t_lab_plus, t_lab_insert = [], [], [], [], []
    for i in range(0, 11):
        data2 = dataGeneration(N, i)
        data3 = copy.deepcopy(data2)
        data4 = copy.deepcopy(data2)
        print(i)
        # print("Before and After(repetition rate=%.1f):" % (i * 0.1))
        # print(data2)
        rate.append(0.1 * i)

        # quicksort in numpy
        start = time.time()
        data1 = np.sort(data2)
        end1 = time.time()
        # my quicksort
        quickSort(data2, 0, N - 1)
        end2 = time.time()
        # my quicksort_plus
        quickSort_plus(data3, 0, N - 1)
        end3 = time.time()
        # my quicksort_insertsort
        quickSort_insertSort(data4, 0, N - 1, 16)
        end4 = time.time()
        # record the time
        t_system.append(end1 - start)
        t_lab.append(end2 - end1)
        t_lab_plus.append(end3 - end2)
        t_lab_insert.append(end4 - end3)
        # result
        # print(data2)
        # print(data3)
        data1 = list(data1)
        print(operator.eq(data1, data2))
        print(operator.eq(data1, data3))
        print(operator.eq(data1, data4))

    label1 = 'quickSort in Numpy'
    label2 = 'my quickSort'
    label3 = 'my quickSort_plus'
    label4 = 'my quickSort_insertSort'
    # drawResult(rate, t_system, t_lab, label1, label2)
    # drawResult(rate, t_system, t_lab_plus, label1, label3)
    # drawResult(rate, t_system, t_lab_insert, label1, label4)
    # drawResult_plus(rate, t_system, t_lab, t_lab_plus, label1, label2, label3)
    # drawResult_plus(rate, t_system, t_lab_insert, t_lab_plus, label1, label4, label3)
    drawResult_insert(rate, t_system, t_lab, t_lab_plus, t_lab_insert, label1, label2, label3, label4)
