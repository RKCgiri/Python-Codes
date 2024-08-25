from numpy import random
import numpy as np
# a=random.rand(3,2)  #It creates decimal number
# print(a)
# a=random.randint(100,200,7)  #It creates a 1D array of length 7
# print(a)
# a=random.randint(100,size=(3,2)) # Only high value is present
# print(a)
a=random.randint(-1,9,size=(3,3))
print(a)
s=0
for i in range(len(a[0])):
    for j  in range(len(a[0])):
        if(i==j or i+j==2):
            s+=a[i][j]
        
print(s)
s=0
for i in range(3):
    s+=a[i][i]+a[i][2-i]
print(s-a[1][1])


# It prints only principal diagonal
diagonal=np.diagonal(a)
print(diagonal)
print(sum(diagonal))
trace=np.trace(a)
print(trace)




