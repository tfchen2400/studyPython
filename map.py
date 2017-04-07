#!/usr/bin/env python3
# coding=utf-8
def f(x):
    return x * x


L = list(range(1, 11))
print(L)
r = map(f, L)
print(list(r))
