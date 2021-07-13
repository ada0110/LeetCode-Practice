'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
'''

from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        n = len(lists)
        print("n:", n)
        
        if n == 0:
            return

        for i in range(n):
            if lists[i] is None:
                del lists[i]
                n -= 1
        
        if n == 1:
            return lists[0]
            
        else:
            L1= lists[0]
            L2 = lists[1]
            merged_list = self.merge2Lists(L1, L2)

        # temp_ll = merged_list
        # self.displayLL(temp_ll, "l0+l1")

            for i in range(2,n):
                print("i:", i)
                merged_list = self.merge2Lists(merged_list, lists[i])
                # temp_ll = merged_list
            return merged_list
        
    def merge2Lists(self, L1, L2):
        curr = ListNode(0)
        # L1 = ListNode(l1) 
        # L2 = ListNode(l2)

        ans = curr
        while(L1 and L2):
            # print(str(L1.val) + " " + str(L2.val))
            if L1.val > L2.val:
                curr.next = L2
                L2 = L2.next
            else:
                curr.next = L1
                L1 = L1.next

            curr = curr.next
            
        while(L1):
            curr.next = L1
            L1 = L1.next
            curr = curr.next
        
        while(L2):
            curr.next = L2
            L2 = L2.next
            curr = curr.next
        return ans.next

    


s = Solution()
# creating ll1

# creating nodes
# l1_1 = ListNode(1)
# l1_2 = ListNode(4)
# l1_3 = ListNode(5)

# l1_1.next = l1_2
# l1_2.next = l1_3

# l2_1 = ListNode(1)
# l2_2 = ListNode(3)
# l2_3 = ListNode(4)

# l2_1.next = l2_2
# l2_2.next = l2_3

# l3_1 = ListNode(2)
# l3_2 = ListNode(6)

# l3_1.next = l3_2

# lists = [l1_1, l2_1, l3_1]

lists = [[1], [1]]

ll = s.mergeKLists(lists)

while(ll):
    print(ll.val)
    ll = ll.next