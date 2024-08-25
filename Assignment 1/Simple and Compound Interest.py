p=int(input("Enter the principal"))
r=float(input("Enter the rate of interest"))
t=int(input("Enter the time"))
pi=p*r*t/100
ci=p*((1+r/100)**t-1)
print(pi)
print(ci)
print("Total amount payable in simple interes= ",p+pi)
print("Total ammount payable in compund interest= ",p+ci)