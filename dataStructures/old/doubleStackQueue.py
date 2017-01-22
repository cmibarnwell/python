#Creating a Queue with 2 stacks. Let's do this. WIP

class Stack:
	def __init__(self):
		self.items=[]

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

	def peek(self):
		return self.items[len(self.items)-1]


class Queue:
	def __init__(self):
		self.half1 = Stack()
		self.half2 = Stack()

	def isEmpty(self):
		if(self.half1.isEmpty() and self.half2.isEmpty()):
			return True
		else:
			return False

	def enqueue(self, item):
		print(self.half1.isEmpty())
		while(self.half1.isEmpty() == False):
			self.half2.push(self.half1.pop())
			print("pushing to Backup %d" %(self.half1.pop()))
		self.half1.push(item)
		print("pushing original %d" %(item))
		while(self.half2.isEmpty() == False):
			self.half1.push(self.half2.pop())
			print("pushing from backup %d" %(self.half2.pop()))
		
	def dequeue(self):
		return self.half1.pop()




q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
