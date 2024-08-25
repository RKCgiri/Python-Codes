def maxmin(l):
    #max,min=l[0],l[0]
    #maxind,minind=0,0
    '''for i in range(len(l)):
        if l[i]>max:
            max=l[i]
            maxind=i
        if l[i]<min:
            min=l[i]
            minind='''
    maxind=l.index(max(l))
    minind=l.index(min(l))
    return l[maxind],maxind,l[minind],minind
   # return max ,maxind,min,minind
l=eval(input("Enter the list with maximumvalule"))
max,maxind,min,minind=maxmin(l)
print(f"Maximum valule is {max} with index {maxind} and minimum valule is {min} with idex {minind}")
