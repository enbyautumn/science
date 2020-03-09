import matplotlib
matplotlib.use('PS')
import matplotlib.pyplot as plt
from numpy.random import rand
import sys 
import json
from termcolor import colored, cprint 
from datetime import datetime

now = datetime.now()
net = NetworkReader.readFrom('/Users/mac/weights.xml') 
data = open("/Users/mac/data.json", "r").read()
data = json.loads(data)

print("Welcome to Dover Weather, one of, if not the highest grade weather forecasting station for Dover you can find")

text = colored("To access today's weather, press 1", 'blue')
text2 = colored("To access the 1-day forcast, press 2", 'blue')
text3 = colored("To access the 2-day forcast, press 3", 'blue')
text4 = colored("To access the 3-day forecast, press 4", 'blue')
print(text)
print(text2)
print(text3)
print(text4)

print("For specific charts, see the below instructions.")

texta = colored("To access a temperature graph, press 5", 'green')
textb = colored("To access a humidity graph, press 6", 'green')
textc = colored("To access a pressure graph, press 7", 'green')
textd = colored("To access previous weather data, press 8", 'green')
print(texta)
print(textb)
print(textc)
print(textd)

number = input ("Enter a number: ")
number = int(number)


# Marker size in units of points^2
volume = (15 * data.volume[:-2] / data.volume[0])**2
close = 0.003 * data.close[:-2] / 0.003 * data.open[:-2]

if number == 1: 
  
  def rounder(t):
    if t.minute >= 30:
        return t.replace(second=0, microsecond=0, minute=0, hour=t.hour+1)
    else:
        return t.replace(second=0, microsecond=0, minute=0)

  hi = rounder(now)
  today = hi, "+0000 UTC"
  date2 = ["dt_iso", today]
  print(date2(["weather"]))

  
x = date2 = ["dt_iso", today]

elif number == 2:
  print("Please wait for our 1-day forcast to be complete")
  print(data(x, ["weather"]))
  
elif number == 3: 
  print("Please wait for our 2-day forcast to be complete")
  print(data(x, ["weather"]))
  
elif number == 4:
  print("Please wait for our 3-day forcast to be complete")
  print(data(x, ["weather"]))
  
elif number == 5:
  ax.scatter(data(x, ["main"]["temp"]))
  
  for x in range(0, 24):
    ax.scatter(data(x+1, ["main"]["temp"]))
                 
  ax.set_xlabel('Days', fontsize=15)
  ax.set_ylabel('Temperature', fontsize=15)
  ax.set_title('Temperature Chart in Degrees Farenhite for the next 24 hours')

  fig, ax = plt.subplots()
  ax.grid(True)
  plt.show()
                              
elif number == 6:
  ax.scatter(data(x, ["main"]["humidity"]))
  
  for x in range(0, 24):
    ax.scatter(data(x+1, ["main"]["humidity"]))
                 
  ax.set_xlabel('Days', fontsize=15)
  ax.set_ylabel('Humidity', fontsize=15)
  ax.set_title('Humidity Chart (in percentage) for the next 24 hours')

  fig, ax = plt.subplots()
  ax.grid(True)
  plt.show()
      
elif number == 7:
  ax.scatter(data(x, ["main"]["pressure"]))
  
  for x in range(0, 24):
    ax.scatter(data(x+1, ["main"]["pressure"]))
                 
  ax.set_xlabel('Days', fontsize=15)
  ax.set_ylabel('Pressure', fontsize=15)
  ax.set_title('Atmospheric Pressure Chart (in hPa units) for the next 24 hours')

  fig, ax = plt.subplots()
  ax.grid(True)
  plt.show()
    
elif number == 8: 
    
  print("would you like instructions on how to enter the date? Yes = 1, No = 0")
  answer = input("1/0:")
  answer = int(answer)
    
  if answer == 1:
    print("Enter the date you would like to view (You will only be able to access dates from 2014 onwards.)")
    print("when you enter the date, you must enter it in the form of year-month-day.")
    print("Also include the hour, in 24-hour time in the form of 00:00:00.")
    print("Finally include '+0000 UTC' at the end.")
    print("For example, if the date was Jan 2 of 2013, at 13:00, enter 2013-01-02 13:00:00 +0000 UTC")
    
    num2 = input("enter the date:")
    num2 = int(num2)
      
  elif answer == 0:
    num2 = input("enter the date:")
    num2 = int(num2)
    
  data = open("/Users/mac/data.json", "r").read()
  data = json.loads(data)
  date = ["dt_iso", num2]
  print(date(["weather"]))
    
    
else:
  print("Sorry, I din't get that. Please re-enter your number")
  print("To access today's weather, press 1")
  ("To access the 1-day forcast, press 2", 'blue')
  ("To access the 2-day forcast, press 3", 'blue')
  ("To access the 3-day forecast, press 4", 'blue')
  
  print("To access a temperature graph, press 5") 
  print("To access a humidity graph, press 6")
  print("To access a pressure graph, press 7")
  print("To access previous weather data, press 8")
  number = input ("Enter a number: ")
  number = int(number)
 




