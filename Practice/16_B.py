str=input("Enter the string")
l=0
u=0

for i in range(len(str)):
    if(str[i]>='A' and str[i]<='Z'):
        u+=1
    else:
        l+=1
print(l,u)
l,u=0,0
for i in str:
    if(i.islower()):
        l+=1
    elif(i.isupper()):
        u+=1
print(l,u)