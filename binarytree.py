import random
import time

class Node:

	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.right = None
		self.left = None
		self.parent = None

	def add(self, node):		
		if node.key > self.key:
			if self.right == None:
				self.right = node
				node.parent = self
			else:
				self.right.add(node)
		else:
			if self.left == None:
				self.left = node
				node.parent = self
			else:
				self.left.add(node)

	def show(self, level = 0):
		border = level * "|"
		str = ""
		str = "%s%s" % (border, self.key)
		if self.left != None:
			str += "\n%s|--%s" % (border, self.left.show(level + 1))
		if self.right != None:
			str += "\n%s|--%s" % (border, self.right.show(level + 1))
		return str

	def find(self, key):
		if key == self.key:
			return self.value
		if key > self.key:
			if self.right == None:
				return None
			else:
				return self.right.find(key)
		else :
			if self.left == None:
				return None
			else:
				return self.left.find(key)


input = [random.randrange(300000) for x in range(300000)]

tree = None	
for x in input:
	node = Node(x,2*x)
	if tree == None:
		tree = node
	else: 
		tree.add(node)

s = time.time()
print tree.find(input[0])
f = time.time()
print f - s