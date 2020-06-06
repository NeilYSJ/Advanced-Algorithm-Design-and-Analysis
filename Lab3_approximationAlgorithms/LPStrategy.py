# -*- coding: utf-8 -*-
'''
@author: Neil.YU
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: neil_yushengjian@foxmail.com
@software: PyCharm 2018.1.2
@file: LPStrategy.py
@time: 2020/5/5 16:35
@desc:
'''

from pulp import *


def LPSetCover(X: list, F: dict) -> list:
    f = [0] * len(X)
    cost = dict()
    for key in F.keys():
        temp = [0] * len(X)
        for i in F[key]:
            temp[i - 1] = 1
            f[i - 1] += 1
        cost[key] = temp
    # create the problem
    prob = LpProblem('SetCover', LpMinimize)
    # create the variable
    ingredient_vars = LpVariable.dicts("F", F.keys(), 0, 1, cat=LpContinuous)
    # add the objective function
    prob += lpSum([ingredient_vars[key] for key in F.keys()])
    # add the constraint
    for x in X:
        prob += lpSum(cost[key][x - 1] * ingredient_vars[key] for key in F.keys()) >= 1.0
    # solve
    prob.solve()

    C = []
    for key in F.keys():
        if ingredient_vars[key].value() >= 1.0 / max(f):
            C.append(key)
    C.sort()

    # print(max(f))
    """
    # Output the result
    S=list(F.keys())
    S.sort()
    print("1/f:%.4f" % (1.0/max(f)))
    i=-1
    for s in S:
        i+=1
        if i!=0 and i%5==0: print("")
        print(s,"%.4f"%ingredient_vars[s].value(),end='\t')
    print("")
    print("C:",end='')
    print(C)
    """
    return C
