n=int(input("Enter the number of key in dictionary"))
sample=dict(input("Enter the key and value with , ").split(',') for a in range(n))
print(sample)
k=input("enter the key name to change")
update=input("Enter the upadted key")
if k in sample:
    sample[update] = sample.pop(k)
    print("Updated dictionary:", sample)
else:
    print(f"The key '{k}' does not exist in the dictionary.")