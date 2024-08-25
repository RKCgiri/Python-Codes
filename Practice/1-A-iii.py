s1=input("Enter first string = ")
s2=input("Enter second string = ")
mid=len(s1)//2
s1=s1[:mid]+s2+s1[mid:]
print(s1)