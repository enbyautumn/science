from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.tools.xml.networkwriter import NetworkWriter
from pybrain.tools.xml.networkreader import NetworkReader
from pybrain.supervised.trainers import BackpropTrainer
import simplejson as json
import math
import requests, json 
import random



net = NetworkReader.readFrom('/Users/mac/weights.xml') 
data = open("/Users/mac/data.json", "r").read()
data = json.loads(data)

#    ((data[x]["main"]["humidity"],data[x]["main"]["pressure"]),(data[x+1]["main"]["temp"])
x = random.randrange(0, 1000)
print("expected: " + str(data[x+1]["main"]["temp"]))
print(net.activate([data[x]["main"]["humidity"],data[x]["main"]["pressure"]]))
