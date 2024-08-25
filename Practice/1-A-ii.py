s1=input("Enter first string = ")
s2=input("Enter second string = ")
print(s1[0]+s1[int(len(s1)/2)]+s1[len(s1)-1])
print(s2[0]+s2[int(len(s2)/2)]+s2[len(s2)-1])
# using scling
print(s1[0:(len(s1)):len(s1)//2]) 