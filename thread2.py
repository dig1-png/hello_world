#! /Users/fanghao_w/opt/anaconda3/bin/python
import math
import numpy as np
import time
print("I am the second thread to caculate sin(c)")
for i in range(10):
	time.sleep(2)
	a = np.random.choice(180,1,False)
	b = np.random.choice(120,1,False)
	c = math.atan2(a, b)
	print("The " + str(i+1) + "th turn : the sin value of (" + str(c) +  ") is :  " + str(math.sin(c)))
