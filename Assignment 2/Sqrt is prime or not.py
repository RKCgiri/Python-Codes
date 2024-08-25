import math
n=int(input("Enter a number "))
sqrt=-1
f=0
r=math.sqrt(n)
print(r)
for i in range(n//2):
    if i*i==n:
        sqrt=i
for i in range(2,sqrt//2+1):
    if sqrt % i==0:
        print ("Not prime ",sqrt)
        f=-1
        break
if f==0:
    print("Prime",sqrt)