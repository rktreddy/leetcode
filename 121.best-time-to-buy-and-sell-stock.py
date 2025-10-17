#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    #     # Greedy approach
    #     max_profit = 0
    #     min_value = prices[0]

    #     for price in prices[1:]:
    #         if min_value < price:
    #             max_profit = max(max_profit, price - min_value)
    #         else:
    #             min_value = price
    #     return max_profit
    
    # def maxProfit(self, prices: List[int]) -> int:
    #     """ Approach 1: Brute Force O(n^2), O(1) """
    #     max_profit = 0
    #     for i in range(len(prices) - 1):
    #         for j in range(i + 1, len(prices)):
    #             profit = prices[j] - prices[i]
    #             if profit > max_profit:
    #                 max_profit = profit
    #     return max_profit
    
    # def maxProfit(self, prices: List[int]) -> int:
    #     """ Approach 2: One Pass O(n), O(1)"""
    #     min_price = float("inf")
    #     max_profit = 0
    #     for i in range(len(prices)):
    #         if prices[i] < min_price:
    #             min_price = prices[i]
    #         elif prices[i] - min_price > max_profit:
    #             max_profit = prices[i] - min_price

    #     return max_profit

    # def maxProfit(self, prices: List[int]) -> int:
    #     """ practice: Approach 2: One Pass O(n), O(1)"""
    #     min_price = float('inf')
    #     max_profit = 0
    #     for price in prices:
    #         if price < min_price:
    #             min_price = price
    #         else:
    #             max_profit = max(max_profit, price - min_price)
    #     return max_profit

    def maxProfit(self, prices: List[int]) -> int:
        """ practice: Approach 2: One Pass O(n), O(1)"""
        minprice = float('inf')
        maxprofit = 0
        for price in prices:
            if price < minprice:
                minprice = price
            else:
                maxprofit = max(maxprofit, price - minprice)
        return maxprofit
    
# @lc code=end

