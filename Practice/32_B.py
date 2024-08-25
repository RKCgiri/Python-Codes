def is_ugly(num):
        if num == 0:
            return False
        for i in [2, 3, 5]:
            while num % i == 0:
                num /= i
        return num == 1
def isUgly(n):
 
    # Base Cases
    if (n == 1):
        return 1
    if (n <= 0):
        return 0
 
    # Condition to check if the
    # number is divided by 2, 3, or 5
    if (n % 2 == 0):
        return (isUgly(n // 2))
         
    if (n % 3 == 0):
        return (isUgly(n // 3))
     
    if (n % 5 == 0):
        return (isUgly(n // 5))
 
    # Otherwise return false
    return 0
 
print(is_ugly(13))
print(is_ugly(12))
print(isUgly(13))
print(isUgly(12))
