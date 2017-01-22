
class Node:
	def __init__(self, val):
		self.l = None
		self.r = None
		self.v = val

class Tree:
	def __init__(self):
		self.root = None

	def getRoot(self):
		return self.root

	def add(self, val):
		if(self.root == None):
			self.root = Node(val)
		else:
			self._add(val, self.root)

	def _add(self, val , node):
		if(val<node.v):
			if(node.l !=None):
				self._add(val, node.l)
			else:
				node.l = Node(val)

		else:
			if(node.r !=None):
				self._add(val, node.r)
			else:
				node.r = Node(val)

	def find(self, val):
		if(self.root != None):
			return self._find(val, self.root)
		else:
			return None

	def _find(self, val, node):
		if(val== node.v):
			return node
		elif(val < node.v and node.r !=None):
			self._find(val, node.l)
		elif(val>node.v and node.r !=None):
			self._find(val, node.r)
		else:
			return None

	def deleteTree(self):
		self.root= None #Thank you garbage collector

	def printTree(self):
		if(self.root!=None):
			self._printTree(self.root)

	def _printTree(self, node):
		if(node != None):
			self._printTree(node.l)
			print(str(node.v)+ ' ')
			self._printTree(node.r)

	def treeDepth(self, node):
		if node != None:
			iLeft= self.treeDepth(node.l)
			iRight= self.treeDepth(node.r)
		else:
			return 0
		if iLeft>iRight:
			return iLeft+1
		else:
			return iRight+1




#	 3
# 0	  4
#   2  8

def main():
	tree= Tree()
	tree.add(3)
	tree.add(4)
	tree.add(0)
	tree.add(8)
	tree.add(2)

	print('Tree data:')
	tree.printTree()

	print('Tree Depth:',tree.treeDepth(tree.root))
	
	print('Tree find "3" Value:',(tree.find(3)).v)
	print('Tree find "10":',tree.find(10))
	tree.deleteTree()
	tree.printTree()

if __name__== "__main__":
	main()