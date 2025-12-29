#
# @lc app=leetcode id=1929 lang=python3
#
# [1929] Concatenation of Array
#

# @lc code=start
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        """ Approach 1: Simple list concatenation O(n), O(n) """
        ans = [0] * 2 * len(nums)
        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i + len(nums)] = nums[i]
        return ans
        
# @lc code=end

