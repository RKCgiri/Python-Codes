def LowerUpper(s):
    uc=0
    lc=0
    for i in range(len(s)):
        if (s[i]>='A' and s[i]<='Z'):
             uc+=1
        if(s[i]>='a' and s[i]<='z'):
            lc+=1
    print(f"No of upper case letter is {uc} and lower case letter is {lc}")
s=input("Enter the string")
print(s)
uc=0
lc=0
LowerUpper(s)
for i in s:
    if(i.islower()):
        lc+=1
    if(i.isupper()):
        uc+=1
print(f"No of upper case letter is {uc} and lower case letter is {lc}")