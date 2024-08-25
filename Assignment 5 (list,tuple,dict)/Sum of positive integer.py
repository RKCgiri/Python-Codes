def sum_positive_values(*args):
    #The syntax is to use the symbol * to take in a variable number of arguments
    result = 0
    for num in args:
        if num > 0:
            result += num
    return result

# Example usage:
result = sum_positive_values(1,2,3,9,-9,-5,-3)
print(result)