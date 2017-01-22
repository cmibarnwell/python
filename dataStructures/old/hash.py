""" Fast implementation
def hash(astring, tablesize):
	sum = 0
	for pos in range(len(astring))
		sum = sum + (ord(astring[pos])*pos]

	return sum%tablesize
"""

class HashTable:
	def __init__(self):
		self.size = 11
		self.slots = [None]* self.size
		self.data - [None] * self.size

	def put(self, key, data):
		hashValue = self.hashFunction

	def hashFunction(self, key, size):
		return key%size

	def rehash(self, oldhash, size):
		return (oldhash+1)%size