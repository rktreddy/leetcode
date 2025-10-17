#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     """ Approach 1 (Brute force) [Time Limit Exceeded] O(S^n), O(n) """
                
    #     n = len(coins)

    #     def dfs(idx, amount):
    #         if amount == 0:
    #             return 0
    #         if idx < n and amount > 0:
    #             min_cost = float('inf')
    #             for x in range(0, amount // coins[idx] + 1):
    #                 res = dfs(idx + 1, amount-x * coins[idx])
    #                 if res != -1:
    #                     min_cost = min(min_cost, res + x)
    #             return -1 if min_cost == float('inf') else min_cost
    #         return -1

    #     return dfs(0, amount)
    # # Time Limit Exceeded

    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     """ Approach 2 (Dynamic programming - Top down) [Accepted] O(S*n), O(S) """

    #     @lru_cache(None)
    #     def dfs(rem):
    #         if rem < 0:
    #             return -1
    #         if rem == 0:
    #             return 0
    #         min_cost = float('inf')
    #         for coin in coins:
    #             res = dfs(rem - coin)
    #             if res != -1:
    #                 min_cost = min(min_cost, res + 1)
    #         return min_cost if min_cost != float('inf') else -1
    #     return dfs(amount)

    def coinChange(self, coins: List[int], amount: int) -> int:
        """ Approach 3 (Dynamic programming - Bottom up) [Accepted] O(S*n), O(S) """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1


# @lc code=end

