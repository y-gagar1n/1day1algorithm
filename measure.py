import time as systime
import random

def time(func,n=300000):
	input = [random.randrange(n) for x in range(n)]
	start = systime.time()
	func(input)
	end = systime.time()
	return end - start

def show(func, n=10):
	input = [random.randrange(n) for x in range(n)]
	print(func(input))