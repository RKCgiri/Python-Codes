import math
def Union_Inter(list1,list2):
    union=(set(list1) | set(list2))
    inter=(set(list1) & set(list2))
    return union,inter


list1=eval(input("Enter list 1"))
list2=eval(input("Enter list 2"))
result=Union_Inter(list1,list2)
print(result[0],"   " ,result[1])
union=[]
inter=[]
union.extend(list1)
print(union)
for i in list2:
    if i not in union:
        union.append(i)
print(union)

for i in list1:
    if i in list2:
        inter.append(i)
print(inter)
    


