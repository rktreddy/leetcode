#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    # def reverse(self, x: int) -> int:
    #     """ Approach 1: Pop and Push Digits & Check before Overflow O(log(x)), O(1) """
    #     sign = [1, -1][x < 0]
    #     rev, x = 0, abs(x)
    #     while x:
    #         x, mod = divmod(x, 10)
    #         rev = rev * 10 + mod
    #         if rev > 2**31 - 1:
    #             return 0
    #     return sign * rev

    # def reverse(self, x: int) -> int:
    #     """ O(logx), O(1)"""
    #     ans = 0
    #     sign = -1 if x < 0 else 1
    #     x *= sign 

    #     while x:
    #         ans = ans * 10 + x % 10
    #         x //= 10
        
    #     return 0 if ans < -2**31 or ans > 2**31 - 1 else ans * sign
    
    def reverse(self, x: int) -> int:
        """ practice: O(logx), O(1) """
        ans = 0
        sign = -1 if x < 0 else 1
        x *= sign

        while x:
            ans = ans * 10 + x % 10
            x //= 10

        return 0 if ans < -2**31 or ans > 2**31 - 1 else ans * sign

        
# @lc code=end

