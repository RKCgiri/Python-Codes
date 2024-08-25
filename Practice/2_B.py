import matplotlib.pyplot as plt
import numpy as np
from numpy import random

n=np.random.randint(0,100,10)
print(n)
m=n**2
print(m)
plt.plot(n,color='red',label='line 1')
plt.legend()
plt.show()
plt.plot(m,label='line 2')
plt.legend()
plt.show()