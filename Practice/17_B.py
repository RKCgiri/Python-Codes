def num(n,b):
    if(n==0): return 0
    l=[] 
    num(n//b,b)
    if(n!=0):
        if(n%b>=10):
            print(chr(ord('A')+n%b-10))
        else:
            print(n%b,end=" ")
n=int(input("Enter decimal num"))
b=int(input("Enter the base"))
num(n,b)