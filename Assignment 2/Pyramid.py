n=int(input("Enter the no"))
for i in range(n+1,1,-1):
    for j in range(0,n-i+1):
        print(" ",end="")
    for k in range(i,1,-1):
        print("* ",end="")
    print("\n")