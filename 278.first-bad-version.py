#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    # def firstBadVersion(self, n: int) -> int:
    #     """ Binary search: O(log n), O(1) """
    #     left, right = 1, n
    #     while left < right:
    #         mid = (left + right) // 2
    #         if isBadVersion(mid):
    #             right = mid
    #         else:
    #             left = mid + 1
    #     return left
    
    def firstBadVersion(self, n: int) -> int:
        """ practice: Binary search: O(log n), O(1) """
        l, r = 1, n
        while l < r:
            mid = (l + r) // 2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
        return l
        
# @lc code=end

