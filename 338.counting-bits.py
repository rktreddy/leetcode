#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
class Solution:
    # def countBits(self, n: int) -> List[int]:
    #     """ Approach 1: Pop Count O(n log n), O(1) """
    #     def pop_count(x: int) -> int:
    #         count = 0
    #         while x != 0:
    #             x &= x - 1 # zeroing out the least significant nonzero bit
    #             count += 1
    #         return count
            
    #     ans = [0] * (n + 1)
    #     for x in range(n + 1):
    #         ans[x] = pop_count(x)
    
    #     return ans                                

    # def countBits(self, n: int) -> List[int]:
    #     """ Approach 2: DP + Most Significant Bit O(n), O(1) """
    #     ans = [0] * (n + 1)
    #     x = 0
    #     b = 1
        
    #     # [0, b) is calculated
    #     while b <= n:
    #         # generate [b, 2b) or [b, n) from [0, b)
    #         while x < b and x + b <= n:
    #             ans[x + b] = ans[x] + 1
    #             x += 1
    #         x = 0 # reset x
    #         b <<= 1 # b = 2b
            
    #     return ans               

    # def countBits(self, n: int) -> List[int]:
    #     """ Approach 3: DP + Least Significant Bit O(n), O(1) """
    #     ans = [0] * (n + 1)
    #     for x in range(1, n + 1):
    #         # x // 2 is x >> 1 and x % 2 is x & 1
    #         ans[x] = ans[x >> 1] + (x & 1) 
    #     return ans     
    
    def countBits(self, n: int) -> List[int]:
        """ Approach 4: DP + Last Set Bit O(n), O(1) """
        ans = [0] * (n + 1)
        for x in range(1, n + 1):
            ans[x] = ans[x & (x - 1)] + 1
        return ans 
    

# @lc code=end

