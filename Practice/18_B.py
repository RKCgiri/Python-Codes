str=input("ENTER string")
num=False
letter=False
for i in str:
    if(i.isdigit()):
        num=True
    if i in "abcdefghijklmnopqrstuvwxyz":
        letter=True
    # if(i.isalpha()):
    #     letter=True
    if(num and letter):
        print("Yes")
        break