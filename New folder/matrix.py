import numpy as np
from numpy import random

m1=random.randint(1,5,size=(3,3))
m2=random.randint(1,5,size=(3,3))
print(m1)
print(m2)
# m3=np.zeros((3,3),dtype=int)
# print(m3)

# for i in range(len(m1)):
#     for j in range(len(m2[0])):
#         for k in range(len(m1[0])):
#             m3[i][j]+=m1[i][k]*m2[k][j]
# print(m3)
# m3=np.dot(m1,m2)
# print(m3)
# s=np.trace(m1)
# print(s)
# s=0
# for i in range(len(m1)):
#     for j in range(len(m1[0])):
#         if i==j or i+j==2:
#             s+=m1[i][j]
# print(s)
# m3=np.add(m1,m2)
# print(m3)


