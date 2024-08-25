n=int(input("Enter the number"))
m=n
rev=0
while n!=0:
    rim=n%10
    rev=rev*10+rim
    n=n//10
print(rev)
if(n%2):
    print("Even Number ")
else:
    print("Odd Number ")