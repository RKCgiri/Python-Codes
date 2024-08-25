def Palindrome(string):
    for i in range(len(string)//2):
        if(string[i]!=string[len(string)-1-i]):
            return False
    return True
string=input("Enter a string ")
print(Palindrome(string))



