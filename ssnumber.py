#!/usr/bin/env python3
#coding=utf-8
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
#返回一个判断是否可以被N整除的函数
def _not_divisible(n):
    return lambda x : x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it)

for n in primes():
    print (n)