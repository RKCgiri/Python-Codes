list=list(map(int,input("enter the list ").split()))
dup = [ ]
n = 1
while n < len(list):
      for i in list :
            if list.count( i ) != 1 :
                  list.remove( i )
                  dup.append(i)
      n += 1

list.sort()
print("New list :- ",list + dup)

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