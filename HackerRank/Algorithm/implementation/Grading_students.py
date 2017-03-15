#!/bin/python3

import sys


n = int(input().strip())
for a0 in range(n):
    grade = int(input().strip())
    if 5-grade%5<3 and grade>=38:
        grade+=5-grade%5
    print(grade)
