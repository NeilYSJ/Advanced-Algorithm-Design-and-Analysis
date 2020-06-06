# -*- coding: utf-8 -*-
'''
@author: Neil.YU
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: neil_yushengjian@foxmail.com
@software: PyCharm 2018.1.2
@file: printResult.py
@time: 2020/5/5 20:20
@desc:
'''

import operator
import matplotlib.pyplot as plt


def printGreedyResult(X: list, F: dict, C: list) -> None:
    U = set()
    for key in C:
        # uncover:
        uncover = list(set(X).difference(U))
        uncover.sort()
        print("uncover:", end='')
        print(uncover)
        # select
        S = F[key]
        print(str(key) + ":", end='')
        print(S)
        # new cover
        print("new cover:", end='')
        add = list(set(S).difference(U))
        add.sort()
        print(add)
        U = U.union(set(S))
        print('')

    print("Union of C:")
    U = list(U)
    U.sort()
    print(U)
    print("X:")
    print(X)


def printLPResult(X: list, F: dict, C: list) -> None:
    U = set()
    for key in C:
        S = F[key]
        U = U.union(set(S))
    print("Union of C:")
    U = list(U)
    U.sort()
    print(U)
    print("X:")
    print(X)


def judge(X: list, F: dict, C: list) -> None:
    U = set()
    for key in C:
        S = F[key]
        U = U.union(set(S))
    U = list(U)
    U.sort()
    print(operator.eq(U, X))


def drawResult(X: list, Y1: list, Y2: list, label: str, label1: str, label2: str, xlabel: str) -> None:
    plt.title(label)
    plt.xlim(xmax=max(X) * 1.1, xmin=-max(X) * 0.1)
    plt.ylim(ymax=max(max(Y1), max(Y2)) * 1.1, ymin=0)
    plt.xlabel(xlabel)
    plt.ylabel('Ratio')
    plt.plot(X, Y1, label=label1, color="red", marker="o")
    plt.plot(X, Y2, label=label2, color="green", marker="<")
    for i in range(len(X)):
        plt.text(X[i], Y1[i], '%.3g' % Y1[i], ha='center', va='bottom')
        plt.text(X[i], Y2[i], '%.3g' % Y2[i], ha='center', va='bottom')

    plt.legend()
    plt.show()
