'''
employees = {}
max_length = 3
while len(employees) < max_length:
    name = input("Enter employee's name: ")
    salary = input("Enter employee's salary: ")
    #  check if key not in dict
    
    if name not in employees:
        employees[name] = salary
print(employees)
'''

employees = dict(
    input('Enter key and value separated by space: ').split(',')
    for e in range(3))


# 👇️ {'id': '1', 'name': 'Alice'}
print(employees)



sample_dict = {'a': 100, 'b': 200, 'c': 300}
if 200 in sample_dict.values():
    print('200 present in a dict')