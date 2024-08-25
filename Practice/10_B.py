import matplotlib.pyplot as plt
vote=[180,200,20]
party=['ABC','XYZ','MNC']
plt.title("Vote ")
plt.plot(party,vote,label="party",marker="o",ms=10,color='r')
plt.legend(title="Vote bank ")
plt.show()
plt.title("Vote ")
plt.bar(party,vote,label="party",width=0.5,color='r')
plt.legend(title="Vote bank ")
plt.show()

list=[0.3,0,0]
plt.pie(vote,labels=party,explode=list)
plt.legend(title="Vote Bank")
plt.show()