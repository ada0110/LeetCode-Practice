'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
'''
# Definition for a binary tree node.
from typing import Text


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root ==None or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left is None and right is None:
            return None
        
        if left and right:
            return root

        if left is None:
            return right
        else:
            return left 

#                 3
#            5         1
#        6     2    0    8
#      n  n  7   4  


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

s = Solution()
ans = s.lowestCommonAncestor(tree, tree.left.left, tree.left.right)
print(ans.val)



