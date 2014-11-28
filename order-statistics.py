import functools
import measure

def getKthMax(a, k):
	n = len(a)
	return getKthMin(a, n-k-1)

def getKthMin(a, k):
	n = len(a)	
	if n == 1:
		return a[0]
	(a, mid) = partition(a)
	if k == mid: return a[mid]
	if(k > mid): return getKthMin(a[mid:], k - mid)
	else: return getKthMin(a[:mid], k)

def partition(a):	
	n = len(a)
	pivot = a[n-1]
	l = [x for x in a[:-1] if x <= pivot]
	r = [x for x in a[:-1] if x > pivot]
	a = l + [pivot] + r	
	return (a, len(l))

p = functools.partial(getKthMax, k = 150000)
measure.time(p)