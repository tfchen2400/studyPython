#!/usr/bin/env python3
#coding=utf-8
def is_odd(x):
    return x % 2 == 1
print(list(filter(is_odd,[1,3,5,7,9,8])))