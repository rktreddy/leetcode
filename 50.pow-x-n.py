#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    # def binaryExp(self, x: float, n: int) -> float:
    #     """ Approach 1: Binary Exponentiation (Recursive) O(logN), O(logN) """
    #     # Base case, to stop recursive calls.
    #     if n == 0:
    #         return 1
        
    #     # Handle case where, n < 0.
    #     if n < 0:
    #         return 1.0 / self.binaryExp(x, -1 * n)
        
    #     # Perform Binary Exponentiation.
    #     # If 'n' is odd we perform Binary Exponentiation on 'n - 1' and multiply result with 'x'.
    #     if n % 2 == 1:
    #         return x * self.binaryExp(x * x, (n - 1) // 2)
    #     # Otherwise we calculate result by performing Binary Exponentiation on 'n'.
    #     else:
    #         return self.binaryExp(x * x, n // 2)
        
    # def myPow(self, x: float, n: int) -> float:
    #     return self.binaryExp(x, n)
    
    # def binaryExp(self, x: float, n: int) -> float:    
    #     """ Approach 2: Binary Exponentiation (Iterative) O(log N), O(1) """
    #     # Base case, to stop recursive calls.
    #     if n == 0:
    #         return 1
        
    #     # Handle case where, n < 0.
    #     if n < 0:
    #         n = -1 * n
    #         x = 1.0 / x
        
    #     # Perform Binary Exponentiation.
    #     result = 1
    #     while n != 0:
    #         # If 'n' is odd we multiply result with 'x' and reduce 'n' by '1'.
    #         if n % 2 == 1:
    #             result *= x
    #             n -= 1
    #         # We square 'x' and reduce 'n' by half, x^n => (x^2)^(n/2).
    #         x *= x
    #         n //= 2
        
    #     return result

    # def myPow(self, x: float, n: int) -> float:
    #     return self.binaryExp(x, n)
    
    # def myPow(self, x: float, n: int) -> float:
    #     """ Neetcode: 2. Binary Exponentiation (Recursive) O(logn), O(logn) """
    #     def helper(x, n):
    #         if x == 0:
    #             return 0
    #         if n == 0:
    #             return 1

    #         res = helper(x * x, n // 2)
    #         return x * res if n % 2 else res

    #     res = helper(x, abs(n))
    #     return res if n >= 0 else 1 / res

    # def myPow(self, x: float, n: int) -> float:
    #     """ Neetcode: 3. Binary Exponentiation (Iterative) O(logn), O(1) """
    #     if x == 0:
    #         return 0
    #     if n == 0:
    #         return 1
        
    #     res = 1
    #     power = abs(n)

    #     while power:
    #         if power % 2 == 1:
    #         # if power & 1:
    #             res *= x
    #         x *= x
    #         power //= 2
    #         # power >>= 1
        
    #     return res if n >= 0 else 1 / res
    

    def myPow(self, x: float, n: int) -> float:
        """ practice: Neetcode: 3. Binary Exponentiation (Iterative) O(logn), O(1) """
        if x == 0:
            return 0
        if n == 0:
            return 1
        
        power = abs(n)
        ans = 1
        while power:
            if power % 2 == 1:
                ans *= x
            x *= x
            power //= 2
        return ans if n >= 0 else 1/ans

# @lc code=end

# res = 1
# power = 10
# x = 2
# it1:
# res = 1
# x = 4
# power = 5
# it2: 
# res = 4
# x = 16
# power = 2
# it3:
# res = 4
# x = 16*16 = 256
# power = 1
# it4:
# res = 4*256 = 1024
# x = 256*256
# power = 0
