#!/usr/bin/env python3
#coding=utf-8
def isReverse(x):
    #赋值
    y = x
    n = 0
    #算数回数
    while(x != 0):
        m = x % 10
        n = n * 10 + m
        x = x / 10
        x = int(x)
    #返回是否是回数
    return y == n
L = filter(isReverse, range(1, 1000))
print(list(L))
    