'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
'''
import sys
from typing import List

class Solution:
    # function for dfs traversal
    
    def dfs(self, grid, r, c):
        # marking the cuurrent cell as visited by replacing 1 by 2
        grid[r][c] = '0'
        # checking for invalid conditions
        lst = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]

        # here whenever grid contains value 0 or 2 then we return 0
        for row,col in lst:
            if(row>=0 and row<len(grid) and col>=0 and c<len(grid) and grid[row][col] == '1'):
                self.dfs(grid, row, col)
               
        # # visiting the adjacent nodes in given island by making recursive calls in vertical and horizontal direction
        # self.dfs(grid, r-1, c) # UP
        # self.dfs(grid, r+1, c) # DOWN
        # self.dfs(grid, r, c-1) # LEFT
        # self.dfs(grid, r, c+1) # RIGHT


    # function to count the no. of islands
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        # checking no. of rows and columns
        # print(len(grid), len(grid[0]))
        # print(grid)
        # traverse the grid using two for loops
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    self.dfs(grid, r, c)
                    islands += 1
                    
        # print(grid) 
        return islands

        



s = Solution()
ans = s.numIslands([["1","1","0","0","0"], 
                    ["1","1","0","1","0"],
                    ["0","0","1","0","0"],
                    ["0","0","0","1","1"]])  
print(ans)
          