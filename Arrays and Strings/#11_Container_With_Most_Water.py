from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # defining left and right pointers
        l = 0
        r = len(height) - 1
        max_area = 0

        while l < r:
            max_area = max(max_area, min(height[r],height[l])*(r-l))

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area

s = Solution()
ans = s.maxArea([1,8,6,2,5,4,8,3,7]) 
print(ans)


# test cases

# [1,8,6,2,5,4,8,3,7]
# [4,8,9,1,2,3]