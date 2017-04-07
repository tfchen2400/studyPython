#!/usr/bin/env python3
# coding=utf-8
from functools import reduce


def str2float(s):
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    def fnPos(x, y):
        return x * 10 + y

    def fnNeg(x, y):
        return x * 0.1 + y * 0.1
        ##�Ƚ�ȡ ��mapreduce ��ƴ��

    # print(s[0])
    flag = True
    if (s[0] == '-'):
        s = s[1:]
        flag = False
    # print(s)
    s1 = s[0:s.find('.', 1)]
    s2 = s[s.find('.', 1) + 1:]
    s2 = '0' + s2[::-1]
    # print ((reduce(fnPos,map(char2num,s1)))+(reduce(fnNeg,map(char2num,s2))))
    # print (0 - (reduce(fnPos,map(char2num,s1)))+(reduce(fnNeg,map(char2num,s2))))
    if (flag == True):
        return (reduce(fnPos, map(char2num, s1))) + (reduce(fnNeg, map(char2num, s2)))
    else:
        return 0 - ((reduce(fnPos, map(char2num, s1))) + (reduce(fnNeg, map(char2num, s2))))


print('str2float(\'-123.456\') =', str2float('-123.456'))
# print (0 - 123.456)
