# -*- coding: utf-8 -*-
'''
@author: Neil.YU
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: neil_yushengjian@foxmail.com
@software: PyCharm 2018.1.2
@file: enumeration.py
@time: 2020/4/6 16:19
@desc:
'''

from myClass import point


def isInTriangle(p: point, a: point, b: point, c: point) -> bool:
    """

    :param p:
    :param a:
    :param b:
    :param c:
    :return: wither point p in the triangle of a,b and c
    """
    # count the sign of Triangle
    signOfTrig = (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)
    if not signOfTrig: return False
    # count the sign of p with a,b a,c and b,c
    signOfAB = (b.x - a.x) * (p.y - a.y) - (b.y - a.y) * (p.x - a.x)
    if signOfAB * signOfTrig < 0: return False
    signOfCA = (a.x - c.x) * (p.y - c.y) - (a.y - c.y) * (p.x - c.x)
    if signOfCA * signOfTrig < 0: return False
    signOfBC = (c.x - b.x) * (p.y - c.y) - (c.y - b.y) * (p.x - c.x)
    if signOfBC * signOfTrig < 0: return False

    return True


def enumeration(Q: set) -> set:
    if len(Q) <= 3: return Q
    Qlist = list(Q)
    m = Qlist[0]
    # the leftmost point must be in the convex hull
    for n in Qlist:
        if n.x < m.x: m = n
    # P includes the points which are not in the convex hull
    P, N = set(), len(Q)
    P.add(m)
    for i in range(N - 2):
        a = Qlist[i]
        if a in P: continue
        for j in range(i + 1, N - 1):
            b = Qlist[j]
            if b in P: continue
            for k in range(j + 1, N):
                c = Qlist[k]
                if c in P: continue
                # if a in the triangle(b,c,m) then add a in P
                if isInTriangle(a, b, c, m):
                    P.add(a)
                    break
                # if b in the triangle(a,c,m) then add b in P
                if isInTriangle(b, a, c, m):
                    P.add(b)
                    break
                # if c in the triangle(b,a,m) then add c in P
                if isInTriangle(c, b, a, m):
                    P.add(c)
            # if a in P then select the next possible point
            if a in P: break
    P.remove(m)
    return Q - P
