'''
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.
'''

from typing import DefaultDict, List

# solution 1:

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         arr_s = len(nums)
#         set_s = len(set(nums))
# or we can also check for sum of arr and sum of set of arr
        # arr_s = sum(nums)
        # set_s = sum(set(nums))          

        # if arr_s != set_s:
        #     return True

# Solution 2
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # m = {}
        m = DefaultDict(int)
        for num in nums:
            if (m[num]):
            # if num in m:
                return True
            # if not then add that elem as key in map with its count
            m[num] += 1
        return False
            

s = Solution()
ans = s.containsDuplicate([1,2,1,3])
print(ans)