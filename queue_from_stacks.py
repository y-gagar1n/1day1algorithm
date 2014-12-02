class Stack:

	def __init__(self):
		self.capacity = 4
		self.data = [None] * self.capacity
		self.i = 0		

	def push(self, v):
		self.data[self.i] = v
		self.i += 1
		if self.i == self.capacity:
			self.__expand()

	def pop(self):
		if self.i == 0: 
			raise Exception("Stack is empty")
		self.i -= 1
		r = self.data[self.i]		
		return r

	def empty(self):
		return self.i == 0

	def __expand(self):
		new_capacity = self.capacity * 2
		new_data = [None] * new_capacity
		for i in range(self.capacity):
			new_data[i] = self.data[i]
		self.capacity = new_capacity
		self.data = new_data

class Queue:

	def __init__(self):
		self.inbox = Stack()
		self.outbox = Stack()

	def enqueue(self, v):
		self.inbox.push(v)

	def dequeue(self):
		if self.outbox.empty():
			if self.inbox.empty():
				raise Exception("Queue is empty")				
			while not self.inbox.empty():
				e = self.inbox.pop()
				self.outbox.push(e)
		return self.outbox.pop()