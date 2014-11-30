import measure
import math
import functools

def sort_by_digit(a, digit_num, base):
	buckets = [[] for i in range(base)]
	for x in a:
		digit = int(round(x / (base ** digit_num)) % base)
		buckets[digit].append(x)
	i = 0
	for b in buckets:
		for x in b:
			a[i] = x
			i += 1


def radixSort(a, base):	
	passes = int(round(math.log(max(abs(x) for x in a), base))) + 1
	for i in range(passes):		
		sort_by_digit(a, i, base)
	return a

func = functools.partial(radixSort, base = 30000)
print measure.time(func)