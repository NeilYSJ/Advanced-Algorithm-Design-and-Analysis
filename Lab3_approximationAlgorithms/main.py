# -*- coding: utf-8 -*-
'''
@author: Neil.YU
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: neil_yushengjian@foxmail.com
@software: PyCharm 2018.1.2
@file: main.py
@time: 2020/5/1 23:13
@desc:
'''

import random
import time
from greedyStrategy import greedySetCover
from LPStrategy import LPSetCover
from enumeration import enumerationCover
from printResult import printGreedyResult, printLPResult, judge, drawResult


def dataGeneration_old(N: int, M: int) -> tuple:
    X = [i for i in range(1, N + 1)]
    F = dict()
    F['S0'] = random.sample(X, M)
    F['S0'].sort()
    U = set(F['S0'])
    j = 1
    # make sure the feasible solution
    while True:
        Y = list(set(X).difference(U))  # X-U
        if len(Y) < M:
            F['S' + str(j)] = Y
            j += 1
            break
        n = random.randint(1, M)
        x = random.randint(1, n)
        F['S' + str(j)] = random.sample(Y, x) + random.sample(list(U), n - x)
        F['S' + str(j)].sort()
        U = U.union(set(F['S' + str(j)]))
        j += 1
    # make F up (because j must be less than N)
    while j < N:
        n = random.randint(1, M)
        F['S' + str(j)] = random.sample(X, n)
        F['S' + str(j)].sort()
        j += 1

    return X, F


def dataGeneration_new(N: int, M: int, f: int) -> tuple:
    X = [i for i in range(1, N + 1)]
    number, max = [0] * N, random.randint(1, N + 1)
    Full = set()

    F = dict()
    F['S0'] = random.sample(X, M)
    F['S0'].sort()
    for x in F['S0']:
        number[x - 1] += 1  # count the number of each x
        if number[x - 1] == f:  Full.add(x)
    U = set(F['S0'])

    j = 1
    # make sure the feasible solution
    while True:
        Y = list(set(X).difference(U))  # X-U
        if len(Y) < M:
            F['S' + str(j)] = Y
            for x in F['S' + str(j)]:
                number[x - 1] += 1  # count the number of each x
                if number[x - 1] == f:  Full.add(x)
            j += 1
            break

        n = random.randint(1, M)
        x = random.randint(1, n)
        F['S' + str(j)] = random.sample(Y, x) + random.sample(list(U - Full), n - x)
        for x in F['S' + str(j)]:
            number[x - 1] += 1  # count the number of each x
            if number[x - 1] == f:  Full.add(x)
        F['S' + str(j)].sort()
        U = U.union(set(F['S' + str(j)]))
        j += 1
    # make F up (because j must be less than N)
    while j < N:
        n = random.randint(1, M)
        F['S' + str(j)] = random.sample(list(set(X) - Full), n)

        if number[max - 1] < f and max not in F['S' + str(j)]:
            F['S' + str(j)][0] = max  # make sure the number of max is f
        for x in F['S' + str(j)]:
            number[x - 1] += 1  # count the number of each x
            if number[x - 1] == f:  Full.add(x)

        F['S' + str(j)].sort()
        j += 1

    return X, F


def countGreedyRatio(M: int) -> float:
    sum = 0
    for i in range(1, M + 1):
        sum += 1.0 / i
    return sum


def ratio_LPSetCover():
    N, M = 50, 15  # N must be larger than M

    A, B1, B3 = [], [], []
    for f in range(12, 40, 4):
        ratio1 = f
        print(f, ratio1)
        A.append(f)
        X, F = dataGeneration_new(N, M, f)

        C3 = LPSetCover(X, F)  # the key of sets in F
        print(len(C3))
        C1 = enumerationCover(X, F)
        print(len(C1))

        B1.append(ratio1)
        ratio3 = len(C3) * 1.0 / len(C1)
        B3.append(ratio3)
    drawResult(A, B1, B3, 'LPSetCover(N=' + str(N) + ')', 'Theoretical', 'Actual', 'f')


def ratio_GreedyCover():
    N = 30  # N must be larger than M

    A, B1, B2 = [], [], []
    for M in range(5, 30, 5):
        ratio1 = countGreedyRatio(M)
        print(M, ratio1)
        A.append(M)
        X, F = dataGeneration_old(N, M)

        C1 = greedySetCover(X, F)  # the key of sets in F
        print(len(C1))
        C3 = enumerationCover(X, F)
        print(len(C3))

        B1.append(ratio1)
        ratio2 = len(C1) * 1.0 / len(C3)
        B2.append(ratio2)
    drawResult(A, B1, B2, 'GreedyCover(N=' + str(N) + ')', 'Theoretical', 'Actual', 'The max number of |S|')


if __name__ == '__main__':
    N, M = 50, 20  # N must be larger than M
    X, F = dataGeneration_old(N, M)
    print(N)

    start1 = time.time()
    C1 = greedySetCover(X, F)  # the key of sets in F
    end1 = time.time()
    # printGreedyResult(X, F, C1)
    # judge(X,F,C1)
    print(len(C1), end1 - start1)
    # print(C1)

    start2 = time.time()
    C2 = LPSetCover(X, F)
    end2 = time.time()
    # printLPResult(X, F, C2)
    # judge(X,F,C2)
    print(len(C2), end2 - start2)
    # print(C2)

    """
    start3 = time.time()
    C3 = enumerationCover(X, F)
    end3 = time.time()
    printLPResult(X, F, C3)
    judge(X, F, C3)
    print(len(C3), end3 - start3)
    """

    # ratio_LPSetCover()
    # ratio_GreedyCover()
