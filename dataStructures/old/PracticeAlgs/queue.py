class Queue:
	def __init__(self):
		self.list = []

	def enqueue(self, data):
		self.list.insert(0, data)

	def dequeue(self):
		self.list.pop()

	def isEmpty(self):
		return len(self.list) == 0

	def size(self):
		return len(self.list)