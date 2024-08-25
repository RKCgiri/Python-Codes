import numpy as np
from numpy import random
import matplotlib.pyplot as plt

num1=random.randint(0,100,6)
num2=random.randint(0,100,6)
sub=['m','p','c','b','h','s']
plt.title("Student 1")
plt.xlabel("uum")
plt.ylabel("sub")
plt.plot(sub,num1,label=sub,color='r',marker='o',ms=10)
plt.legend()
plt.show()

plt.title("Student 2")
plt.xlabel("uum")
plt.ylabel("sub")
plt.plot(sub,num2,color='r',marker='o',ms=10)
plt.show()


# bar

plt.bar(sub,num1,label="sub1",width=0.1,color='r')
plt.legend()
plt.show()
plt.bar(sub,num2,label="sub2",width=0.1,color='g')
plt.legend()
plt.show()

# pie plot
my_expo=[0.3,0,0,0,0,0]
plt.pie(num1,labels=sub,explode=my_expo,shadow=True)
plt.legend(title="Subjects")
plt.show()

my_expo=[0.3,0,0,0,0,0]
plt.pie(num2,labels=sub,explode=my_expo,shadow=True)
plt.legend(title="Subjects")
plt.show()

