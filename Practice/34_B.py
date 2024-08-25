import matplotlib.pyplot as plt
import numpy as np
from numpy import random

x=np.random.randint(20,100,30)
y=np.random.randint(0,10,30)
color=np.random.randint(0,100,30)
plt.scatter(x,y,c=color,cmap='viridis')
plt.colorbar()
plt.show()