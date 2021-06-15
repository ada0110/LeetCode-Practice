'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit.
 Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

'''

from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode(0)
        ptr = ans
        sum = carry = 0

        while(l1 or l2):
            sum = carry
            if (l1):
                sum += l1.val
                l1 = l1.next

            if(l2):
                sum += l2.val
                l2 = l2.next

            carry = int(sum / 10)
            ptr.next = ListNode(sum % 10)
            ptr = ptr.next

        if(carry == 1):
            ptr.next = ListNode(carry)
        
        return ans.next
        




s = Solution()

# creating nodes
l1_1 = ListNode(2)
l1_2 = ListNode(4)
l1_3 = ListNode(3)

l1_1.next = l1_2
l1_2.next = l1_3

l2_1 = ListNode(5)
l2_2 = ListNode(6)
l2_3 = ListNode(4)

l2_1.next = l2_2
l2_2.next = l2_3

# l3 = ListNode(0)

ll = s.addTwoNumbers(l1_1, l2_1)

# printing the list
while(ll):
    print(ll.val)
    ll = ll.next
