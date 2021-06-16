'''
Given the head of a singly linked list, group all the nodes with odd indices together
 followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

 
Example 1:
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]
'''
# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if (not head):
            return
            
        odd = head
        even = odd.next
        evenList = even

        while(even and even.next):
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = evenList

        return head




s = Solution()

# creating nodes
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

ll = s.oddEvenList(n1)
        
while(ll):
    print(ll.val)
    ll = ll.next
