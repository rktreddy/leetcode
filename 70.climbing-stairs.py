#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:    
    """ Approach 1: Brute Force O(2^n)"""
    # def climbStairs(self, n: int) -> int:
    #     return self.climb_Stairs(0, n)

    # def climb_Stairs(self, i: int, n: int) -> int:
    #     if i > n:
    #         return 0
    #     if i == n:
    #         return 1
    #     return self.climb_Stairs(i + 1, n) + self.climb_Stairs(i + 2, n)
    
    """ Approach 2: Recursion with Memoization: Time O(n), Space: O(n) """
    # def climbStairs(self, n: int) -> int:
    #     memo = [0] * (n + 1)
    #     return self.climb_Stairs(0, n, memo)

    # def climb_Stairs(self, i: int, n: int, memo: List[int]) -> int:
    #     if i > n:
    #         return 0
    #     if i == n:
    #         return 1
    #     if memo[i] > 0:
    #         return memo[i]
        
    #     memo[i] = self.climb_Stairs(i + 1, n, memo) + self.climb_Stairs(i + 2, n, memo)

    #     return memo[i]
    
    """ Approach 3: Dynamic Programming: Time O(n), Space: O(n) """
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [0 for _ in range(n + 1)]
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

    # """ Approach 4: Fibonacci Number: Time O(n), Space: O(1) """
    # def climbStairs(self, n: int) -> int:
    #     if n == 1:
    #         return 1
    #     first = 1
    #     second = 2
    #     for i in range(3, n + 1):
    #         third = first + second
    #         first = second
    #         second = third
    #     return second
    
    """ Approach 5: Binets Method: Time O(log n), Space: O(1) """
    # def climbStairs(self, n: int) -> int:
    #     q = [[1, 1,], [1, 0]]
    #     res = self.pow(q, n)
    #     return res[0][0]
    
    # def pow(self, a: int, n: int) -> int:
    #     ret = [[1, 0], [0 ,1]]
    #     while n > 0:
    #         if (n & 1) == 1:
    #             ret = self.multiply(ret, a)
    #         n >>= 1
    #         a = self.multiply(a, a)
    #     return ret

    # def multiply(self, a: [[int]], b: [[int]]) -> [[int]]:
    #     c = [[0, 0], [0, 0]]
    #     for i in range(2):
    #         for j in range(2):
    #             c[i][j] = a[i][0] * b[0][j] + a[i][1] * b[1][j]
    #     return c
    
    """ Approach 6: Fibonacci Formula: Time O(log n), Space: O(1) """
    # def climbStairs(self, n: int) -> int:
    #     sqrt5 = 5**0.5
    #     phi = (1 + sqrt5) / 2
    #     psi = (1 - sqrt5) / 2
    #     return int((phi ** (n + 1) - psi ** (n + 1)) / sqrt5)

# @lc code=end

