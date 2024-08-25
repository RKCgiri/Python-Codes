largest,second=-1,-1
while True:
    n=input("Enter number ")
    if(n=='b'):break
    if(int(n)>largest):
        second=largest
        largest=int(n)
    elif (int(n)<largest and int(n)>second):
        second=int(n)
    
print(largest,second)
        