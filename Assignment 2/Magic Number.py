n=int(input("Enter a number"))
m=n
s=0
while not ( m>=0 and m<=9):
   while m!=0:
      rim=m%10
      s+=rim
      m=m//10
   if(s>=10):
      m=s
      s=0
   else:
      m=s
      break
if m==1:
   print("Magic Number")
else:
   print("Not")