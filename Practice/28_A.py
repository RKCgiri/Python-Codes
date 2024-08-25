import math
len=int(input("Enter the Lenth of rectangle:"))
bre=int(input("Enter the Breadth of rectangle:"))
r=int(input("Enter the Redius of Circle:"))
area1=len*bre
perimeter=2*(len+bre)
area2=3.14*r*r
circum=2*math.pi*r
print("Area of Rectangle =",area1)
print("Perimeter of Rectangle =",perimeter)
print("Area of Circle =",area2)
print("Circum of Circle =",circum)