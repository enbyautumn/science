from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.tools.xml.networkwriter import NetworkWriter
from pybrain.tools.xml.networkreader import NetworkReader
from pybrain.supervised.trainers import BackpropTrainer
import simplejson as json
import math
import requests, json 


net = NetworkReader.readFrom('/Users/mac/weights.xml') 

