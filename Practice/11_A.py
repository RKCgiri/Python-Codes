n=int(input("Enter range"))
for i in range(n):
    if str(i)==str(i)[::-1]:
        if(i>2):
            f=0
            for j in range(2,i-1):
                if(i%j==0):
                    f=-1
            if(f!=-1):
                print(f"{i} is a pallindromic prime number ")
        