keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

res_dict = dict(zip(keys, values))
print(res_dict)

#solution 2


keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# empty dictionary
res_dict = dict()

for i in range(len(keys)):
    res_dict.update({keys[i]: values[i]})
print(res_dict)



test_keys = ["Rash", "Kil", "Varsha"]
test_values = [1, 4, 5]
 
# Printing original keys-value lists
print("Original key list is : " + str(test_keys))
print("Original value list is : " + str(test_values))
 
# using dictionary comprehension
# to convert lists to dictionary
res = {test_keys[i]: test_values[i] for i in range(len(test_keys))}
 
# Printing resultant dictionary
print("Resultant dictionary is : " + str(res))


import sys
d = {}

if len(keys) != len(values):
    print("Both lists must need to be of same length to acheive the solution")
    sys.exit()

for i in range(len(keys)):
    d[keys[i]] = values[i]
    
print(d)