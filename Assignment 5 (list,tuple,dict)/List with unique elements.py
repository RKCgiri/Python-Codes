import pandas as pd
import numpy as np
def unique(l):
    
    '''x=[]
    for a in l:
        if( a not in x):
            x.append(a)
    return x'''
   # By using set()         
    ''' list_set=set(l)
    unique_list=list(list_set)
    return unique_list'''
    # By using pandas
    '''unique=pd.Series(l).drop_duplicates().tolist()
    return unique'''
    # By using numpy
    element=np.array(l)
    return np.unique(element)

l=list(map(int,input("Enter the list elements").split()))
print("The lists elements are = ",l)
x=unique(l)
print("The list of unique elements are = ",x)




