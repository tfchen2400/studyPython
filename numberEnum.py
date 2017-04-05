#!/usr/bin/env python3
from enum import Enum
Animal = Enum('Animal','ant bee cat dog')

print(Animal.ant)
print(repr(Animal.ant))
print(Animal.ant == 1)
type(Animal.ant)
print('----------------')
