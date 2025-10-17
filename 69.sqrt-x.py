#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
from math import e, log
class Solution:
    # def mySqrt(self, x: int) -> int:
    #     """ Approach 1: Pocket Calculator Algorithm O(1), O(1) """
    #     if x < 2:
    #         return x

    #     left = int(e ** (0.5 * log(x)))
    #     right = left + 1
    #     return left if right * right > x else right
        
    # def mySqrt(self, x: int) -> int:
    #     """ Approach 2: Binary Search O(log N), O(1)"""
    #     if x < 2:
    #         return x

    #     left, right = 2, x // 2

    #     while left <= right:
    #         pivot = left + (right - left) // 2
    #         num = pivot * pivot
    #         if num > x:
    #             right = pivot - 1
    #         elif num < x:
    #             left = pivot + 1
    #         else:
    #             return pivot

    #     return right        
    
    # def mySqrt(self, x: int) -> int:
    #     """ Approach 3: Recursion + Bit Shifts O(log N), O(log N) """
    #     if x < 2:
    #         return x

    #     left = self.mySqrt(x >> 2) << 1
    #     right = left + 1
    #     return left if right * right > x else right
    
    def mySqrt(self, x: int) -> int:
        """Approach 4: Newton's Method O(log N), O(1)"""
        if x < 2:
            return x

        x0 = x
        x1 = (x0 + x / x0) / 2
        while abs(x0 - x1) >= 1:
            x0 = x1
            x1 = (x0 + float(x) / x0) / 2

        return int(x1)
    
# @lc code=end

