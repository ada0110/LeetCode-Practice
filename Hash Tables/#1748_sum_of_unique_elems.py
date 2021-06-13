'''
You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.

Return the sum of all the unique elements of nums.

Example 1:

Input: nums = [1,2,3,2]
Output: 4
Explanation: The unique elements are [1,3], and the sum is 4.
'''

from typing import List

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        m = {}
        ans = 0
        for i in range(len(nums)):
            if nums[i] in m:
                m[nums[i]] += 1
            else:
                m[nums[i]] = 1

        for num in nums:
            if m[num] == 1:
                ans += num

        print("map:", m)
        return ans
        
s = Solution()
ans = s.sumOfUnique( nums = [1,2,3,2])
print(ans)
