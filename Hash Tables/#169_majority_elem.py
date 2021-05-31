'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.
'''

from typing import List
from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = defaultdict(int)

        # aading the numbers and their count in the map m
        for num in nums:
            # m[num] += 1
            # getting the current elem from map m. If num not found in map
            # consider its count as zero and if found add 1 to the count i.e., value
            m[num] = m.get(num, 0) + 1

        for num in nums:
            # if the count is greater than ⌊n / 2⌋ times then return True
            if (m[num] > len(nums)//2):
                return num
        


s = Solution()
ans = s.majorityElement([5,2,5,3,5,8,5,9,5,5]) #list len = 10 so majority elem must occur more than 5 times
print(ans)