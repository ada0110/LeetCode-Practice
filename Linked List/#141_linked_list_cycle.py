'''
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached 
again by continuously following the next pointer. Internally, pos is used to denote 
the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
'''

from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class to detect the cycle in ll 
#  using hare and turtle algorithm
class Solution:
    def hasCycle(self, head: ListNode) -> bool:

        hare = head
        turtle = head

        while(turtle and hare and hare.next):
            hare = hare.next.next
            turtle = turtle.next

            if (hare == turtle):
                return True

        return False

    

s = Solution()

# creating the nodes 
n1 = ListNode(3)
n2 = ListNode(2)
n3 = ListNode(0)
n4 = ListNode(-4)

# connecting the nodes into a list
n1.next = n2
n2.next = n3
n3.next = n4

# 3 => 2 => 0 => -4, -4 is connected back to 2 so -4 => 2
# cycle
n4.next = n2

ans = s.hasCycle(n1)
print(ans)
