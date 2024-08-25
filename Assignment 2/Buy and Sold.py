n=int(input("Enter number of items to buy"))
cost=0
if n>=100:
    cost=n*70
elif n>=10:
    cost=n*100
else:
    cost=n*120
print("The no of product you buy ",n,"The cost is ",cost)