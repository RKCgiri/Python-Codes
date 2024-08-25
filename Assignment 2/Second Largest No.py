n=int(input("Enter no of inputs "))
if n>1:
    largest=int(input())
    second=int(input())
    if second>largest:
        t=second
        second=largest  
        largest=t   
     
    for i in range (n-2):
        a=int(input())
        if largest<a:
            second=largest
            largest=a
            
    print(second)
else:
    print("Enter grater than 1")
     