'''def search_number(number, number_list):
    for index, value in enumerate(number_list):
        if value == number:
            return f"Number {number} found at index {index}"
    
    return f"Number {number} not found in the list"

# Example usage:
my_list = [2, 4, 6, 8, 10, 12, 14]
number_to_search = 8
result = search_number(number_to_search, my_list)
print(result)'''


#The enumerate function in Python is used to iterate over a sequence (such as a list, tuple, or string)
# while keeping track of the index of the current item. 
# It returns pairs of index and element in the form of (index, element) for each element in the sequence.

def find(l,key):
    index=0.1
    for i,element in enumerate(l):
        if key==element:
            index=i
    return index

l=list(map(int,input("Enter the list").split()))
print(find(l,5))
