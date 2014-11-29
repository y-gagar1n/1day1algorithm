import random
import measure

class Heap():

	def __init__(self):
		self.heap_size = 0

	def left(self, i):
		return i * 2 +1

	def right(self, i):
		return i * 2 + 2

	def parent(self, i):
		return max((i - 1) / 2, 0)

	def max_heapify(self, a, i):
		n = len(a) - 1
		l = self.left(i)
		r = self.right(i)	
		if l < self.heap_size and a[l] > a[i]:
			largest = l
		else:
			largest = i
		if r < self.heap_size and a[r] > a[largest]:
			largest = r
		if i != largest:
			a[i], a[largest] = a[largest], a[i]
			self.max_heapify(a, largest)	

	def build_max_heap(self, a):
		self.heap_size = len(a)
		for i in xrange(len(a)/2-1,-1,-1):
			self.max_heapify(a, i)			

def heapsort(a):		
	h = Heap()
	h.build_max_heap(a)	
	for i in xrange(len(a)-1, 0, -1):
		a[0], a[i] = a[i], a[0]
		h.heap_size -= 1
		h.max_heapify(a, 0)		
	return a
	
measure.time(heapsort)
