import matplotlib
matplotlib.use('PS')
import matplotlib.pyplot as plt
from numpy.random import rand
import sys 
import json
from termcolor import colored, cprint 
from datetime import date
import time


t = time.localtime()
today = date.today()
net = NetworkReader.readFrom('/Users/mac/weights.xml') 
data = open("/Users/mac/data.json", "r").read()
data = json.loads(data)

x = random.randrange(0, 1000)

print("Welcome to (Insert name here), one of, if not the highest grade weather forecasting station you can find")

text = colored("To access today's weather, press 1", 'blue')
text2 = colored("To access the complete 5-day forcast, press 2", 'blue')
text3 = colored("To access the complete 7-day forcast, press 3", 'blue')
print(text)
print(text2)
print(text3)

print("For specific charts, see the below instructions.")

texta = colored("To access a temperature graph, press 4", 'green')
textb = colored("To access a humidity graph, press 5", 'green')
textc = colored("To access a pressure graph, press 6", 'green')
textd = colored("To access previous weather data, press 7", 'green')
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
  print("Today's date:", today)
  print(current_time)
  current_time = time.strftime("%H%M%S", t)
  round(float(current_time), -4)
  
  current_time = time.strftime("%H:%M:%S", t)

  today2 = today, current_time, "+0000 UTC"
  date2 = ["dt_iso", today2]
  print(date2(["weather"]))

elif number == 2: 
  print("Please wait for our 5-day forcast to be complete")
  print(data(x, ["weather"]))
  
elif number == 3:
  print("Please wait for our 5-day forcast to be complete")
  print(data(x, ["weather"]))
  
elif number == 4:
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
                              
elif number == 5:
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
      
elif number == 6:
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
    
elif number == 7: 
    
  print("would you like instructions on how to enter the date? Yes = 1, No = 0")
  answer = input("1/0")
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
  print("To access the complete 5-day forcast, press 2")
  print("To access the complete 7-day forcast, press 3")
  
  print("To access a temperature graph, press 4") 
  print("To access a humidity graph, press 5")
  print("To access a pressure graph, press 6")
  print("To access previous weather data, press 7")
  number = input ("Enter a number: ")
  number = int(number)
 




