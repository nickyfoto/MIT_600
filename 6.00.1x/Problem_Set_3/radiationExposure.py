# def f(x):
#     import math
#     return 10*math.e**(math.log(0.5)/5.27 * x)

# def f(x):
# 	import math
# 	return 400*math.e**(math.log(0.5)/3.66 * x)

def f(x):
	import math
	return 150*math.e**(math.log(0.5)/32.2 * x)

def radiationExposure(start, stop, step):
	total = 0
	num = (stop-start)/step
	while num >0:
		total += f(start)*step
		start += step
		num -= 1

	return total

# print radiationExposure(0, 5, 1)
# print f(0.5)
print radiationExposure(100, 400, 4)
	
