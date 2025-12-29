#
# @lc app=leetcode id=714 lang=python3
#
# [714] Best Time to Buy and Sell Stock with Transaction Fee
#

# @lc code=start
class Solution:
    # def maxProfit(self, prices: List[int], fee: int) -> int:
    #     """ Approach 1: Dynamic Programming O(n), O(n) """
    #     n = len(prices)
    #     hold, free = [0] * n, [0] * n
        
    #     # In order to hold a stock on day 0, we have no other choice but to buy it for prices[0].
    #     hold[0] = -prices[0]
        
    #     for i in range(1, n):
    #         hold[i] = max(hold[i - 1], free[i - 1] - prices[i])
    #         free[i] = max(free[i - 1], hold[i - 1] + prices[i] - fee)
        
    #     return free[-1]

    # def maxProfit(self, prices: List[int], fee: int) -> int:
    #     """ Approach 2: Space-Optimized Dynamic Programming O(n), O(1) """
    #     n = len(prices)
    #     hold, free = -prices[0], 0
        
    #     for i in range(1, n):
    #         tmp = hold
    #         hold = max(hold, free - prices[i])
    #         free = max(free, tmp + prices[i] - fee)
        
    #     return free
    
    def maxProfit(self, prices: List[int], fee: int) -> int:
        """ practice: Approach 2: Space-Optimized Dynamic Programming O(n), O(1) """
        n = len(prices)
        free, hold = 0, -prices[0]
        for i in range(1, n):
            tmp = hold
            hold = max(hold, free - prices[i])
            free = max(free, tmp + prices[i] - fee)
        return free
    
    
    # # The class Solution contains a method to calculate the maximum profit from trading stocks,
    # # given an array that represents the price of a stock on different days, and a fixed transaction fee.
    # def maxProfit(self, prices: List[int], fee: int) -> int:
    #     """ Algomonster O(n), O(1) """
    #     # Initialize cash and hold variables:
    #     # cash represents the max profit achievable without holding any stock
    #     # hold represents the max profit achievable while holding a stock
    #     cash, hold = 0, -prices[0]
      
    #     # Iterate through the list of prices, starting from the second price
    #     for price in prices[1:]:
    #         # Update cash to the max of itself or the profit from selling a stock at the current price minus the fee
    #         # Update hold to the max of itself or the value of the cash after buying a stock at the current price
    #         cash, hold = max(cash, hold + price - fee), max(hold, cash - price)
      
    #     # The value of cash at the end of iteration will represent the maximum profit achievable
    #     return cash
        
# @lc code=end

