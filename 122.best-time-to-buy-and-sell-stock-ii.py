#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    #     """ Approach 1: Brute Force O(n^2), O(n): Time limit exceeded """
    #     return self.calculate(prices, 0)

    # def calculate(self, prices, s):
    #     if s >= len(prices):
    #         return 0
    #     max = 0
    #     for start in range(s, len(prices)):
    #         maxprofit = 0
    #         for i in range(start + 1, len(prices)):
    #             if prices[start] < prices[i]:
    #                 profit = (
    #                     self.calculate(prices, i + 1)
    #                     + prices[i]
    #                     - prices[start]
    #                 )
    #                 if profit > maxprofit:
    #                     maxprofit = profit
    #         if maxprofit > max:
    #             max = maxprofit
    #     return max
    
    # def maxProfit(self, prices: List[int]) -> int:
    #     """ Approach 2: Peak Valley Approach O(n), O(1) """
    #     i = 0
    #     valley = prices[0]
    #     peak = prices[0]
    #     maxprofit = 0
    #     while i < len(prices) - 1:
    #         while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
    #             i += 1
    #         valley = prices[i]
    #         while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
    #             i += 1
    #         peak = prices[i]
    #         maxprofit += peak - valley
    #     return maxprofit
    
    # def maxProfit(self, prices: List[int]) -> int:
    #     """ practice: Approach 2: Peak Valley Approach O(n), O(1) """
    #     i = 0
    #     valley = prices[0]
    #     peak = prices[0]
    #     maxprofit = 0
    #     while i < len(prices) - 1:
    #         while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
    #             i += 1
    #         valley = prices[i]
    #         while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
    #             i += 1
    #         peak = prices[i]
    #         maxprofit += peak - valley
    #     return maxprofit

    def maxProfit(self, prices: List[int]) -> int:
        """ Meetcode Approach 3: Greedy O(n), O(1) """
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += (prices[i] - prices[i - 1])

        return profit


        
# @lc code=end

