import matplotlib
matplotlib.use('PS')
import matplotlib.pyplot as plt
from numpy.random import rand

net = NetworkReader.readFrom('/Users/mac/weights.xml') 
data = open("/Users/mac/data.json", "r").read()
data = json.loads(data)

x = random.randrange(0, 1000)

ax.scatter(data(x, ["main"]["temp"]))
ax.scatter(data(x+1, ["main"]["temp"]))
ax.scatter(data(x+2, ["main"]["temp']))
ax.scatter(data(x+3, ["main"]["temp']))
ax.scatter(data(x+4, ["main"]["temp"]))                
ax.scatter(data(x+5, ["main"]["temp"]))
ax.scatter(data(x+6, ["main"]["temp"]))
                 
ax.set_xlabel('Days', fontsize=15)
ax.set_ylabel('Temperature', fontsize=15)
ax.set_title('Temperature Chart in Degrees Farenhite')

fig, ax = plt.subplots()
ax.grid(True)
plt.show()


