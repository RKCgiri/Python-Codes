import numpy as np
from numpy import random

import matplotlib.pyplot as plt
billPerMount=np.random.randint(0,100,12)
# billPerMount=np.arange(0,100,12)   # np.arrange(lower,heigher,size)
print(billPerMount)
x=['Jan','Feb','Mar','April','May','June','July','Aug','Sept','Oct','Nov','Dec']
# plt.plot(billPerMount,marker='*')
# plt.plot(billPerMount,'o:r')
plt.title("Mounthly Bills")
plt.xlabel("Avarage units ")
plt.ylabel("Mounths")
plt.plot(x,billPerMount,label=x,marker='o',ms=10,mec='r',linestyle='dashed',color='g',linewidth=2)
plt.legend(title="Data per year",loc='lower right')
plt.show()

plt.bar(billPerMount,x,label=x,width=0.5)
plt.legend()
plt.show()
