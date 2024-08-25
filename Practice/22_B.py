l=list(map(int,input("Enter the number").split()))
l3=list(map(int,input("Enter the number").split()))
s=l+l3 #it means append on the list
print(s)
print(l)
l1=[]
print("Enter list")
n=int(input("Enter no of elemnt"))
for i in range(n):
    a=int(input())
    l1.append(a)
print(l1)
l2=[]
print("Enter list")
for i in range(n):
    a=int(input())
    l2.append(a)
print(l2)

l3=[]
for i in range(n):
    l3.append(l1[i]+l2[i])
print(l3)