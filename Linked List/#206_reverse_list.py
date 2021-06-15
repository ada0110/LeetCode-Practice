
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        # while (curr is not None):
        while(curr):
            next_ = curr.next  # next node
            curr.next = prev   # reverse 
            prev = curr        # make prev as curr
            curr = next_       # make curr as next

        head = prev

        return head


s = Solution()

# creating nodes
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)

# creating links
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

ll = s.reverseList(n1)

while(ll):
    print(ll.val)
    ll = ll.next

        