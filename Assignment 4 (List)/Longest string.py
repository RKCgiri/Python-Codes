l = eval(input("Enter list of strings: "))
''' eval function make it type casting automatically and also we can
find any expression using this function like:
x=eval("3**3")//result is 27 '''
largeIdx = 0
largeLen = 0

for i in range(len(l)):
    length = len(l[i])
    if length > largeLen:
        largeLen = length
        largeIdx = i

print("Longest String:", l[largeIdx],type(l))

res = max(l, key = len)
 
# printing result
print("Maximum length string is : " + res)