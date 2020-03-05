# get current weather data
def k2c(k): 
    return k-273.15

# Python program to find current 
# weather details of any city 
# using openweathermap api 

# import required modules 
import requests, json 

# Enter your API key here 
api_key = "9a6f64de069cb85d600ee405159a85f3"

# base_url variable to store url 
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Give city name 
#city_name = input("Dover") 

# complete_url variable to store 
# complete url address 
complete_url = base_url + "appid=" + api_key + "&q=" + 'Dover' 

# get method of requests module 
# return response object 
response = requests.get(complete_url) 

# json method of response object 
# convert json format data into 
# python format data 
x = response.json() 

# Now x contains list of nested dictionaries 
# Check the value of "cod" key is equal to 
# "404", means city is found otherwise, 
# city is not found 
if x["cod"] != "404": 

	# store the value of "main" 
	# key in variable y 
	y = x["main"] 

	# store the value corresponding 
	# to the "temp" key of y 
	current_temperature = (y["temp"])

	# store the value corresponding 
	# to the "pressure" key of y 
	current_pressure = y["pressure"] 

	# store the value corresponding 
	# to the "humidity" key of y 
	current_humidiy = y["humidity"] 

	# store the value of "weather" 
	# key in variable z 
	z = x["weather"] 

	# store the value corresponding 
	# to the "description" key at 
	# the 0th index of z 
	weather_description = z[0]["description"] 

	# print following values 
	print(" Temperature (in K) = " +
					str(current_temperature) +
		"\n atmospheric pressure (in hPa unit) = " +
					str(current_pressure) +
		"\n humidity (in percentage) = " +
					str(current_humidiy) +
		"\n description = " +
					str(weather_description)) 

else: 
	print(" City Not Found ") 

# AI - WIP
import simplejson as json
import math
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.tools.xml.networkwriter import NetworkWriter
from pybrain.tools.xml.networkreader import NetworkReader
ds = SupervisedDataSet(3, 3)


data = open("Z:\sevendata.json", "r").read()
data = json.loads(data)
len = len(data)

for x in range(len):
	try:
		ds.addSample((data[x]["main"]["temp"],data[x]["main"]["humidity"],data[x]["main"]["pressure"]),(data[x+24]["main"]["temp"],data[x+48]["main"]["temp"],data[x+72]["main"]["temp"]))
	except:
		print("nu")
#print(data[x+1]["main"]["temp"])
print("set finished building")

import time
start = time.time()

from pybrain.supervised.trainers import BackpropTrainer
#net = buildNetwork(3, 5, 8, 5, 3)
net = NetworkReader.readFrom('Z:\weights.xml') 
trainer = BackpropTrainer(net, ds, verbose=True)
while True:
	trainer.trainUntilConvergence(maxEpochs=50, verbose=True)
	NetworkWriter.writeToFile(net, 'Z:\weights.xml') 
	print("Trained another 50")
	done = time.time()
	elapsed = done - start
	print(elapsed)
	f = open("Z:\times.txt", "a")
	f.write(elapsed)
	f.close()
	start = time.time()
