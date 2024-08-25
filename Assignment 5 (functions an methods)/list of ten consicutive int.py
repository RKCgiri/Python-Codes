def consicutive(l):
    l=sorted(l)
    isconsicutive=all(l[i]==l[i-1]+1 for i in range(1,len(l)))
    '''The all() function returns True if all items in an iterable are true,
    otherwise it returns False.
    If the iterable object is empty, the all()
    function also returns True.

'''
    return isconsicutive
l=list(map(int,input("Enter the list elements").split()))
print(consicutive(l))
def checkConsecutive(l):
    return sorted(l) == list(range(min(l), max(l)+1))
     
# Driver Code
lst = [2, 3, 1, 4, 5]
print(checkConsecutive(lst))
                      