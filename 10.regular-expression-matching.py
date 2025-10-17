#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
class Solution(object):
    # def isMatch(self, text: str, pattern: str) -> bool:
    #     """ Approach 1: Recursion O((T+P)*2^(T+P/2)),O((T+P)*2^(T+P/2)) """
    #     if not pattern:
    #         return not text

    #     first_match = bool(text) and pattern[0] in {text[0], "."}

    #     if len(pattern) >= 2 and pattern[1] == "*":
    #         return (
    #             self.isMatch(text, pattern[2:])
    #             or first_match
    #             and self.isMatch(text[1:], pattern)
    #         )
    #     else:
    #         return first_match and self.isMatch(text[1:], pattern[1:])
    
    # def isMatch(self, text: str, pattern: str) -> bool:
    #     """ Approach 2: Dynamic Programming (Top Down) O(TP), O(TP) """
    #     memo = {}

    #     def dp(i: int, j: int) -> bool:
    #         if (i, j) not in memo:
    #             if j == len(pattern):
    #                 ans = i == len(text)
    #             else:
    #                 first_match = i < len(text) and pattern[j] in {text[i], "."}
    #                 if j + 1 < len(pattern) and pattern[j + 1] == "*":
    #                     ans = dp(i, j + 2) or first_match and dp(i + 1, j)
    #                 else:
    #                     ans = first_match and dp(i + 1, j + 1)

    #             memo[i, j] = ans
    #         return memo[i, j]

    #     return dp(0, 0)

    def isMatch(self, text: str, pattern: str) -> bool:
        """ Approach 2: Dynamic Programming (Bottom Up) O(TP), O(TP) """
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]

        dp[-1][-1] = True
        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):
                first_match = i < len(text) and pattern[j] in {text[i], "."}
                if j + 1 < len(pattern) and pattern[j + 1] == "*":
                    dp[i][j] = dp[i][j + 2] or first_match and dp[i + 1][j]
                else:
                    dp[i][j] = first_match and dp[i + 1][j + 1]

        return dp[0][0]
    
# @lc code=end

