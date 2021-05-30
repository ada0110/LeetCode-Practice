'''Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.

Could you implement a solution using only O(1) extra space complexity 
and O(n) runtime complexity?'''

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        intended_sum = (n*(n+1)) // 2
        curr_sum = sum(nums)
        return int(intended_sum - curr_sum)



s = Solution()
ans = s.missingNumber([1, 0, 3])
print("Missing number is:", ans)

