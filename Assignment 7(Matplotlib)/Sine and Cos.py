import matplotlib.pyplot as plt
import numpy as np

x=np.arange(-4*np.pi,4*np.pi,0.1)
y=np.sin(x)
z=np.cos(x)
plt.xlabel("X values from -4pi to 4pi")
plt.ylabel("Sin(x)")
plt.title("The sine wave")
plt.legend(loc='upper right')
plt.plot(x,y,label='sine(x)')
plt.plot(x,z,label='Cos(x)')
plt.legend()  
# To create legend label is required
plt.show()