import matplotlib.pyplot as plt

total=int(input("Enter total no seates "))
x=120
y=210
z=total-(120+210)
vote=[x,y,z]
party=['x','y','z']
plt.title("WB Vote")
plt.plot(party,vote,label=party,marker='o',color='g',ms=10)
plt.legend(title="WB")
plt.show()

plt.title("WB Vote")
plt.bar(party,vote,label=party,width=.21,color='g')
plt.legend(title="WB")
plt.show()

my=[0.3,0,0]
plt.title("WB Vote")
plt.pie(vote,labels=party,explode=my,shadow=True)
plt.legend(title="WB")
plt.show()


