'''
Serialization is the process of converting a data structure or object into a sequence of bits 
so that it can be stored in a file or memory buffer, or transmitted across a network connection 
link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. 
There is no restriction on how your serialization/deserialization algorithm should work. 
You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized 
to the original tree structure.
'''

# Definition for a binary tree node.
# from _typeshed import SupportsLessThan


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        # time and space = O(n)
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return "X#"
        
        # preorder traversal of the tree
        return str(root.val) + "#" + self.serialize(root.left) + self.serialize(root.right)

        



        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def dfs():
            val = next(data)
            if val == 'X':
                return None
            node = TreeNode(int(val))

            node.left = dfs()
            node.right = dfs()
            
            return node

        data = iter(data.split("#"))
        # print(list(data))

        return dfs()



#                 3
#           5          1
#        6    2     0    8
#           7   4  

tree = TreeNode(3)
tree.left = TreeNode(5)
tree.left.left = TreeNode(6)
tree.left.right = TreeNode(2)
# tree.left.left.left = TreeNode(None)
# tree.left.left.right = TreeNode(None)
tree.left.right.left = TreeNode(7)
tree.left.right.right = TreeNode(4)
tree.right = TreeNode(1)
tree.right.right = TreeNode(8)
tree.right.left = TreeNode(0)

# s = Codec()
# ans = s.serialize(tree)
# print(ans)

# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()
ans = deser.deserialize(ser.serialize(tree))