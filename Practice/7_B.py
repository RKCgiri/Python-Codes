l=list(map(int,input("Enter the list").split()))
print(l)
u=[]
for i in range(len(l)):
    if l[i] not in u:
        u.append(l[i])
print(u)