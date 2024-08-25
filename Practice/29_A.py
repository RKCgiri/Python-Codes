units=int(input("Enter the unit value = "))
bill=0
if(units>=0 and units<=200):
    bill=units*.5
elif(units>=201 and units<=400):
    bill=100+units*.65
elif(units>=401 and units<=600):
    bill=200+units*.8
else:
    bill=425+units*1.25
print(bill) 