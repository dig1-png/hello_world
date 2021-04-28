#! usr/bin/env python
import math
import numpy as np
import time
print("I am the first thread to caculate atan value between a and b")
for i in range(10):
	time.sleep(1)
	a = np.random.choice(180,1,False)
	b = np.random.choice(120,1,False)
	c = math.atan2(a, b)
	print("The " + str(i+1) + "th turn : the arctan value of (" + str(a)+ "," +  str(c)+ ") is :  " + str(c))
