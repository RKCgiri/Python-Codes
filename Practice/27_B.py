import numpy as np
from numpy import random
def add(m1,m2):
    return m1+m2
def fileh(m1,m2,res):
    with open("matrix.txt",'w') as f:
        f.write(f" The sum of the matrix {m1} and {m2} is {res}")
      
m1=random.randint(10,20,size=(3,3))
m2=random.randint(10,20,size=(3,3))
print(m1)
print(m2)
m3=add(m1,m2)
print(m3)
fileh(m1,m2,m3)