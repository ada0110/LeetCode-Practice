'''Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Ex:
Input: nums = [4,1,2,1,2]
Output: 4
'''

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x = sum(nums)
        y = sum(set(nums))
        ans= 2*y - x
        return ans


s = Solution()
ans = s.singleNumber([4,1,2,1,2,4,5])
print("The single number in array is: ", ans)