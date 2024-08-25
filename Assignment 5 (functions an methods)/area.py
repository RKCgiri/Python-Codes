import math
def circle(r):
    return math.pi*r**2 
def square(l):
    return l*l
def rec(l,w):
    return l*w

n=1
while(n<4 and n>0):
    print("1->circle,2->rectangle,3->squre")
    n=int(input("Enter"))
    if n==1:
        print("Enter the radious of the circle")
        r=int(input())
        res=circle(r)
        print(f"The area of the circle is {res}")  # This is f string
    elif n==2:
        print("Enter the side of square")
        l=int(input())
        print(square(l))
    elif n==3:
        print("Enter the lengthe and width of the ractangle")
        l=int(input())
        w=int(input())
        print(rec(l,w))
    else:
        print("Wromg choise")