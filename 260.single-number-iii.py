#
# @lc app=leetcode id=260 lang=python3
#
# [260] Single Number III
#

# @lc code=start
from collections import Counter
class Solution:
    # def singleNumber(self, nums: List[int]) -> List[int]:
    #     """ Approach 1: Hashmap O(N), O(N) """

    #     hashmap = Counter(nums)
    #     return [x for x in hashmap if hashmap[x] == 1]
    
    def singleNumber(self, nums: List[int]) -> List[int]:
        """ Approach 2: Two bitmasks O(N), O(1) """

        # difference between two numbers (x and y) which were seen only once
        bitmask = 0
        for num in nums:
            bitmask ^= num
        
        # rightmost 1-bit diff between x and y
        diff = bitmask & (-bitmask)
        
        x = 0
        for num in nums:
            # bitmask which will contain only x
            if num & diff:
                x ^= num
        
        return [x, bitmask^x]
        
# @lc code=end

