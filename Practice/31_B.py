l=[]
for i in range(1,27):
    c=""
    c=chr(i+96)*i
    #for j in range(0,i):
       # c=c+chr(i+96)
    l.append(c)
print(l)    
l1=[]
l2=[]
for i in range(26):
    for j in range(i):
        l1.append(chr(i+65))
    l2.append(l1)
print(l2)
