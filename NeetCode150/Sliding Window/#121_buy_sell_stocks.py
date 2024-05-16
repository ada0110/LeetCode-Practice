'''
121. Best Time to Buy and Sell Stock
Easy
Topics
Companies
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
'''
from typing import List
class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    def maxProfit(self, prices):
        l = 0
        r = l + 1
        max_profit = 0
        while (r < len(prices)):        
            # check if its profitable 
            if prices[l] < prices[r]:
                curr_profit = prices[r] - prices[l]
                print("curr_profit:", curr_profit)
                max_profit = max(curr_profit, max_profit) 
                # r += 1
            else:
                l = r
            r += 1
                
        return max_profit
    
    def maxProfit_v2(self, prices: List[int]) -> int:
        l = 0
        r = l + 1
        max_profit = 0
        while (r < len(prices)):
            curr_profit = prices[r] - prices[l]
            print(f"l:{l}\tr:{r}")
            print("curr_profit:", curr_profit)
            if curr_profit < 0:
                l += 1
                r += 1
                print(f"\tl:{l}\tr:{r}")
            elif curr_profit > max_profit:
                max_profit = curr_profit
                print("max_profit:", max_profit)
                r += 1
        return max_profit
    
s = Solution()
ans = s.maxProfit(prices = [1,2,4])
print(ans)



