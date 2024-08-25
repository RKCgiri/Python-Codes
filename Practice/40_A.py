def fact(n,k):
    m=k
    for i in range(n,0,-1):
        if(n % i==0):
            k-=1
            if(k==0):
                print(f"The {m} th factor of {n} is {i}")
n=int(input("enter the num"))
k=int(input("enter the k th"))
fact(n,k)