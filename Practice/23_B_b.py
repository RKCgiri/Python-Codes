row1=int(input("enter the row  of 1st matrix"))
col1=int(input("enter the  col of 1st matrix"))
print(row1,col1)
print("Enter the matrix elements ")
m1=[]
print(m1)
for i in range(row1):
    r=[]
    for j in range(col1):
        r.append(int(input()))
    m1.append(r)
row2=int(input("enter the row  of 1st matrix"))
col2=int(input("enter the  col of 1st matrix"))
print(row2,col2)
print("Enter the matrix elements ")
m2=[]
print(m1)
print(m2)
for i in range(row2):
    r=[]
    for j in range(col2):
        r.append(int(input()))
    m2.append(r)
print(m2)


m3=[]
for i in range(row1):
    r=[]
    for j in range(col1):
       r.append(m1[i][j]*m2[i][j]) 
    m3.append(r)
print(m3)