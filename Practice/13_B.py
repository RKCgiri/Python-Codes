n=int(input("Enter number grater than 21"))
for i in range(11,n+1):
    if(i%3==0 and i%7==0):
        print("Tipsy Topsy")
    elif(i%7==0):
        print("Topsy")
    elif(i%3==0):
        print("Tipsy")
    else:
        print(i)