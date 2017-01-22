def commonParent(node1, node2):
	if node1.parent.left == node 2 or node1.parent.left == node 2:
		return node1.parent
	elif(node1.parent != None or node2.parent != None):
		return commonParent(node1.parent, node2.parent)
	else:
		return None