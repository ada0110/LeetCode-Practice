'''
You are given an array people where people[i] is the weight of the ith person, 
and an infinite number of boats where each boat can carry a maximum weight of limit.
Each boat carries at most two people at the same time, provided the sum of the weight 
of those people is at most limit.

Return the minimum number of boats to carry every given person.

Example 1:

Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)
Example 2:

Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)
Example 3:

Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)
'''

from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        min_boats = 0

        people = sorted(people)
        print(people)

        if(sum(people) < limit):
            return 1

        # intialize left and right pointers
        left = 0
        right =len(people)-1
        # print(left,right)

        while(left <= right):
            # when only one person is remaining
            if left == right:
                min_boats += 1
                break 

            if people[left] + people[right] <= limit:
                left += 1
            
            right -= 1
            min_boats += 1
        
        return min_boats

                

s = Solution()
ans = s.numRescueBoats([3,1,7], 7)
print(ans)




# min_boats = 0
# weight = people[0]

# # if weight == limit:
# #     min_boats += 1
# # print("min_boats:", min_boats)

# for i in range(len(people)-2):
#     if people[i] <= limit:
#         min_boats += 1
#         print("min_boats:", min_boats)


#     # elif people[i] < limit or people[i]+people[i+1] > limit:
#     #     min_boats += 1
#     weight -= people[i] + people[i+2]
#     if weight == limit:
#         min_boats += 1

#     print("min_boats_:", min_boats)


            


