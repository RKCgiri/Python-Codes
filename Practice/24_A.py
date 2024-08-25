def count(list):
    l1=l2=l3=0
    for i in list:
        if(i>=26 and i<=35):
            l1+=1
        elif(i>=36 and i<=45):
            l2+=1
        elif(i>=46 and i<=55):
            l3+=1
    return l1,l2,l3
list=eval(input("Enter interger input"))
l1,l2,l3=count(list)
print(l1,l2,l3)


