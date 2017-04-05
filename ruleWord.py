#!/usr/bin/env python3
#coding=utf-8
def normalize(x):
    L = [x[0].upper(),x[1:].lower()]
    res = ""
    for i in L:
        res = res + i
    return res
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)