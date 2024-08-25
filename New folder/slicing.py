def sclice():
    str=input()
    # str=str[1:-1:]
    # s=str[::-1]
    str2=input()
    # p=str[0:len(str):len(str)//2]
    # s=str2[0:len(str2):len(str2)//2]
    # s=s+p
    s=str[0:len(str)//2:]+str2+str[len(str)//2:len(str):]
    return s
print(sclice())