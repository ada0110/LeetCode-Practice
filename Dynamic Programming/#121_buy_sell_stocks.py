from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ''' M1: O(n)'''
        # calculate max profit while traversing array
        # n = len(prices)
        # max_profit = [0] * n
        # for i in range(len(prices)):
        #     max_profit[i] = max(prices[i:]) - prices[i] 
        # print(max_profit)
        # print(max(max_profit)) 

        '''M2: O(n)'''
        # here rather than creating separate maxx_profit arr
        # we keep track of min price and then subtract from upcoming values and keep the maximum
        profit = 0
        buy_price = float("inf")

        for price in prices:
            if price < buy_price:
                buy_price = price
            else:
                profit = max(profit, price-buy_price)
        return profit




              

s = Solution()
ans = s.maxProfit( [900,510,174,329,873,382,279,855,396,810,322,192,442])
    #[100, 180, 260, 310, 40, 535, 695])#[3, 2, 6, 5, 0, 3]) #[3,5,2]) #[2,4,1]) #[7,6,4,3,1]) # [7,8,1,5,3,6,4])
print(ans)