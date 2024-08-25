import math
n=int(input())
f=0
for i in range(2,int(math.sqrt(n))):
    if(n%i==0):
        f=-1
        break
if(f!=-1):
    print("prime")   