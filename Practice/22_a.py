def status(list):
    l=[]
    for i in list:
        if(i<2):
            l.append('born')
        elif(i>=2 and i<=10):
            l.append('child')
        elif(i>=11 and i<=17):
            l.append('Young')
        elif(i>=18 and i<=49):
            l.append("adult")
        elif(i>=50 and i<=79):
            l.append('old')
        else:
            l.append('very old')
    return l
list=list(map(int,input("Enter the ages ").split()))
l=status(list)
print(l)
res=dict(zip(list,l))
print(res)
            