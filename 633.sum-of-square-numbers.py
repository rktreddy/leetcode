#
# @lc app=leetcode id=633 lang=python3
#
# [633] Sum of Square Numbers
#

# @lc code=start
class Solution:
    # def judgeSquareSum(self, c: int) -> bool:
    #     """ Approach 1: Brute Force O(c), O(1) """
    #     a = 0
    #     while a * a <= c:
    #         b = 0
    #         while b * b <= c:
    #             if a * a + b * b == c:
    #                 return True
    #             b += 1
    #         a += 1
    #     return False
    
    # def judgeSquareSum(self, c: int) -> bool:
    #     """ Approach 2: Better Brute Force O(c), O(1) """
    #     a = 0
    #     while a * a <= c:
    #         b = c - a * a
    #         i = 1
    #         sum = 0
    #         while sum < b:
    #             sum += i
    #             i += 2
    #         if sum == b:
    #             return True
    #         a += 1
    #     return False
    
    # def judgeSquareSum(self, c):
    #     """ Approach 3: Using Sqrt Function O(sqrt(c) log c), O(1) """
    #     a = 0
    #     while a * a <= c:
    #         b = (c - a * a) ** 0.5
    #         if b == int(b):
    #             return True
    #         a += 1
    #     return False
    
    def judgeSquareSum(self, c):
        """ practice: Approach 3: Using Sqrt Function O(sqrt(c) log c), O(1) """
        a = 0
        while a * a <= c:
            b = (c - a * a) ** 0.5
            if b == int(b):
                return True
            a += 1
        return False

    
    # def judgeSquareSum(self, c):
    #     """ Approach 4: Binary Search O(sqrt(c) log c), O(log c) """
    #     def binary_search(s, e, n):
    #         if s > e:
    #             return False
    #         mid = s + (e - s) // 2
    #         if mid * mid == n:
    #             return True
    #         elif mid * mid > n:
    #             return binary_search(s, mid - 1, n)
    #         else:
    #             return binary_search(mid + 1, e, n)

    #     for a in range(
    #         int(c**0.5) + 1
    #     ):  # equivalent to `for (long a = 0; a * a <= c; a++)` in Java
    #         b = c - a * a
    #         if binary_search(0, b, b):
    #             return True
    #     return False
    
    # def judgeSquareSum(self, c: int) -> bool:
    #     """ Approach 5: Fermat Theorem O(sqrt(c)), O(1) """
    #     i = 2
    #     while i * i <= c:
    #         count = 0
    #         while c % i == 0:
    #             count += 1
    #             c //= i
    #         if i % 4 == 3 and count % 2 != 0:
    #             return False
    #         i += 1
    #     return c % 4 != 3
    
    # def judgeSquareSum(self, c: int) -> bool:
    #     """ cracking faang: Using Sqrt Function O(sqrt(c) log c), O(1) """
        
# @lc code=end

