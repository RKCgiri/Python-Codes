def prime(n):
    l=[2]
    fl=[]
    p=True
    for i in range(3,n+1):
        for j in range(2,i):
            if(i%j==0):
                p=False
            
        if p==True:       
            l.append(i)
        if(len(l)>=2):
            sum=0
            for i in l:
                 sum+=i
            fl.append(sum)
    return fl

    
    
    
    
n =int(input("Enter the heighest no"))
list=[]
list=prime(n)
for i in list:
    print(i)