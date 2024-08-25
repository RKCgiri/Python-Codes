def check(str):
    b='01'
    for i in str:
        if i not in b:
            return False
    return True
print(check("radhe krishna"))
print(check("11110001010101"))
print(check('11110001010121'))