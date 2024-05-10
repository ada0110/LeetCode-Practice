'''
You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints 
of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container,
such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

'''
from typing import List

class Solution:
    
    def maxArea_v1(self, height: List[int]) -> int:
        max_area = 0
        
        for i in range(len(height)):
            l = i
            r = len(height) - 1
            
            while (l < r):
                length = r - l
                print(f"\nlength:{length}\nheight[l]:{height[l]}\nheight[r]: {height[r]}")
                if height[l] < height[r]:
                    water = length * height[l]
                    print("water when height[l] < height[r]:", water)
                    l += 1
                
                # elif height[l] >= height[r]:
                #     water = length * height[r]
                #     print("water when height[l] > height[r]:", water)
                #     r -= 1
                else:
                    water = length * height[r]
                    print("water when height[l] > height[r]:", water)
                    r -= 1
                    
            
                if water >= max_area:
                    max_area = water
                    print("max_area:", max_area)
                    
        return max_area

    
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l = 0
        r = len(height) - 1
        
        while (l < r):
            length = r - l
            current_area = min(height[l], height[r])* length
            max_area = max(current_area, max_area)
        
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                            
        return max_area
    
    
s = Solution()
ans = s.maxArea(height = [1,2,4])
print(ans)