#!/bin/python3

import sys


q = int(input().strip())
for a0 in range(q):
    x,y,z = input().strip().split(' ')
    x,y = [int(x)-int(z),int(z)-int(y)]
    x=abs(x)
    y=abs(y)
    if x==y:
        print('Mouse C')
    elif x>y :
        print('Cat B')
    else:
        print('Cat A')