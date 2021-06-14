'''
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

Example 1:
Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

Example 2:
Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
'''

from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sum_ = 0
        max_subarr = 0
        m = {}

        # print("arr: ", nums)
        # calculating prefix sum
        for i in range(len(nums)):
            if nums[i] == 1:
                sum_ += 1
                # print(sum_)
            else:
                sum_ -= 1
                # print(sum_)

            # print("prefix sum:", sum_)

            # if sum == 0 means from start till given index we got equal no of 1s and 0's
            if sum_ == 0:
                max_subarr = i + 1
                # print("max subarr when sum=0:", max_subarr)

            # if sum in present in map it means from given index till the map index it will has equal 1's and 0's and check with with prev max_subarr
            elif sum_ in m:
                max_subarr = max(max_subarr, i - m[sum_])
                # print("max_subarr: ", max_subarr)

            # if sum_ not present in map then add sum and its index
            else:
                 m[sum_] = i

            # print("map: ", m)

        return max_subarr



s = Solution()
ans = s.findMaxLength(nums= [1,1,0,0,0,0,0,1,1,0,1,0,1])
print(ans)