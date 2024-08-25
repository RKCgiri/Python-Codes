print("Radhe Krishna")
n=int(input("Enter the year "))
print(n)
d=n*365
h=d*24
m=h*60
s=m*60
print(d,h,m,s)
y=int(input("Enter the year "))
if y%4==0:
    if y%100==0:
        if y%400==0:
            print("Leap year")
        else:
            print("Not")
    else:
        print("Leap Year")
else:
    print("Not")