import math
l=list(map(int,input("Enter the number ").split()))
print(l)
length=len(l)
sum=0
for i in l:
    sum+=i
mean=sum/length

s=0
for i in l:
    s+=(i-mean)**2
variance=s/length
stdev=variance**.5
stdev=math.sqrt(variance)

print(mean,variance,stdev)
    