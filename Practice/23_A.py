def fact(n):
    if(n==0): 
        return 1
    return n*fact(n-1)
n=int(input("enter the rannge"))
sum=0
for i in range(n):
    print(f"1/{i}!+",end=" ")
    sum+=1/(fact(i))
print("\n the sum is" ,sum)