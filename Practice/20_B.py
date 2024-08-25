# def Palindrome(string):
#     for i in range(len(string)//2):
#         if(string[i]!=string[len(string)-1-i]):
#             return False
#     return True
def Palindrome(n):
    if(str(i)==str(i)[::-1]):
        return True
    return False
l=list(map(str,input("enter").split()))
print(l)
for i in l:
    if(Palindrome(i)==True):
        print("True",end=" ")
    else:
        print("False",end=" ")