'''
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. 
(i.e., from left to right, then right to left for the next level and alternate between).
'''

# If zigzag is True then ==> appendleft(right node) then appendleft(left node)  
# 			pop ==> pop()
					
# If zigzag is False then ==> append (left node) then append (right node)
# 			pop ==> popleft()


from typing import List
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root:TreeNode) -> List[List[int]]:
        if root is None:
            return 

        ans = []
        q = deque()
        zigzag = False
        q.append(root)

        while len(q):
            level = []
            for i in range(len(q)):
                if zigzag:
                    node = q.pop()
                    level.append(node.val)
                    print
                    if node.right:
                        q.appendleft(node.right)
                    if node.left:
                        q.appendleft(node.left)
                else:
                    node = q.popleft()
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            
            ans.append(level)
            zigzag = not(zigzag)

        return ans


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.left.left = None
root.left.right = None
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

s = Solution()
ans = s.zigzagLevelOrder(root)
print(ans)