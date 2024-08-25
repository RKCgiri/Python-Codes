import numpy as np
from numpy import random

def fun(s):
    avg=[]
    for i in range(len(s[0])):
        sum=0
        for j in range(len(s)):
            sum+=s[j][i]
        avg.append(sum/len(s))
    topper=0
    top=-1
    for i in range(len(s)):
        max=0
        for j in range(len(s[0])):
            max+=s[i][j]
        if top<max:
            top=max
            topper =i
    return avg,topper
s=[]
n=int(input("enter sutudents no "))
for i in range(n):
    s.append(random.randint(1,100,6))
print(s)
avg,top=fun(s)
print(avg,"\n",top)
