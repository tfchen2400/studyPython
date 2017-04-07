#!/usr/bin/env python3
# coding=utf-8
from functools import reduce


def prod(L):
    def multip(x, y):
        return x * y;

    return reduce(multip, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
