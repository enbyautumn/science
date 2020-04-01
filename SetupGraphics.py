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

print("Welcome to Dover Weather, one of, if not the best weather forecasting stations for Dover, MA.")
print("ZIP:02030")

text = colored("To access the 1-day forcast, press 1", 'blue')
text2 = colored("To access the 2-day forcast, press 2", 'blue')
text3 = colored("To access the 3-day forecast, press 3", 'blue')
text4 = colroed("To access previous weather data, press 4", 'blue')
print(text)
print(text2)
print(text3)
print(text4)


number = input ("Enter a number: ")
number = int(number)


# Marker size in units of points^2
volume = (15 * data.volume[:-2] / data.volume[0])**2
close = 0.003 * data.close[:-2] / 0.003 * data.open[:-2]
  
def rounder(t):
  if t.minute >= 30:
      return t.replace(second=0, microsecond=0, minute=0, hour=t.hour+1)
  else:
      return t.replace(second=0, microsecond=0, minute=0)

roundIt = rounder(now)
today = roundIt, "+0000 UTC"
date2 = ["dt_iso", today]
print(date2(["weather"]))

x = date2

if number == 1:
  print("Please wait for our 1-day forcast to be complete.")
  print(data(x, ["weather"]))
  
elif number == 2: 
  print("Please wait for our 2-day forcast to be complete.")
  print(data(x, ["weather"]))
  
elif number == 3:
  print("Please wait for our 3-day forcast to be complete.")
  print(data(x, ["weather"]))
    
elif number == 4: 
  
 print("would you like instructions on how to enter the date? Yes = 1, No = 0")
 answer = input("1/0:")
 answer = int(answer)
    
 if answer == 1:
  
   print("Enter the date you would like to view (You will only be able to access dates from 2014 onwards.)")
   print("when you enter the date, you must enter it in the form of year-month-day.")
   print("Include the hour in 24-hour time in the form of 00:00:00.")
   print("Also, include '+0000 UTC' at the end.")
   print("For example, if the date was Jan 2 of 2013, at 13:00, enter 2013-01-02 13:00:00 +0000 UTC")
    
   num2 = input("enter the date:")
   num2 = int(num2)
      
 elif answer == 0:
   num2 = input("Enter the date:")
   num2 = int(num2)
    
 data = open("/Users/mac/data.json", "r").read()
 data = json.loads(data)
 date = ["dt_iso", num2]
 print(date(["weather"]))
    
    
else:
  print("Sorry, I didn't get that. Please re-enter your number")
  
  print(text)
  print(text2)
  print(text3)
  print(text4)
  
  number = input ("Enter a number: ")
  number = int(number)
 




