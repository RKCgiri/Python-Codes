import math
def Amstrong(n):
    m=n
    l=len(str(n))
    print(l)
    s=0
    while n!=0:
        r=n%10
        s+=r**l
        n//=10
    print(s)
    if s!=m:
        return False
    
    return True
print(Amstrong(153))
print(Amstrong(151))