n=int(input("Enter the no cookies"))
box=n//24
contener=box//75
box=box%75
cookies=n%24
print(contener, box, cookies)