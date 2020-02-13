import matplotlib
matplotlib.use('PS')

import matplotlib.pyplot as plt
from numpy.random import rand


fig, ax = plt.subplots()
   
ax.scatter(2, 5)
ax.grid(True)

ax.set_xlabel('Days', fontsize=15)
ax.set_ylabel('Temperature', fontsize=15)
ax.set_title('Temperature Chart in Degrees Farenhite')

ax.grid(True)
plt.show()


