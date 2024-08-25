def fun(str):
    vioel='aeiou'
    if(len(set(str.lower()) & set(vioel))>=5):
        return True
    return False
str=input("Enter string ")
print(str)   
new=fun(str)  
print(new)    