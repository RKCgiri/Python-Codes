import math
n=int(input("Enter the num"))
for i in range(2,n+1):
    if(n%i==0):
        f=True
        for j in range(2,i):
            if(i%j==0):
                f=False
                break
        if(f==True):
          print(i,end=" ")