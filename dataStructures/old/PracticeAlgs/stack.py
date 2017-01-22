class Stack:
	def __init__(self):
		self.list = []

	def push(self, data):
		self.list.append(data)

	def pop(self):
		return self.list.pop()

	def isEmpty(self):
		return len(self.list) == 0

	def size(self):
		return len(self.list)