#!/usr/bin/env python3.6
# coding=utf-8
B = []


def move(n, a, b, c):
    if n == 1:
        buzhou = a + str(n) + '-->' + c + str(n)
        B.append(buzhou)
        return
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)


move(3, 'A', 'B', 'C')
print(B)
