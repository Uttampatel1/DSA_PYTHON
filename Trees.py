class Node(object):
    def __init__(self,value):
        self.value= value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self,root):
        self.root = Node(root)

    def search(self,find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        return self.preorder_search(tree.root,find_val)
        
    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        return self.preorder_print(tree.root, "")[:-1]

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        if start != None:
            if start.value == find_val:
                return True
            else:
                return self.preorder_search(start.left,find_val) | self.preorder_search(start.right,find_val)
        return False

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left,traversal)
            traversal = self.preorder_print(start.right,traversal)
        return traversal

    def inorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        if start:
            traversal = self.preorder_print(start.left,traversal)
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.right,traversal)
        return traversal

    def postorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        if start:
            traversal = self.preorder_print(start.left,traversal)
            traversal = self.preorder_print(start.right,traversal)
            traversal += (str(start.value) + "-")
        return traversal

    # def printInorder(self,root):
    #      if root:
    #         # First recur on left child
    #         self.printInorder(root.left)
    #             # then print the data of node
    #         print(root.value,end="-")
    #             # now recur on right child
    #         self.printInorder(root.right)

    # def printPostorder(self,root):
    #      if root:
    #         # First recur on left child
    #         self.printPostorder(root.left)
    #             # now recur on right child
    #         self.printPostorder(root.right)
    #         # then print the data of node
    #         print(root.value,end='-')
    
            
# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
print (tree.search(4))
# Should be False
print (tree.search(6))

# Test print_tree
# Should be 1-2-4-5-3
print (tree.print_tree())


print(tree.inorder_print(tree.root,"Inorder:"))
print(tree.preorder_print(tree.root,"Preorder:"))
print(tree.postorder_print(tree.root,"Postorder:"))

# print("Inorder Traversal:")
# print(tree.printInorder(tree.root))
# print("PostOrder Traversal:")
# print(tree.printPostorder(tree.root))





# ******************************************************************************************************************

# Python program to do inorder traversal without recursion

# A binary tree node
class Node:
	
	# Constructor to create a new node
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

# Iterative function for inorder tree traversal
def inOrder(root):
	
	# Set current to root of binary tree
	current = root
	stack = [] # initialize stack
	
	while True:
		
		# Reach the left most Node of the current Node
		if current is not None:
			
			# Place pointer to a tree node on the stack
			# before traversing the node's left subtree
			stack.append(current)
		
			current = current.left

		
		# BackTrack from the empty subtree and visit the Node
		# at the top of the stack; however, if the stack is
		# empty you are done
		elif(stack):
			current = stack.pop()
			print(current.data, end=" ") # Python 3 printing
		
			# We have visited the node and its left
			# subtree. Now, it's right subtree's turn
			current = current.right

		else:
			break
	
	print()

# Driver program to test above function

""" Constructed binary tree is
			1
		/ \
		2	 3
	/ \
	4 5 """

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

inOrder(root)

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)
