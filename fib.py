#!/usr/bin/env python3
#coding=utf-8
#ì³²¨ÄÇÆõÊýÁÐ
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a+b
        n = n + 1
    return 'done'
f = fib(100)
for i in range(100):
    print(next(f))