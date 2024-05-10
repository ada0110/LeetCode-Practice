'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.


Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
'''
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        
        for i, a in enumerate(nums):
            # don't take the same number again
            if i > 0 and a == nums[i-1]: 
                continue
            
            l = i + 1
            r = len(nums) - 1
            # print("a:", a)
            while (l < r):
                three_sum = a + nums[l] + nums[r]
                print(f"a:{a}, nums[l]:{nums[l]}, nums[r]:{nums[r]}")
                print("three_sum:",three_sum)
                    
                if three_sum < 0:
                    l = l + 1
                elif three_sum > 0:
                    r = r - 1
                else:
                    ans.append([a, nums[l], nums[r]])
                    l += 1
                    
                    while(nums[l] == nums[l-1]) and l < r:
                        l += 1
                    
            print("\n")
        return ans
    
    
s = Solution()
ans = s.threeSum(nums = [-1,0,1,2,-1,-4])
print(ans)
        
        