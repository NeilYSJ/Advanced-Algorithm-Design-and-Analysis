# -*- coding: utf-8 -*-
'''
@author: Neil.YU
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: neil_yushengjian@foxmail.com
@software: PyCharm 2018.1.2
@file: enumeration.py
@time: 2020/5/11 15:20
@desc:
'''

from itertools import combinations


def enumerationCover(X: list, F: dict) -> list:
    index = F.keys()
    for i in range(1, len(index)):
        print(i)
        temp = list(combinations(index, i))
        print(len(temp))
        for keys in temp:
            C = set()
            for key in keys:
                C = C.union(set(F[key]))
            if len(C) == len(X):
                return list(keys)
    return []
