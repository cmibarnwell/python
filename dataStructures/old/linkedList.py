#List Elements
class Node:

	def __init__(self, initData):
		self.data = initData
		self.next = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self, new):
		self.data = new

	def setNext(self, new):
		self.next = new

class LinkedList:
	def __init__(self):
		self.head= None

	def insert(self, val):
		#Uses search function to look for data
		check, previous, current = self.__search__(val)

		#See if already present
		if check:
			return

		#Create new node and place in list
		node = Node(val)
		if(previous == None):
			node.setNext(self.head)
			self.head = node
		else:
			node.setNext(current)
			previous.setNext(node)

	#Private search function for class use only
	def __search__(self, val):
		current = self.head
		previous = None
		stop = False
		while current != None and not stop:
			if(current.getData()== val):
				return True, previous, current
			elif(val < current.getData()):
				stop = True
			else:
				previous = current
				current = current.getNext()
		return False, previous, current

	def size(self):
		current= self.head
		count = 0
		while current != None:
			count += 1
			current = current.getNext()

		return count

	def remove(self, val):
		found, previous, current = self.__search__(val)
		if not found:
			print("Error, %s not found" %(val))
			return
		if(previous== None):
			self.head = current.getNext()
		else:
			previous= current.getNext()
		current = None


	#Checks for list population
	def isEmpty(self):
		return self.head== None

	def printList(self):
		current = self.head
		while current:
			print(current.getData())
			current = current.getNext()

def main():
	list= LinkedList()
	list.insert(5)
	list.insert(6)
	list.insert(2)
	list.insert(3)


	print(list.isEmpty())
	print(list.size())

	list.remove(2)
	print(list.size())
	list.remove(2)
	list.printList()

if __name__== "__main__":
	main()
