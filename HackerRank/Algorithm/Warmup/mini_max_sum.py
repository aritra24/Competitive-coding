#!/bin/python

import sys


a,b,c,d,e = input().strip().split(' ')
a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]
num=[a,b,c,d,e]
num=sorted(num)
print(sum(num)-num[4],sum(num)-num[0])