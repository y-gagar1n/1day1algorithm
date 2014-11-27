import time as systime
import random

def time(func):
	input = [random.randrange(3000000) for x in range(300000)]
	start = systime.time()
	func(input)
	end = systime.time()
	print end - start

def show(func, n):
	input = [random.randrange(n) for x in range(n)]
	print(func(input))