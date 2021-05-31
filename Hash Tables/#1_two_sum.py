'''
Given an array of integers nums and an integer target, return indices of the two numbers 
such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order. 
'''

from typing import List 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # creating an empty map to store the previously seen values along with their indexes
        # keys--> element, values --> index
        m = {}
        for i in range(len(nums)):

            # finding out the second number by subtracting from target
            goal = target - nums[i]
            
            # if that number is present in map, return its index and current elements index (i)
            if goal in m:
                return [m[goal], i]
            
            # if num not in goal then save that num as key into map and its value as index i
            m[nums[i]] = i


s = Solution()
ans = s.twoSum([3,6,12,14], 15)
print(ans)
