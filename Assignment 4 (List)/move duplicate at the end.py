l=eval(input("Enter the list"))
dedup = []
dup = []
for i in l:
    if i in dedup:
        dup.append(i)
    else:
        dedup.append(i)

l = dedup + dup

print("Modified List:")
print(l)