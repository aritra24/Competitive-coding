#!/bin/python3

import sys


n = int(input().strip())
types = list(map(int, input().strip().split(' ')))
types.sort()
b=set(types)
k=0
ide=0
for i in b:
    if types.count(i)>k:
        k=types.count(i)
        ide=i
print(ide)