while True:
    k=input("Enter the number ")
    if k=='q':
        break
    m=int(k)
    n=m
    rev=0
    while n!=0:
        rim=n%10
        rev=rev*10+rim
        n=n//10
    if rev==m:
        print("Pallindrome")
    else:
        print("Not")