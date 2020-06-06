# -*- coding: utf-8 -*-
'''
@author: Neil.YU
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: neil_yushengjian@foxmail.com
@software: PyCharm 2018.1.2
@file: myClass.py
@time: 2020/4/6 19:33
@desc:
'''
import math
import matplotlib.pyplot as plt


class point:
    x, y = 0, 0

    def __init__(self, x, y):
        self.x, self.y = x, y

    def view(self):
        return (self.x, self.y)

    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return int(str(self.x) + str(self.y))


class vector:
    x, y = 0, 0

    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'

    def view(self):
        return (self.x, self.y)

    def norm(self):
        return math.sqrt(self.x * self.x + self.y * self.y)


def drawPoint(Q: set, P1: set, P2: set, P3: set, minlimit=-10, maxlimit=110):
    plt.subplot(131)
    plt.title("enumeration")
    plt.xlim(xmax=maxlimit, xmin=minlimit)
    plt.ylim(ymax=maxlimit, ymin=minlimit)
    plt.xlabel("x")
    plt.ylabel("y")
    for q in Q - P1:
        plt.plot(q.x, q.y, 'ro')
    for p in P1:
        plt.plot(p.x, p.y, 'bs')

    plt.subplot(132)
    plt.title("grahamScan")
    plt.xlim(xmax=maxlimit, xmin=minlimit)
    plt.ylim(ymax=maxlimit, ymin=minlimit)
    plt.xlabel("x")
    plt.ylabel("y")
    for q in Q - P2:
        plt.plot(q.x, q.y, 'ro')
    for p in P2:
        plt.plot(p.x, p.y, 'bs')

    plt.subplot(133)
    plt.title("divideConquer")
    plt.xlim(xmax=maxlimit, xmin=minlimit)
    plt.ylim(ymax=maxlimit, ymin=minlimit)
    plt.xlabel("x")
    plt.ylabel("y")
    for q in Q - P3:
        plt.plot(q.x, q.y, 'ro')
    for p in P3:
        plt.plot(p.x, p.y, 'bs')

    plt.show()


def drawResult(X: list, Y1: list, Y2: list, Y3: list, Xlimit=10000, Ylimit=100):
    plt.subplot(121)
    plt.title("Enumeration")
    plt.xlim(xmax=max(X)*1.1, xmin=0)
    plt.ylim(ymax=max(Y1)*1.1, ymin=0)
    plt.xlabel("number")
    plt.ylabel("time")
    plt.plot(X, Y1, label="Enumeration", color="red", marker=".")
    for i in range(len(X)):
        plt.text(X[i],Y1[i],'%.4f' % Y1[i],ha='center', va= 'bottom')

    plt.subplot(122)
    plt.title("Graham-Scan&DivideConquer")
    plt.xlim(xmax=max(X)*1.1, xmin=0)
    plt.ylim(ymax=max(max(Y2),max(Y3))*1.1, ymin=0)
    plt.xlabel("number")
    plt.ylabel("time")
    plt.plot(X, Y2, label="Graham-Scan", color="blue", marker="o")
    plt.plot(X, Y3, label="DivideConquer", color="black", marker="<")
    for i in range(len(X)):
        plt.text(X[i], Y2[i], '%.4f' % Y2[i],ha='center', va= 'bottom')
        plt.text(X[i], Y3[i], '%.4f' % Y3[i],ha='center', va= 'bottom')
    plt.legend()
    plt.show()
