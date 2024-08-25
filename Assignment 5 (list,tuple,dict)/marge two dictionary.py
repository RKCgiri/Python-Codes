# Define a function 'merge_dictionaries' that takes a variable number of dictionaries ('*dicts') as arguments.
# It merges the dictionaries into a new dictionary and returns the result.
def merge_dictionaries(*dicts):
    # Create an empty dictionary 'result' to store the merged key-value pairs.
    result = dict()

    # Iterate through the input dictionaries ('dicts') using a for loop.
    for d in dicts:
        # Update the 'result' dictionary by adding key-value pairs from the current dictionary 'd'.
        result.update(d)

    # Return the merged 'result' dictionary.
    return result

# Create two dictionaries 'students1' and 'students2' with key-value pairs.
students1 = {
    'Theodore': 10,
    'Mathew': 11,
}

students2 = {
    'Roxanne': 9
}

# Print a message indicating the start of the code section.
print("Original dictionaries:")

# Print the original dictionaries 'students1' and 'students2'.
print(students1)
print(students2)

# Print a message indicating the start of the merged dictionaries section.
print("\nMerge dictionaries:")

# Call the 'merge_dictionaries' function with 'students1' and 'students2' as arguments to merge the dictionaries.
# Print the result, which is the merged dictionary.
print(merge_dictionaries(students1, students2)) 




# Create the first dictionary 'd1' with key-value pairs.
d1 = {'a': 100, 'b': 200}

# Create the second dictionary 'd2' with key-value pairs.
d2 = {'x': 300, 'y': 200}

# Create a new dictionary 'd' and initialize it as a copy of 'd1'.
d = d1.copy()

# Update the dictionary 'd' by adding key-value pairs from 'd2'.
d.update(d2)

# Print the dictionary 'd' after combining the key-value pairs from 'd1' and 'd2.
print(d) 


dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict3 = {**dict1, **dict2}# we can marge two dict using ** and |(union) operator
#dict3=dict1|dict2
print(dict3)