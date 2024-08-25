l1=int(input("Enter the lenth"))
l2=int(input("Enter the lenth"))
l3=int(input("Enter the lenth"))

if(l1==l2 and l2==l3):
    print("Eqitorial")
elif(l1==l2 or l1==l3 or l2==l3):
    print("semi decular")
else:
    print("decular")