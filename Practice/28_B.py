with open("28_B.txt",'r') as f :
    title=f.readline()
    data1=f.readline().split(',')
    data2=f.readline().split(',')
print(title)
print(data1)
print(data2)
print("customer",data1[0])
print("custoommer 1 july",data1[6],"customer 1 nov ",data1[11])
print("custoommer 2 july",data2[6],"customer 2 nov ",data2[11])
