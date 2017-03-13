#!/bin/python3

import sys


n = int(input().strip())
pos=0
neg=0
z=0
a = [int(arr_temp) for arr_temp in input().strip().split(' ')]
for i in range(n):
    if a[i]>0:
        pos=pos+1
    elif a[i]<0:
        neg=neg+1
    else:
        z=z+1
print(pos/n)
print(neg/n)
print(z/n)