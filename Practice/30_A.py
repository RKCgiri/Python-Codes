val1=int(input("Enter value 1"))
val2=int(input("Enter value 2"))
op=input("+-*^%/")
res=0

if(op=='+'):
    res=val1+val2
elif(op=='-'):
    res=val1-val2
elif(op=='*'):
    res=val1*val2
elif(op=='/'):
    res=val1/val2
elif(op=='^'):
    res=val1**val2
elif(op=='%'):
    res=val1%val2
else:
    print("Wrong choise")
print(res)
