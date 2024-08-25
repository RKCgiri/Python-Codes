from numpy import random
import numpy as np

'''

row1=int(input("Enter the row size"))
col1=int(input("Enter the column size"))

a=random.randint(0,5,size=(row1,col1))
print(a)
row2=int(input("Enter row of 2nd matrix"))
col2=int(input("Enter column of 2nd matrix"))
if(row1!=col2):
    print("Matrix multipication is not possible")
else:
    b=random.randint(10,size=(row2,col2))
    print("First matrix is=\n",a)
    print("Second matrix is \n",b)
    mul=np.zeros((row1,col2),dtype=int)
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):# or len(a[0])
                mul[i][j]+=a[i][k]*b[k][j]
            
    print("The result is=\n",mul)'''
  

'''
# using numpy function

b=random.randint(10,size=(2,3))
print(b)
print("The result is=\n",np.dot(a,b))
'''
# using recursive function

def matrix_multiply_recursive(A, B):
	# check if matrices can be multiplied
	if len(A[0]) != len(B):
		raise ValueError("Invalid matrix dimensions")

	# initialize result matrix with zeros
	result = [[0 for j in range(len(B[0]))] for i in range(len(A))]

	# recursive multiplication of matrices
	def multiply(A, B, result, i, j, k):
		if i >= len(A):
			return
		if j >= len(B[0]):
			return multiply(A, B, result, i+1, 0, 0)
		if k >= len(B):
			return multiply(A, B, result, i, j+1, 0)
		result[i][j] += A[i][k] * B[k][j]
		multiply(A, B, result, i, j, k+1)

	# perform matrix multiplication
	multiply(A, B, result, 0, 0, 0)
	return result


# example usage
A = [[12, 7, 3], [4, 5, 6], [7, 8, 9]]
B = [[5, 8, 1, 2], [6, 7, 3, 0],[4, 5, 9, 1]]

result = matrix_multiply_recursive(A, B)
print(result)
for row in result:
	print(row)




