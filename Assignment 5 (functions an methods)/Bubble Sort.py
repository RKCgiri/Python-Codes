def swap(a,b):
   a,b = b,a

def bubbleSort(arr):
    n=len(arr)
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:               
                arr[j],arr[j+1]=arr[j+1],arr[j]
        for k in range(0,n):
            print(arr[k],end=" ")
        print("\n")
arr=list(map(int,input("Enter the list").split()))
print("list elemts are")
for i in range(0,len(arr)):
    print(arr[i],end=" ")
print("\n")
bubbleSort(arr)
print(" \n After sorting list elements are")
for i in arr:
    print(i,end=" ")
    

    