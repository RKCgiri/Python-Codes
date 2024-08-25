import math
for i in range(0,6):
    for j in range(i,-1,-1):
        print(int(math.pow(2,j)),end=" ")
    print()