#!/usr/local/bin/python3
from pybrain3.tools.shortcuts import buildNetwork
from pybrain3.datasets import *
from pybrain3.supervised.trainers import BackpropTrainer
from math import *
import time
from pprint import pprint
import matplotlib.pyplot as plt

classificate_func = {0: 'sin', 1: 'cos'}
start_time = time.time()

if __name__ == "__main__":
	sinuses = []
	cosinuses = []

	net = buildNetwork(3, 6, 1, bias=True)
	ds = SupervisedDataSet(3, 1)

	for k in range (-10, 10):
		ds.addSample(tuple( 0.5 + 0.3 * cos(k * pi * x / 64) for x in range(-1, 2) ), (1, ))
		ds.addSample(tuple( 0.5 + 0.3 * sin(k * pi * x / 64) for x in range(-1, 2) ), (0, ))	
	trainer = BackpropTrainer(net, ds, learningrate=0.01, verbose=True)
	trainer.trainUntilConvergence(validationProportion=0.5)

	a = classificate_func[int(net.activate(tuple(( 0.5 + 0.3 * cos(2 * pi * x / 64) for x in range(3)))))]
	b = classificate_func[int(net.activate(tuple(( 0.5 + 0.3 * sin(2 * pi * x / 64) for x in range(3)))))]
	print('Искомая функция: %s\n Время выполнения: %s' % (a, time.time() - start_time))
	print('Искомая функция: %s\n Время выполнения: %s' % (b, time.time() - start_time))
	# b = ('Искомая функция: %s\n Время выполнения: %s' % 
	# 	(classificate_func[int(net.activate(tuple(( 0.5 + 0.3 * sin(2 * pi * x / 64) for x in range(3)))))],
	# 	 time.time() - start_time))

	plt.figure(1)
	first_graphic = plt.subplot(211)
	first_graphic.set_title(a)
	first_graphic.plot([ x for x in range (-400, 400)], [ 0.5 + 0.3 * globals()[a](2 * pi * x / 64) for x in range(-400, 400)], 'k')
	second_graphic = plt.subplot(212)
	second_graphic.set_title(b)
	second_graphic.plot([ x for x in range (-400, 400)], [ 0.5 + 0.3 * globals()[b](2 * pi * x / 64) for x in range(-400, 400)], 'k')
	# plt.title(a)
	plt.show()
	print(a, b)


	# pprint(cosinuses_list)
	# pprint(sinsuses_list)
