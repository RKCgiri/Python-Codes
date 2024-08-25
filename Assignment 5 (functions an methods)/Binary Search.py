def binarySearch(arr,key):
    low=0
    index=-1
    high=len(arr)-1
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]==key):
            index= mid
            break
        elif(arr[mid]>key):
            high=mid-1
        else:
            low=mid+1

    return index






arr=list(map(int,input("Enter a sorted list").split()))
print("list elemts are")
for i in range(0,len(arr)):
    print(arr[i],end=" ")
print("\n")
key=int(input("Enter the key to search"))
index=binarySearch(arr,key)
if index!=-1:
   print("The key",key,"is present at = ",index)
else:
    print("The element is not found")
