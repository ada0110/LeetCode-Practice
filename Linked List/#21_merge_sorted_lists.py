# Merge two sorted linked lists and return it as a sorted list. 
# The list should be made by splicing together the nodes of the first two lists.


from typing import List

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # creating head
        cur = ListNode(0)
        ans = cur

        while (l1 and l2):
            if(l1.val > l2.val):
                cur.next = l2
                l2 = l2.next
            else:
                cur.next = l1
                l1 = l1.next
            
            # cur node should always point to last node of cur list
            cur = cur.next

        
        # if l1 has some elements left and l2 is empty then add those elems in cur list
        while(l1):
            cur.next = l1
            l1 = l1.next
            cur = cur.next
        
        # if l2 has some elements left and l1 is empty then add those elems in cur list
        while(l2):
            cur.next = l2
            l2 = l2.next
            cur = cur.next

        # returning ans.next cz we created a dummy node at ans and the actual list starts from ans.next
        return ans.next


s = Solution()
# now we have to create the lists to be merged
# l1 = 1 -> 2 -> 4
l1_1 = ListNode(1)
l1_2 = ListNode(2)
l1_3 = ListNode(3)

l1_1.next = l1_2
l1_2.next = l1_3

# l2 = 1 -> 3 -> 4
l2_1 = ListNode(1)
l2_3 = ListNode(3)
l2_4 = ListNode(4)

l2_1.next = l2_3
l2_3.next = l2_4

# calling the function with heads of two lists
answer = s.mergeTwoLists(l1_1, l2_1)

# printing the address of head node of the sorted list
print(answer)

# printing the values
while (answer != None):
    print(answer.val)
    answer = answer.next 





        
