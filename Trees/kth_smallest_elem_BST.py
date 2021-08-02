# Definition for a binary tree node.
# Time complexity : O(N) to build a traversal.
# Space complexity : O(N) to keep an inorder traversal.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:

    def __init__(self) -> None:
        self.arr = []

    # inorder traversal 
    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            self.arr.append(node.val)
            self.inorder(node.right)
        
    # inserting nodes in BST
    def insert(self, root, node):
        if root is None:
            node = root
            return 

        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                self.insert(root.right, node)

        else:
            if root.left is None:
                root.left = node
            else:
                self.insert(root.left, node)

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.inorder(root)
        print("inorder traversal", self.arr)
        # print("len of arr:", len(self.arr))
        return self.arr[k-1]





tree = TreeNode(5)
s = Solution()
s.insert(tree, TreeNode(8))
s.insert(tree, TreeNode(10))
s.insert(tree, TreeNode(14))
s.insert(tree, TreeNode(7))

k =int(input("which smallest elem you want to find: "))
ans = s.kthSmallest(tree, k)
print(f"{k}th smallest elem: {ans}")

# example output
# which smallest elem you want to find: 3
# inorder traversal [5, 7, 8, 10, 14]
# 3th smallest elem: 8


        