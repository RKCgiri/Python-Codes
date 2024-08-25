import matplotlib.pyplot as plt
import numpy as np

from numpy import random
marks=np.random.randint(0,100,6)
subjects=['math','physics','chemistry','biology','computer science','Sanskrit']
print(marks)
plt.bar(marks,subjects,color='red',width=0.5)
plt.legend(title="Subjects")
plt.show()

# pie plot
my_expo=[0.3,0,0,0,0,0]
plt.pie(marks,labels=subjects,explode=my_expo,shadow=True)
plt.legend(title="Subjects")
plt.show()


