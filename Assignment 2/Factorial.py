def factorial( n):
    if n<=1:
        return 1
    else:
        return n * factorial(n-1)
# Factorial without recursion
def fact(n):
    f=1
    i=1
    for i in range(1,n+1):
        f=f*i
    return f
print("Enter the number to calculate factorial")
num=int(input())
f=factorial(num)
f2=fact(num)
print("The factorial of the number is ",f,f2)