def bubble(list):
    for i in range(len(list)-1):
        for j in range(len(list)-1-i):
            if list[j]>list[j+1]:
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
list=list(map(int,input("Enter ").split()))
print(list)
bubble(list)
print(list)