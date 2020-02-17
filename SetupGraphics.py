import matplotlib
matplotlib.use('PS')
import matplotlib.pyplot as plt
from numpy.random import rand

net = NetworkReader.readFrom('/Users/mac/weights.xml') 
data = open("/Users/mac/data.json", "r").read()
data = json.loads(data)

x = random.randrange(0, 1000)


print("For a complete five day forecast, please wait until we've actually finished this.")
print("For specific charts, see the below instructions.")
print("To access a temperature graph, press 1")
print("To access a humidity graph, press 2")
number = input ("Enter a number: ")
number = int(number)

# Marker size in units of points^2
volume = (15 * data.volume[:-2] / data.volume[0])**2
close = 0.003 * data.close[:-2] / 0.003 * data.open[:-2]

while true:
  if number == 1:
    ax.scatter(data(x, ["main"]["temp"]))
    ax.scatter(data(x+1, ["main"]["temp"]))
    ax.scatter(data(x+2, ["main"]["temp"]))
    ax.scatter(data(x+3, ["main"]["temp"]))
    ax.scatter(data(x+4, ["main"]["temp"]))                
    ax.scatter(data(x+5, ["main"]["temp"]))
    ax.scatter(data(x+6, ["main"]["temp"]))
                 
    ax.set_xlabel('Days', fontsize=15)
    ax.set_ylabel('Temperature', fontsize=15)
    ax.set_title('Temperature Chart in Degrees Farenhite')

    fig, ax = plt.subplots()
    ax.grid(True)
    plt.show()
                              
  elif number == 2:
    ax.scatter(data(x, ["main"]["humidity"]))
    ax.scatter(data(x+1, ["main"]["humidity"]))
    ax.scatter(data(x+2, ["main"]["humidity"]))
    ax.scatter(data(x+3, ["main"]["humidity"]))
    ax.scatter(data(x+4, ["main"]["humidity"]))                
    ax.scatter(data(x+5, ["main"]["humidity"]))
    ax.scatter(data(x+6, ["main"]["humidity"]))
                 
    ax.set_xlabel('Days', fontsize=15)
    ax.set_ylabel('Humidity', fontsize=15)
    ax.set_title('Humidity Chart')

    fig, ax = plt.subplots()
    ax.grid(True)
    plt.show()
      
  else:
    print("Sorry, I din't get that. Please re-enter your number")
    print("Temperature graph = 1")                       
    number = input ("Enter a number: ")
    number = int(number)                      



