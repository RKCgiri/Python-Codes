num=list(map(int,input("Enter the numenetors").split()))
denum=list(map(int,input("Enter the denomenetors").split()))
ans=[]
#max=0
maxind=0
for i in range(len(num)):
    ans.append(num[i]/denum[i])
print(ans)
print(max(ans))
'''for i in range(len(ans)):
    if ans[i]>max:
        max=ans[i]
        maxind=i
print(max,maxind)
   ''' 