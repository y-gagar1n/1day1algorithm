class Node:
	def __init__(self, key, value):
		self.left = None
		self.right = None
		self.parent = None
		self.key = key
		self.value = value
		self.color = 0 #0 - red, 1 - black

	def insert(self, node):
		node.color = 0

	def sibling(self):
		if self == self.parent.left:
			return self.parent.right
		else:
			return self.parent.left

	def uncle(self):
		return self.parent.sibling()

	def grandparent(self):
		return self.parent.parent

	def insert(self, node):
		if node.key <= self.key:
			if self.left != None:
				self.left.insert(node)
			else:
				node.color = 0
				self.left = node
				node.parent = self
				ensure(self.left)
		else:
			if self.right != None:
				self.right.insert(node)
			else:
				node.color = 0
				self.right = node
				node.parent = self
				self.ensure(self.right)

	def rotate_right(self):
		saved_p = self.parent
		saved_left = self.left
		if saved_p.left == self:
			saved_p.left = saved_left
		else: 
			saved_p.right = saved_left
		self.left = saved_left.right
		saved_left.right = self
		saved_left.parent = saved_p

	def rotate_left(self):
		saved_p = self.parent
		saved_right = self.right
		if saved_p.right== self:
			saved_p.right = saved_right
		else: 
			saved_p.left = saved_right
		self.right = saved_right.left
		saved_right.left = self
		saved_right.parent = saved_p

	def ensure(self, node):
		if self.parent == None:
			self.color = 1
			return
		if self.parent.color == 1:
			return
		if self.parent.color == 0 and self.uncle().color == 0:
			self.parent.color = 1
			self.uncle().color = 1
			self.grandparent().color = 0	
			ensure(self.grandparent())
			return		
		if self.parent.color == 0 and self.uncle().color == 1: 
			if self == self.parent.right and self.parent == self.grandparent().left:
				self.rotate_left(self.parent)
			elif self == self.parent.left and self.parent == self.grandparent().right:
				self.rotate_right(self.parent)
			if self == self.parent.left and self.parent == self.grandparent().left:
				self.rotate_left(self.grandparent())
				return
			elif self == self.parent.right and self.parent == self.grandparent().right:
				self.rotate_right(self.grandparent())
				return

t = Node(1,2)
t.insert(Node(5,10))




