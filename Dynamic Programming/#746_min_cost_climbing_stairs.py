'''
You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
 Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

 

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: Cheapest is: start on cost[1], pay that cost, and go to the top.
Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: Cheapest is: start on cost[0], and only step on 1s, skipping cost[3].

''' 

# min cost to reach ith step is min of the cost required to reach i-1th step and i-2th step 
# min_cost[i] = min((min_cost[i-1]+cost[i-1], min_cost[i-2]+cost[i-2]))

from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost = [0] * (len(cost)+1)

        for i in range(2, len(cost)+1):
            min_cost[i] = min(min_cost[i-1]+cost[i-1], min_cost[i-2]+cost[i-2])

        print(min_cost)
        return min_cost[-1] 




s = Solution()
ans = s.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]) #[10,15,20]) #)
print(ans)