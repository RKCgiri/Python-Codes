list1=list(map(int,input("ENter num").split()))
list2=list(map(int,input("ENter num").split()))
for i in range(len(list1)):
    if(list1[i]!=list2[i]):
        print(i)
        break
print(list1)
print(list2)

