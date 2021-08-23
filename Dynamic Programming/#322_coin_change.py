'''
You are given an integer array coins representing coins of different denominations 
and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1
'''


# coins: [1,2,5] 
# amount = 11
# min coins ==> to achieve amount
# 5 + 5 + 1 ==> 11 ==> 3 coins

# for each amount will store the min coins needed and then move to target amount

	# Amount	        0	1	2	3	4	5	6	7	8	9	10	11
	# Min coins needed 	0	1	1	2	2	1	2	2	3	3	2	3
	# to reach amount




from typing import List
from typing_extensions import IntVar
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount <= 0:
            return 0
        if min(coins) > amount:
            return -1
        
        INT_MAX = 1 << 32
        dp = [INT_MAX] * (amount+1)
        dp[0] = 0

        # counting min coins for each amount from 1 to target amount
        for i in range(1, amount+1):
            for coin in coins:
                # check if current coin is smaller than or equal to curr amount i 
                if  coin <= i:
                    dp[i] = min(dp[i-coin]+1, dp[i])
        
        return dp[amount] if dp[amount] != INT_MAX else -1

        



s = Solution()
ans = s.coinChange([1,2,5], 11)  
print(ans)
