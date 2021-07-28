'''
Given the root of a binary tree and an integer targetSum,
return true if the tree has a root-to-leaf path such that adding up all the values 
along the path equals targetSum.

A leaf is a node with no children.

Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasSum(self, root, targetSum, curr_sum):
        if root is None:
            return False
        curr_sum += root.val
        # if the root node is leaf node and sum is equal to targetSum
        if curr_sum == targetSum and root.left is None and root.right is None:
            return True
        # serach for sum in left and right subtree
        return self.hasSum(root.left, targetSum, curr_sum) or self.hasSum(root.right, targetSum, curr_sum)
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        return self.hasSum(root, targetSum, 0)


s = Solution()

tree = TreeNode(5)
tree.left = TreeNode(2)
tree.right = TreeNode(3)

ans = s.hasPathSum(tree, 5)
print(ans)