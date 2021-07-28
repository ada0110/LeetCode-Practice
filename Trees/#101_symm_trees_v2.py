# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isMirror(self, t1, t2):
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False
        return t1.val ==t2.val and self.isMirror(t1.right, t2.left) and self.isMirror(t1.left, t2.right)

    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root, root)


# creating tree
tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(2)
tree.left.left = TreeNode(3)
# tree.left.left = TreeNode(None)
tree.left.right = TreeNode(4)
# tree.left.right = TreeNode(3)
tree.right.left = TreeNode(4)
# tree.right.left = TreeNode(2)
tree.right.right = TreeNode(3)


# [1,2,2,3,4,4,3] --> True
# [1,2,2,null,3,null,3] --> False
#           1
#       2       2
# null     3  null  3 
# False

# [1,2,2,2,null,2] -->
#           1
#        2    2
#    2  null 2  

s = Solution()
ans = s.isSymmetric(tree)
print(ans)