import sys

class Vertex:
	def __init__(self, key):
		self.id = key
		self.connectedTo = {}

		#Below is necessary only for breadth-first search
		self.distance = sys.maxsize
		self.color = 'white'
		self.pred = None

	def addNeighbor(self, nbr, weight =0):
		self.connectedTo[nbr] = weight

	def __str__(self):
		return str(self.id) + ' connectedTo:' + str([x.id for x in self.connectedTo])

	def getConnections(self):
		return self.connectedTo.keys()

	def getId(self):
		return self.id

	def getWeight(self,nbr):
		return self.connectedTo[nbr]

	def setColor(self, color):
		self.color = color

	def setDistance(self, d):
		self.d = distance

	def setPred(self, p):
		self.pred = p

	def getColor(self):
		return self.color

	def getDistance(self):
		return self.d

	def getPred(self):
		return self.pred


class Graph:
	def __init__(self):
		self.vertList = {}
		self.numVertices = 0

	def addVertex(self,key):
		self.numVertices = self.numVertices + 1
		newVertex = Vertex(key)
		self.vertList[key] = newVertex
		return newVertex

	def getVertex(self, n):
		if n in self.vertList:
			return self.vertList[n]
		else:
			return None

	def __contains__(self, n):
		return n in self.vertList

	def addEdge(self, f, t, cost= 0):
		if f not in self.vertList:
			nv = self.addVertex(f)
		if t not in self.vertList:
			nv = self.addVertex(t)
		self.vertList[f].addNeighbor(self.vertList[t], cost)

	def getVertices(self):
		return self.vertList.keys()

	def __iter__(self):
		return iter(self.vertList.values())

	def bfs(self, start):
		start.setDistance(0)
		start.setPred(None)
		vertQueue = Queue()
		vertQueue.enqueue(start)
		while(vertQueue.size()>0):
			currentVert = vertQueue.dequeue()
			for nbr in currentVert.getConnections():
				if(nbr.getColor = 'white'):
					nbr.setColor('gray')
					nbr.setDistance(currentVert.getDistance()+1)
					nbr.setPred(currentVert)
					vertQueue.enqueue(nbr)
			currentVert.setColor('black')

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

for v in g:
	for w in v.getConnections():
		print("(%s, %s)"%(v.getId(),w.getId()))
		print("%s"%(v.getWeight(w)))
