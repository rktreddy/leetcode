#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
import functools
class Solution:
    # def reverseBits(self, n: int) -> int:
    #     """ Approach 1: Bit by Bit O(1), O(1) """
    #     ret, power = 0, 31
    #     while n:
    #         ret += (n & 1) << power
    #         n = n >> 1
    #         power -= 1
    #     return ret
    
    # def reverseBits(self, n: int) -> int:
    #     """ Approach 2: Byte by Byte with Memoization """
    #     ret, power = 0, 24
    #     while n:
    #         ret += self.reverseByte(n & 0xFF) << power
    #         n = n >> 8
    #         power -= 8
    #     return ret

    # # memoization with decorator
    # @functools.lru_cache(maxsize=256)
    # def reverseByte(self, byte):
    #     return (byte * 0x0202020202 & 0x010884422010) % 1023
        
    def reverseBits(self, n: int) -> int:
        """ Approach 3: Mask and Shift O(1), O(1) """
        n = (n >> 16) | (n << 16)
        n = ((n & 0xFF00FF00) >> 8) | ((n & 0x00FF00FF) << 8)
        n = ((n & 0xF0F0F0F0) >> 4) | ((n & 0x0F0F0F0F) << 4)
        n = ((n & 0xCCCCCCCC) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xAAAAAAAA) >> 1) | ((n & 0x55555555) << 1)
        return n
    
# @lc code=end

