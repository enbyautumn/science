import matplotlib
matplotlib.use('PS')
import matplotlib.pyplot as plt
from numpy.random import rand
import sys 
from termcolor import colored, cprint 

net = NetworkReader.readFrom('/Users/mac/weights.xml') 
data = open("/Users/mac/data.json", "r").read()
data = json.loads(data)

x = random.randrange(0, 1000)

print("Welcome to (Insert name here), one of, if not the highest grade weather forecasting station you can find")
print("Currently, we can only provide graphs for you to view as our 5-7 day forecast is still under cunstruction")
print("For the complete 5-7 day forecast, please wait until we've actually finished this.")


text = colored("For specific charts, see the below instructions.", 'red')
print(text) 

texta = colored("To access a temperature graph, press 2", 'green')
textb = colored("To access a humidity graph, press 3", 'green')
textc = colored("To access a pressure graph, press 4", 'green')
print(texta)
print(textb)
print(textc)

number = input ("Enter a number: ")
number = int(number)

while true:
  
  # Marker size in units of points^2
  volume = (15 * data.volume[:-2] / data.volume[0])**2
  close = 0.003 * data.close[:-2] / 0.003 * data.open[:-2]

  if nuber == 1: 
    print("Please wait for our 5-day forcast to be coplete")
    
    
  if number == 2:
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
                              
  elif number == 3:
    ax.scatter(data(x, ["main"]["humidity"]))
    ax.scatter(data(x+1, ["main"]["humidity"]))
    ax.scatter(data(x+2, ["main"]["humidity"]))
    ax.scatter(data(x+3, ["main"]["humidity"]))
    ax.scatter(data(x+4, ["main"]["humidity"]))                
    ax.scatter(data(x+5, ["main"]["humidity"]))
    ax.scatter(data(x+6, ["main"]["humidity"]))
                 
    ax.set_xlabel('Days', fontsize=15)
    ax.set_ylabel('Humidity', fontsize=15)
    ax.set_title('Humidity Chart (in percentage)')

    fig, ax = plt.subplots()
    ax.grid(True)
    plt.show()
      
  elif number == 4:
    ax.scatter(data(x, ["main"]["pressure"]))
    ax.scatter(data(x+1, ["main"]["pressure"]))
    ax.scatter(data(x+2, ["main"]["pressure"]))
    ax.scatter(data(x+3, ["main"]["pressure"]))
    ax.scatter(data(x+4, ["main"]["pressure"]))                
    ax.scatter(data(x+5, ["main"]["pressure"]))
    ax.scatter(data(x+6, ["main"]["pressure"]))
                 
    ax.set_xlabel('Days', fontsize=15)
    ax.set_ylabel('Pressure', fontsize=15)
    ax.set_title('Atmospheric Pressure Chart (in hPa units)')

    fig, ax = plt.subplots()
    ax.grid(True)
    plt.show()
    
    
  else:
    print("Sorry, I din't get that. Please re-enter your number")
    print("To access a temperature graph, press 2") 
    print("To access a humidity graph, press 3")
    print("TO access a pressure graph, press 4")
    number = input ("Enter a number: ")
    number = int(number)
 
print(str(weather_description))



