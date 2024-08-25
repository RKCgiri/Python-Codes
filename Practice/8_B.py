sum=0
avg=0
cnt=0
while True:
    n=input("Enter the number")
    if n=='q':
        break
    sum+=int(n)
    cnt+=1
print("Avarage is ",sum/cnt)