import numpy as np
from numpy import random

def fun(s):
    for i in range(len(s)):
        for j in range(len(s[0])):
            s[i][j]+=5
s=[]
n=int(input("enter sutudents no "))
for i in range(n):
    s.append(random.randint(1,100,6))
print(s)
fun(s)
print(s)
