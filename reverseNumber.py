#!/usr/bin/env python3
# coding=utf-8
def isReverse(x):
    # ��ֵ
    y = x
    n = 0

    while (x != 0):
        m = x % 10
        n = n * 10 + m
        x = x / 10
        x = int(x)

    return y == n


L = filter(isReverse, range(1, 1000))
print(list(L))