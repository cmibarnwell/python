class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right



def searchTreeCheck(tree):
    temp=tree
    while(temp.left !=None):
        if not temp.left.value<temp.value or temp.right<temp.value:
            return False
        else:
            temp=temp.left

    temp = tree

    while(temp.right !=None):
        if not temp.right.value>temp.value or temp.left>temp.value:
            return False
        else:
            temp=temp.right

    return True