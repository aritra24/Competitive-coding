#!/bin/python3

import sys


n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]
k=set(c)
count=0
for i in k:
    count+=c.count(i)//2
print(count)