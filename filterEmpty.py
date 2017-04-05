#!/usr/bin/env python3
#coding=utf-8
def not_empty(s):
    res = s and s.strip()
    print(res)
    return res
print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))