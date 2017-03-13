#!/bin/python3

import sys


n = int(input().strip())
a = []
fir=0
sec=0
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
for i in range(n):
    fir=fir+a[i][i]
    sec=sec+a[i][n-i-1]
print(abs(fir-sec))