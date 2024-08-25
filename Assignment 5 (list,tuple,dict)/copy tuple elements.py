tuple1 = (11, 22, 33, 44, 55, 66)
tuple2 = tuple1[3:-1]
print(tuple2)
list1 = [11, 22, 33, 44, 55, 66]
slice_index1 = int(input("Please enter slice index 1:"))
slice_index2 = int(input("Please enter slice index 2:"))
list2 = list1[slice_index1:slice_index2]
print(list2)