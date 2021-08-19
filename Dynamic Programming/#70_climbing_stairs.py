class Solution:
    def climbStairs(self, n: int) -> int:
        # handling base cases
        if n==1:
            return 1
        # we begin the steps from 1 so to store steps required for nth stair
        # we need arr of size n+1
        # for n=5, stairs:  0 1 2 3 4 (0 to 4 => 5 stairs)
        #    steps needed:  0 1 2 3 5 8 

        # or simple the step indexing/counting begins from 1 
        dp = [0] * (n+1)

        # defining base cases
        # no of ways to reach step 1
        dp[1] = 1

        # no of ways to reach step 2
        dp[2] = 2
        print(dp)

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
            print(dp)

        return dp[n]

s = Solution()
ans = s.climbStairs(5)#2)
print("ans:", ans)