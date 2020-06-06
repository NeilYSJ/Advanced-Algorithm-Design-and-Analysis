# -*- coding: utf-8 -*-
'''
@author: Neil.YU
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: neil_yushengjian@foxmail.com
@software: PyCharm 2018.1.2
@file: greedyStrategy.py
@time: 2020/5/5 15:53
@desc:
'''


def greedySetCover(X: list, F: dict) -> list:
    U = set(X)  # U<-X
    key_visited = []  # C<-null
    while len(U) > 0:
        cover_max, key, S = 0, -1, []
        # select the S which cover the set U most
        for i in F.keys():
            if i in key_visited: continue
            cover = len(U.intersection(set(F[i])))
            if cover > cover_max: cover_max, key, S = cover, i, F[i]
        key_visited.append(key)
        U = U.difference(S)

    return key_visited
