n=int(input("Enter the number of key in dictionary"))
test_dict=dict(input("Enter the key and value with , ").split(',') for a in range(n))
print("The original dictionary is : " + str(test_dict))

Keymax = min(zip(test_dict.values(), test_dict.keys()))
min_value_key = min(test_dict, key=test_dict.get)
print(Keymax)
print(min_value_key)
print("Keys with minimum values are : " + str(Keymax))