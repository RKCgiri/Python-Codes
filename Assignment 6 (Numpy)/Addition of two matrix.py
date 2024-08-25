from numpy import random
import numpy as np

row=int(input("Enter the row size"))
col=int(input("Enter the column size"))
add=np.zeros((row,col),dtype=int)
sub=np.zeros((row,col),dtype=int)
a=np.random.randint(100,size=(row,col))
b=np.random.randint(100,size=(row,col))
print("Printing elements of first matrix")
for row in a:
    for element in row:
        print(element, end=" ")
    print()
print(a)
print(b)
for i in range(len(a)):
    for j in range(len(a[0])):
        add[i][j]=a[i][j]+b[i][j]
        sub[i][j]=a[i][j]-b[i][j]
print("Addition is = \n",add,"\n Suntraction is =\n ",sub)

# Using numpy function
print(np.add(a,b))
print(np.subtract(a,b))




