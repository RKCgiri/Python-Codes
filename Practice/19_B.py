import math
a=int(input("input a"))
b=int(input("input b"))
c=int(input("input c"))

d=(b**2)-(4*a*c)
s=math.sqrt(abs(d))
if(d>0):
    print("real and different")
    print((-b-s)/(2*a))
    print((-b+s)/(2*a))
elif(d==0):
    print("same real")
    print(-b/(2*a))
else:
    print("Complex")
    print(-b/(2*a),"+",s,"i")
    print(-b/(2*a),"-",s,"i")