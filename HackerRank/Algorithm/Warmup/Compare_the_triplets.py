#!/bin/python3

import sys


a= input().strip().split(' ')
b= input().strip().split(' ')
al=0
bo=0
for i in range(3):
    if int(a[i])>int(b[i]):
        al=al+1
    elif int(a[i])<int(b[i]):
        bo=bo+1
print(al,bo)