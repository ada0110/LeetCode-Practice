class BinaryTree():
    def __init__(self, value):
        self.data = value
        self.left_child = None
        self.right_child = None
    
    # When there is no left child, simply add a node to the tree but if there exists
    # a left child then we insert a node and push the existing child down one level in the tree. 
   
    def insert_left(self, new_node):
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            new_child = BinaryTree(new_node)
            new_child.left_child = self.left_child
            self.left_child = new_child

    def insert_right(self, new_node):
        if self.right_child is None:
            self.right_child = BinaryTree(new_node)
        else:
            new_child = BinaryTree(new_node)
            new_child.right_child = self.right_child
            self.right_child = new_child

    def get_root(self):
        return self.data
    
    def set_root_val(self, new_root):
        self.data = new_root

    def get_left_child(self):
        return self.left_child
    
    def get_right_child(self):
        return self.right_child

    def printTree(self):
        if self.left_child:
            self.left_child.printTree()
        print(self.data)
        if self.right_child:
            self.right_child.printTree()


a_tree = BinaryTree(3)
a_tree.insert_left(4)
a_tree.insert_left(5)
a_tree.insert_right(6)
a_tree.insert_right(8)

# print(a_tree.get_root())
# print(a_tree.get_left_child())

print(a_tree.printTree())