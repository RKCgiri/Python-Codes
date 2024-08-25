def find(list):
    my_list=[]
    for i in range(len(list)): # increase this range
       sum=0
       l=str(list[i])
       k=len(l)
       for j in range(0,k):
          sum=sum+pow(int(l[j]),3)
  
       if(sum==list[i]):
          print("This is an matching number: ",list[i])  
          my_list.append(list[i])
    return my_list
    
list=list(map(int,input("Enter the numbers of the list").split()))
my_list=find(list)
print(my_list)
print("Highest number : ",max(list))
print("Lowest  number : ",min(list))