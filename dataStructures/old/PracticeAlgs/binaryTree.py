class Node:
	def __init__(self, initData):
		self.data = initData
		self.right = None
		self.left = None

class Tree:
	def __init__(self):
		self.root = None

	def insert(self, data):
		if(self.root == None):
			self.root = Node(data)
		else:
			self._insert(data, self.root)

	def _insert(self, data, node):
		if(data > node.data):
			if(node.right != None):
				self._insert(data, node.right)
			else:
				node.right = Node(data)
		elif(data < node.data):
			if(node.left != None):
				self._insert(data, node.left)
			else:
				node.left = Node(data)
		elif(data == node.data):
			return

	def search(self, data):
		if(self.root != None):
			return self._search(data, self.root)
		else:
			return None

	def _search(self, data, node):
		if(data > node.data):
			if(node.right != None):
				self._search(data, node.right)
			else:
				return None
		elif(data < node.data):
			if(node.left != None):
				self._search(data, node.left)
			else:
				return None
		elif(data == node.data):
			return node
		else:
			return None

	def isEmpty(self):
		return self.root == None

	def depthCheck(self):
		if(self.root != None):
			return self._depthCheck(self.root)
		else:
			return 0

	def _depthCheck(self, node):
		if(node != None):
			iLeft = self._depthCheck(node.left)
			iRight = self._depthCheck(node.right)
		else:
			return 0
		if(iLeft>iRight):
			return iLeft + 1
		else:
			return iRight + 1

	def printTree(self):
		if(self.root != None):
			self._printTree(self.root)

	def _printTree(self, node):
		if(node != None):
			self._printTree(node.left)
			print(node.data)
			self._printTree(node.right)

	def deleteTree(self):
		self.root = None


tree= Tree()
tree.insert(3)
tree.insert(4)
tree.insert(0)
tree.insert(8)
tree.insert(2)

print('Tree data:')
tree.printTree()

print('Tree Depth:',tree.depthCheck())

print('Tree find "3" Value:',(tree.search(3)).data)
print('Tree find "10":',tree.search(10))
tree.deleteTree()
tree.printTree()