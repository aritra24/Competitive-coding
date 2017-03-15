#!/bin/python3

import sys


s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
ap=0
ora=0
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]
for i in apple:
    if a+i in range(s,t+1):
        ap=ap+1
for i in orange:
    if b+i in range(s,t+1):
        ora=ora+1
print(ap)
print(ora)