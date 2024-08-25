def max_min(list):
    max,min=float('-inf'),float('inf')
    maxi,mini=float('-inf'),float('inf')
    for i in range(len(list)):
        if list[i]>max:
            max=list[i]
            maxi=i
        if list[i]<min:
            min=list[i]
            mini=i
    return max,maxi,min,mini
list=list(map(int,input("Enter the list").split()))
max,maxi,min,mini=max_min(list)
print(f"The max is {max} in {maxi} and min is {min} in {mini}")