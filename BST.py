class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def start_insert(self,start,new_val):
        if start.value < new_val:
            if start.right:
                self.start_insert(start.right,new_val)
            else:
                start.right = Node(new_val)
        
        else:
            if start.left:
                self.start_insert(start.left,new_val)
            else:
                start.left = Node(new_val)

    def insert(self, new_val):
        self.start_insert(self.root,new_val)

    def start_search(self,start,find_val):
        if start != None:
            if start.value == find_val:
                return True
            elif start.value < find_val:
                self.start_search(self.right,find_val)
            else:
                self.start_search(self.left,find_val)
        return False


    def search(self, find_val):
        return self.start_search(self.root,find_val)

# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search

# Should be True
print (tree.search(4))
# Should be False
print (tree.search(6))
