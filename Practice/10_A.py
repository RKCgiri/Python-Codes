n=int(input("Enter the range"))
m=int(input("Ente rthe number "))
for i in range(n):
    if(i%m==0):
        print(f"The {i} is divisable by {m}")
        if(i%2==0):
            print("and even")
        else:
            print("and odd")
