from typing import List

class Solution:

    def dfs(self, grid, r, c):
            curr_area = 1
            # marking the cuurrent cell as visited by replacing 1 by 0
            grid[r][c] = 0

            # checking for invalid conditions
            lst = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]

            for r,c in lst:
                if(r>=0 and r<len(grid) and c>=0 and c<len(grid[0]) and grid[r][c] == 1):
                    curr_area += self.dfs(grid, r, c)

            return curr_area


    # function to max area of islands
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        count = 0
        max_area = 0
        # checking no. of rows and columns
        # print(len(grid), len(grid[0]))
        # print(grid)
        # traverse the grid using two for loops
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    count = self.dfs(grid, r, c)
                    if count > max_area:
                        max_area = count
        return max_area

s = Solution()
ans = s.maxAreaOfIsland([ [0,0,1,0,0,0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1,1,1,0,0,0],
                        [0,1,1,0,1,0,0,0,0,0,0,0,0],
                        [0,1,0,0,1,1,0,0,1,0,1,0,0],
                        [0,1,0,0,1,1,0,0,1,1,1,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,0,1,1,1,0,0,0],
                        [0,0,0,0,0,0,0,1,1,0,0,0,0]])
print(ans)
         