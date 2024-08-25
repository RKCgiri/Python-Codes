import math
def fact(n):
    if(n==0): 
        return 1
    return n*fact(n-1)
n=int(input("enter the rannge"))
sum=0
j=1
x=int(input("Enter the num"))

for i in range(1,n+1):
    print(f"x^{i}/{i}!+",end=" ")
    sum+=math.pow(x,i)/(fact(i))
print("\n the sum is" ,sum)