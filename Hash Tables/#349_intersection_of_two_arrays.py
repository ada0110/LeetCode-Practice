'''
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must be unique and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
'''

from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # m ={}
        # ans = []
        # nums1 = set(nums1)
        # nums2 = set(nums2)
        print(nums1, nums2)

        # for num in nums1:
        #     m[num] = 1
        # # print(m)
        # for num in nums2:
        #     if num in m.keys():
        #         ans.append(num)
        # return ans

    # or simply
        return list(set(nums1) & set(nums2))

s = Solution()
ans = s.intersection (nums1 = [1,2,2,1], nums2 = [2,2]) #(nums1 = [4,9,5], nums2 = [9,4,9,8,4])
print(ans)