import numpy as np
from numpy import random
def Sortrow(r):
    return r.sort()

m=random.randint(10,20,size=(3,3))
print(m)
Sortrow(m[1])
print(m)
