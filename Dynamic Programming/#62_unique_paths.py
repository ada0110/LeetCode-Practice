class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # intialize 2D dp array with zeros
        dp =[[0 for x in range(n)] for y in range(m)]
        print(dp)

        # intializing first row to 1
        for i in range(n):
            dp[0][i] = 1
        
        # intializing first column to 1
        for i in range(m):
            dp[i][0] = 1

        for i in range(1, m):
            for j in range(1, n): 
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        print(dp)

        return dp[-1][-1]



s = Solution()
ans = s.uniquePaths(m=3, n=7)
print(ans)