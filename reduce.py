#!/usr/bin/env python3
# coding=utf-8
from functools import reduce


def add(x, y):
    return x + y


def gen(x):
    res = 1
    x = x - 1
    for i in range(1, x + 1):
        res = res * 3
    return res


l = [gen(x) for x in range(1, 4)]
print(l)
print(reduce(add, [1, 3, 9]))
