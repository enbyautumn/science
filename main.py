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
# get historical data - WIP


		      
# AI - WIP
import math
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.tools.xml.networkwriter import NetworkWriter
from pybrain.tools.xml.networkreader import NetworkReader
ds = SupervisedDataSet(2, 1)


data = open("/home/mac/data.json", "r").read()
for x in len(data): 
	ds.addsample((data[x]["main"]["humidity"], data[x]["main"]["humidity"]), (data[x + 1]["main"]["temp"]))
	

print("set finished building")
from pybrain.supervised.trainers import BackpropTrainer
net = buildNetwork(2, 5, 1)
trainer = BackpropTrainer(net, ds, verbose=False)
trainer.trainUntilConvergence(maxEpochs=10000)
NetworkWriter.writeToFile(net, 'weights.xml')
print(round(net.activate([1,1])))
print(round(net.activate([3,2])))
print(round(net.activate([3,3])))
print(round(net.activate([4,1])))
print(round(net.activate([1,2])))
print(round(net.activate([4,4])))
