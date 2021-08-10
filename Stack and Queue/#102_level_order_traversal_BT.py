
# time and space complexity: O(n)

from typing import Deque, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if root is None:
            return ans

        # q = [] 
        # q.append(root)
        # print(q)
        # OR use a deque
        q = deque([root])
        while (len(q)):
            n = len(q)
            temp = []
            for i in range(n):
                # f = q.pop(0) 
                # OR
                f = q.popleft()
                temp.append(f.val)
                print(temp)

                if f.left is not None:
                    q.append(f.left)
                if f.right is not None:
                    q.append(f.right)

            if len(temp) > 0:
                ans.append(temp[:])
                temp.clear()
            # return ans
            print("ans:", ans)
            # print("temp:", temp)
        
        return ans 
               
          
            
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

# building tree for given input
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.left.left = None
root.left.right = None
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

s = Solution()
ans = s.levelOrder(root)
print(ans)
'''
q = dequeue([root])
ans = []
while q:
    n = len(q)
    temp = []
    loop n times:
        f = q.popleft()
        temp.append(f.val)
        if f.left is valid:
            q.append(f.left)
        if f.right is valid:
            q.append(f.right)
    ans.append(temp)
    temp.clear()

'''


"""
               10
#           5       20
#       8         3    7
#                    1   2

queue = [10]
ans = []
n = 1
temp = []
f = 10
temp = [10]
queue = [5, 20]
ans = temp = [10] 

----------------------------
queue = [5, 20]
n = 2
loop 2 times:

1.
f = 5
temp = [5]
queue = [20, 8]
ans = [5]

2.
queue = [20, 8]
f = 20
temp = [5, 20]
queue = [8, 3, 7]
ans = [[10], [5,20]]
-----------------------------

queue = [8, 3, 7]
while q:
    n = 3
    loop 3 times:
    # first time:
        f = 8
        temp = 8
        queue = [3, 7] //no change in queue as 8 has no childrens

    # second time
        queue = [3, 7]
        f = 3
        temp = [8, 3]
        queue = [7]
    
    # third time
        queue = [7]
        f = 7
        temp = [8, 3, 7]
        queue = [1, 2]
    ans = [[10], [5,20], [8, 3, 7]]
-------------------------------

queue = [1, 2]
n = 2
loop runs 2 times:
# first time
    f = 1
    temp = [1]
    
# second time
    f = 2
    temp = [1, 2]
    ans = [[10], [5,20], [8, 3, 7], [1, 2]]
----------------------------

"""