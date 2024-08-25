a=int(input("Enter number"))
b=int(input("Enter number"))

for i in range(1,a+1):
    if(a %i==0 and b%i==0):
        hcf=i
lcm=a*b/hcf
print(hcf)
print(lcm)

