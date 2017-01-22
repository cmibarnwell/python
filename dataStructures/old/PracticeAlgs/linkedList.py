class Node: 
	def __init__(self, data=None):
		self.data = data
		self.next = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self, data):
		self.data = data

	def setNext(self, node):
		self.next = node

class LinkedList:
	def __init__(self):
		self.head = None
		self.count= 0

	def insert(self, data):
		find, previous = self.search(data)
		if(find != None):
			return find
		new = Node(data)
		self.count+= 1
		if(previous == None):
			new.next = self.head
			self.head = new
		else:
			new.next = previous.next
			previous.next = new


	def search(self, data):
		current = self.head
		previous = None
		if(current != None):
			return self._search(self, data, node, previous)
		else:
			return None, previous

	def _search(self, data, node, previous):
		if(node != None):
			if(node.data == data):
				return node, previous
			elif(data < node.data):
				return None, previous
			else:
				previous = node
				return self._search(data, node.next, previous)
		else:
			return None, previous

	def removeNode(self, data):
		find, previous = self.search(data)
		if(find == None):
			return None
		if(previous == None):
			self.head = find.next
		else:
			previous = find.next
		return find


	def isEmpty(self):
		return self.head == None

	def size(self):
		return self.count

list= LinkedList()
list.insert(5)
list.insert(6)
list.insert(2)
list.insert(3)


print(list.isEmpty())
print(list.size())

list.removeNode(2)
print(list.size())
list.removeNode(2)
