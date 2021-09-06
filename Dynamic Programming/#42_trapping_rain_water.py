from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        water = 0

        if n < 1:
            return 0
        
        # left and right array to store the maximum height of building from left side and right side respectively
        left = [0] * n
        right = [0] * n

        # at left and right ends the arrays will contain only heights
        left[0] = height[0]
        right[n-1] = height[n-1]

        for i in range(1, n):
            left[i] = max(left[i-1], height[i]) 
        print("left:", left)

        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], height[i]) 
        print("right:", right)

        # water = min(left,right)-height 
        for i in range(n):
            water += min(left[i], right[i]) - height[i]

        return water

# test cases
# [0,1,0,2,1,0,1,3,2,1,2,1]

s = Solution()
ans = s.trap([4,2,0,3,2,5])
print(ans)