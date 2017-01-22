class Vertex:
	def __init__(self, key):
		self.id = key
		self.connectedTo = {}

	def addNeighbor(self, nbr, weight = 0):
		self.connectedTo[nbr] = weight


class Graph:
	def __init__(self):
		self.vertList = {}
		self.vertCount = 0

	def addVertex(self, key):
		self.vertCount += 1
		newVertex = Vertex(key)
		self.vertList[key] = newVertex
		return newVertex

	def addEdge(self, vert, vert2, cost = 0):
		if vert not in self.vertList:
			newVertex = self.addVertex(vert)
		if vert2 not in self.vertList:
			newVertex = self.addVertex(vert2)
		self.vertList[vert].addNeighbor(vert2, cost)

	def __iter__(self):
		return iter(self.vertList.values())
		


g = Graph()
for i in range(6):
	g.addVertex(i)

print(g.vertList)

g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)
g.addEdge(2,4)

#for v in g:
#	for w in v.connectedTo:
#		print('(%s, %s)'%(v.id,w.id))
#		print('%s'%(v.connectedTo[w]))
