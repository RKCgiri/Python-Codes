def SuperASCII(string):
    freq=[0 for i in range(26)]
    for i in range(len(string)):
         index=ord(string[i])-97+1
         freq[index-1]+=1
    for i in range(len(string)):
        index=ord(string[i])-97+1
        if(index!=freq[index-1]):
            return False
    return True

if __name__ == '__main__':
    string = input("Enter the string: ")
    result = SuperASCII(string)
    print(result)
    
    
    
import string 
 
dicti = {}
a = []
for i in string.ascii_lowercase:
    a.append(i)
for i in string.ascii_lowercase:
    for j in range (1,27):
        if (a.index(i)+1) == j: #if the number is equal to the position of the alphabet
            dicti[i] = j        #in the list, then the number will be ascii code for the
            break               #aplhabet in the dictionary
 
s = 'bba'
t = True #t is initialized as true
 
for i in s:
    if s.count(i) != dicti[i]: #if any of the alphabet count is not equal to its
        t = False              #corresponding ascii code in the dictionary, t will be false
 
if t:
    print("Yes")            #printing yes if t remains true after checking all alphabets 
else:
    print("No")