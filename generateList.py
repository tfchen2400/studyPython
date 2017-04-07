#!/usr/bin/env python3
# -*- coding: utf-8 -*-

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = []

for x in L1:
    if isinstance(x, str):
        L2.append(x)

print(L2)
