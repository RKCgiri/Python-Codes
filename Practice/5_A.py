def occurance(str,substr):
    list=[]
    cnt=0
    temp=str.lower()
    i=0
    while i<len(str):
        j=temp.find(substr.lower(),i)
        if(j==-1):
            break
        cnt+=1
        i=j+len(substr)
        list.append(j)
    return list,cnt

str="Radhe Krishna Radhe Radhe"
substr="radhe"
print(occurance(str,substr))

def fun(str):
    str=str.lower()
    cnt=0
    for i in range(len(str)):
        if( str[i:i+5]=='india'):
            cnt+=1
            print(f"India is found at {i}")
    print(f"Total conunt {cnt} ")
str="India is a varat .rada krishna orn in india"
fun(str)

