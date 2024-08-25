from numpy import random
import numpy as np

row=int(input("Enter the row size"))
col=int(input("Enter the column size"))
a=random.randint(100,size=(row,col))
print(a)
'''
for i in range(row):
 
        # Initialize max1 to 0 at beginning
        # of finding max element of each row
        max1 = 0
        for j in range(col):
            if a[i][j] > max1:
                max1 = a[i][j]
 
        # print maximum element of each row
        print(max1)
#  Another approach
for i in a:
   print(max(i))
'''
print(np.amin(a,1))

