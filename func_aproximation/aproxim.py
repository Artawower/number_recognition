#!/usr/local/bin/python3

from pybrain3.tools.shortcuts import buildNetwork
from pybrain3.datasets import *
from pybrain3.supervised.trainers import BackpropTrainer
from math import *
import time

test_func = lambda x, k: 0.5 + k * sin(2 * 3.1415 * x / 64) 
start_time = time.time()
if __name__ == "__main__":
	print(test_func(3, 5.54))
	net = buildNetwork(3, 3, 1, bias=True)
	ds = SupervisedDataSet(3, 1)

	for x in range(10):
		for k in range(10):
			ds.addSample((x, test_func(x, k)), k)

	
	train = BackpropTrainer(net, learningrate=0.01, momentum=0.05)	
	train.trainOnDataset(ds, 1000)
	train.testOnData()	
	print(net.activate((3, 2)))
	# print(test_func(90, 1))
	print('Время выполнения: %s сек' % (time.time() - start_time))