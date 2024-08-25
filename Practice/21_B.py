n=int(input("Enter total term no"))
a=2
b=9
c=1
sum=0
for i in range(n):
    sum+=(a/b)*c
    c*=-1
    a+=3
    b+=4
print(sum)