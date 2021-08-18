# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#  time complexity: O(n)
# space complexity: O(h) where h is the height of the tree --> cz of recursive nature
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left, right) + 1

tree = TreeNode(2)
tree.left = TreeNode(4)
tree.right = TreeNode(7)
tree.right.left = TreeNode(12)
tree.right.right = TreeNode(15)
tree.right.right.left = TreeNode(18)

s = Solution()
ans = s.maxDepth(tree)
print(ans)