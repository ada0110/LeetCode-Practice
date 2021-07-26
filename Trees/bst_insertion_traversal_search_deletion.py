class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

# inserting a node in BST
def insert(root, node):
    # if there are no nodes in tree then insert the node as root node
    if root is None:
        root = node
        return 
    
    # if root val is smaller than node val then insert node in the right of root
    # else insert node in the left of root
    if root.data < node.data:
        if root.right is None:
            root.right = node
        else:
            insert(root.right, node)

    else:
        if root.left is None:
            root.left = node
        else:
            insert(root.left, node)


# seraching for a node in BST
# intially the node will be root, key is the node we want to search
def search(node, key):
    print("current node is: ", node.data)
    if node is None:
        return None
    
    if node.data == key:
        print("Node found!")
        return node
    
    if key > node.data:
        # means we need to search in right subtree
        return search(node.right, key)
        # otherwise we search in left subtree
    return search(node.left, key)

# finding min value in the right subtree
# for right subtree the min value will be in the leftmost node in right subtree
def minimumValue(node):
    while node.left is not None:
        node = node.left
    return node

# intially the node will be root, key is the node we want to delete
def deleteNode(node, key):
    if node is None:
        return None
    
    # if key is less than root means the key lies in left subtree 
    # so we recursively call deleteNode method on left subtree
    if key < node.data:
        node.left = deleteNode(node.left, key) 
    
    # if key is greater that root means it must lie in right subtree    
    elif key > node.data:
        node.right = deleteNode(node.right, key)
    
    # key == node.data then replace the current node with inorder predecessor(max of LHS)
    # else replace with inorder successor (min of RHS)
    else:
        # checking whether current node has only one child
        # if current node has only right child
        if node.left is None:
            temp = node.right
            # delete current node
            node = None
            return temp

        # if current node has only left child
        elif node.right is None:
            temp = node.left
            node = None
            return temp
        
        # if the current node has both left and right children
        # then find min val in right subtree --> inorder successor and replace current node with it after deletion
        temp = minimumValue(node.right)
        node.data = temp.data
        node.right = deleteNode(node.right, temp.data)

    return node



# -----------------traversal-------------------------------------------
def preorder(node):
    if node is not None:
        print(node.data)
        preorder(node.left)
        preorder(node.right)


def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data)
        inorder(node.right)


def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data)

# --------------------------------------------------------------------
#            5
#         /     \
#        3       7
#      /  \     /  \
#     2    4   6    8
# --------------------------------------------------------------------

tree = Node(5)
insert(tree, Node(3))
insert(tree, Node(2))
insert(tree, Node(4))
insert(tree, Node(7))
insert(tree, Node(6))
insert(tree, Node(8))

print("preorder:")
preorder(tree)
print()

print("inorder:")
inorder(tree)
print()

print("postorder:")
postorder(tree)

# searching for node 6
print("search for node:")
search(tree, 6)

# deleting node from tree and replacing with inorder successor
print("node deletion:")
deleteNode(tree, 3)
print("inorder traversal after node deletion")
print(inorder(tree))