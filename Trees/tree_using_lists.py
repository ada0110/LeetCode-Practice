class Treelist():
    # The make_binary_tree function simply constructs a list with a root node
    # and two empty sublists for the children.
    def make_bin_tree(self, root):
        return ([root, [], []])

    # To add a left subtree to the root of a tree, we need to insert a new list into the second position of the root list.
    # If the list already has something in the second position, we need to keep track of it 
    # and push it down the tree as the left child of the list we are adding
    def insert_left(self, root, new_child):
        old_child = root.pop(1)

        if(len(old_child) > 1):
            # pushing down the old child 
            root.insert(1, [new_child, old_child, []])
        else:
            root.insert(1, [new_child, [], []])
        return root
    

    def insert_right(self, root, new_child):
        old_child = root.pop(2)

        if (len(old_child) > 1):
            # pushing down the old child
            root.insert(2, [new_child, [], old_child])
        else:
            root.insert(2, [new_child, [], []])

    def get_root(self, root):
        return root[0]
    
    def set_root(self, root, new_val):
        root[0] = new_val

    def get_left_child(self, root):
        return root[1]

    def get_right_child(self, root):
        return root[2]



s = Treelist()

a = s.make_bin_tree(3)
s.insert_left(a, 5)
s.insert_left(a, 4)
s.insert_right(a, 7)
s.insert_right(a, 6)

print("tree:", a)
