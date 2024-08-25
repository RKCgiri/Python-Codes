def swap(a,b):
    t=a
    a=b
    b=t
    return a,b   
l=eval(input("Enter the list element"))
print(l)
for i in range(len(l)//2):
    '''t=l[i]
    l[i]=l[len(l)-i-1]
    l[len(l)-i-1] =t'''
    l[i],l[len(l)-i-1]=swap(l[i],l[len(l)-1-i])
print(l)