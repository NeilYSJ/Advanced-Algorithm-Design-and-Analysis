# -*- coding: utf-8 -*-
'''
@author: Neil.YU
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: neil_yushengjian@foxmail.com
@software: PyCharm 2018.1.2
@file: draw.py
@time: 2020/5/2 20:32
@desc:
'''

import matplotlib.pyplot as plt


def drawT(X: list, Y: list, label: str) -> None:
    plt.title("test")
    plt.xlim(xmax=max(X) * 1.1, xmin=-max(X) * 0.1)
    plt.ylim(ymax=max(Y) * 1.1, ymin=0)
    plt.xlabel('k')
    plt.ylabel('time')
    plt.plot(X, Y, label=label, color="blue", marker="o")
    for i in range(len(X)):
        plt.text(X[i], Y[i], '%.3g' % Y[i], ha='center', va='bottom')
    plt.legend()
    plt.show()


def drawResult(X: list, Y1: list, Y2: list, label1: str, label2: str) -> None:
    plt.title("Compare with " + label1 + " and " + label2)
    plt.xlim(xmax=max(X) * 1.1, xmin=-max(X) * 0.1)
    plt.ylim(ymax=max(max(Y1), max(Y2)) * 1.1, ymin=0)
    plt.xlabel('Repetition rate')
    plt.ylabel('time')
    plt.plot(X, Y1, label=label1, color="blue", marker="o")
    plt.plot(X, Y2, label=label2, color="green", marker="<")
    for i in range(len(X)):
        plt.text(X[i], Y1[i], '%.3g' % Y1[i], ha='center', va='bottom')
        plt.text(X[i], Y2[i], '%.3g' % Y2[i], ha='center', va='bottom')

    plt.legend()
    plt.show()


def drawResult_plus(X: list, Y1: list, Y2: list, Y3: list, label1: str, label2: str, label3: str) -> None:
    plt.title("Compare with " + label1 + " , " + label2 + " and " + label3)
    plt.xlim(xmax=max(X) * 1.1, xmin=-max(X) * 0.1)
    plt.ylim(ymax=max(max(Y1), max(Y2), max(Y3)) * 1.1, ymin=0)
    plt.xlabel('Repetition rate')
    plt.ylabel('time')
    plt.plot(X, Y1, label=label1, color="blue", marker="o")
    plt.plot(X, Y2, label=label2, color="green", marker="<")
    plt.plot(X, Y3, label=label3, color="red", marker="s")
    for i in range(len(X)):
        plt.text(X[i], Y1[i], '%.3g' % Y1[i], ha='center', va='bottom')
        plt.text(X[i], Y2[i], '%.3g' % Y2[i], ha='center', va='bottom')
        plt.text(X[i], Y3[i], '%.3g' % Y3[i], ha='center', va='bottom')

    plt.legend()
    plt.show()


def drawResult_insert(X: list, Y1: list, Y2: list, Y3: list, Y4: list, label1: str, label2: str, label3: str,
                      label4: str) -> None:
    plt.title("Compare with " + label1 + " , " + label2 + " , " + label3 + " and " + label4)
    plt.xlim(xmax=max(X) * 1.1, xmin=-max(X) * 0.1)
    plt.ylim(ymax=max(max(Y1), max(Y2), max(Y3), max(Y4)) * 1.1, ymin=0)
    plt.xlabel('Repetition rate')
    plt.ylabel('time')
    plt.plot(X, Y1, label=label1, color="blue", marker="o")
    plt.plot(X, Y2, label=label2, color="black", marker="<")
    plt.plot(X, Y3, label=label3, color="red", marker="s")
    plt.plot(X, Y4, label=label4, color="green", marker="x")
    for i in range(len(X)):
        plt.text(X[i], Y1[i], '%.3g' % Y1[i], ha='center', va='bottom')
        plt.text(X[i], Y2[i], '%.3g' % Y2[i], ha='center', va='bottom')
        plt.text(X[i], Y3[i], '%.3g' % Y3[i], ha='center', va='bottom')
        plt.text(X[i], Y4[i], '%.3g' % Y4[i], ha='center', va='bottom')

    plt.legend()
    plt.show()
