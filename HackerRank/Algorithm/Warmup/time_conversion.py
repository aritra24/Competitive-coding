#!/bin/python3

import sys


time = input().strip().split(":")
if time[2][2]=="P":
    time[2]=time[2][0]+time[2][1]
    time[0]=str(int(time[0])%12+12)
elif time[2][2]=="A":
    time[2]=time[2][0]+time[2][1]
    time[0]=str(int(time[0])%12)
for i in range(3):
    if len(time[i])!=2:
        time[i]="0"+time[i]
print((":".join(time)))