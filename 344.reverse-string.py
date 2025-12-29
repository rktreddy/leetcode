#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#

# @lc code=start
class Solution:
    # def reverseString(self, s: List[str]) -> None:
    #     """
    #     Do not return anything, modify s in-place instead.
    #     """
    #     left, right = 0, len(s) - 1

    #     while left < right:
    #         s[left], s[right] = s[right], s[left]
    #         left += 1
    #         right -= 1

    def reverseString(self, s: List[str]) -> None:
        """ Practice """
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        

        
# @lc code=end

