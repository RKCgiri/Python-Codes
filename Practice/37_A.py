import math
def circle(r):
    return math.pi*r*r
def squere(l):
    return l*l
def rectangle(l,b):
    return l*b
def triagle(h,b):
    return .5*b*h

while True:
    n=int(input("1->circle,2->squre,3->rectangle,4->triangle,5->exit"))
    if n==1:
        r=float(input("Enter the radious of the circle "))
        print(circle(r))
    elif n==2:
        l=int(input("Enter the length "))
        print(squere(l))
    elif n==3:
        l=int(input("Enteer length "))
        b=int(input("Enter breath "))
        print(triagle(l,b))
    elif n==4:
        h=int(input("enter height of triangle"))
        b=int(input("base of triangle"))
        triagle(h,b)
    elif n==5:
        break
    else:
        print("Wrong chise")
    print()