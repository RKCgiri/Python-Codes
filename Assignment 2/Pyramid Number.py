n=int(input("Enter the number "))
for i in range(1,n+1,1):
    for k in range(n-i,0,-1):
        print(" ",end=" ")
    for j in range(0,i,1):
        print(i,end="   ")
    print("\n")
for i in range(1,n,1):
    for k in range(0,i,1):
        print("  ",end="")
    for j in range(n,i,-1):
        print(n-i,end="   ")
    print("\n")