import numpy as np
from numpy import random
import matplotlib.pyplot as plt

a=random.rand(10)
print(a)
avg=a*100
print(avg)
sec=['A','B','C','D','E','F','J','L','M','N']

# # # plt.title("CGPA")
# # # plt.plot(sec,avg,label=sec,ms=10,color='y',marker='*')
# # # plt.legend(title="Class cgpa")
# # # plt.show()

# # # plt.title("CGPA")
# # # plt.bar(sec,avg,label=sec,color='y',width=.3)
# # # plt.legend(title="Class cgpa")
# # # plt.show()

my=[0.3,0,0,0,0,0,0,0,0,0]
plt.title("CGPA")
plt.pie(avg,labels=sec,explode=my,shadow=True)
plt.legend(title="Class cgpa")
plt.show()
