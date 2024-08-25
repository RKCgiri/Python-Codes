# oreder of n^2
s=input("Enter the string = ")
newString=""
for i in s:
    if i not in newString:
        newString=newString+i
print(newString)

# order of one by using dictionary

dict={}
ans=""
for i in range(len(s)):
    if s[i] not in dict:
        ans=ans+s[i]
        dict[s[i]]=1
print(ans)