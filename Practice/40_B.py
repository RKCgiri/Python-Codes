with open("40_B_exit.txt",'r') as f:
    data=f.readlines()
print(data)
with open("40_B_deliver.txt",'w') as f:
    lineno=1
    for line in data:
        f.write(f"{lineno}==>{line}")
        lineno+=1
    
