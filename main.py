# get current weather data
import requests, json 
api_key = "9a6f64de069cb85d600ee405159a85f3"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
complete_url = base_url + "appid=" + api_key + "&q=" + 'Dover' 
response = requests.get(complete_url) 
x = response.json() 
if x["cod"] != "404": 
	y = x["main"] 
  current_temperature = (y["temp"])
	current_pressure = y["pressure"] 
  current_humidiy = y["humidity"] 
	z = x["weather"] 
	weather_description = z[0]["description"] 
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
left = 0
right = 0
loops = 10 #This determines how high the set goes e.x. loop of 10 goes from 0,0 to 9,9
while left < loops:
  ds.addSample((left,right),(left+right))
  right+=1
  if right >= loops:
    right = 0
    left+=1
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
