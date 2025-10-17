#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start
class Solution:
    # def sortedSquares(self, nums: List[int]) -> List[int]:
    #     """ Approach 1: Sort O(n log n), o(n) or O(logn) """
    #     return sorted(x*x for x in nums)
    
    # def sortedSquares(self, nums: List[int]) -> List[int]:
    #     """ Approach 2: Two Pointer O(n), o(n) """
    #     n = len(nums)
    #     result = [0] * n
    #     left = 0
    #     right = n - 1
    #     for i in range(n - 1, -1, -1):
    #         if abs(nums[left]) < abs(nums[right]):
    #             square = nums[right]
    #             right -= 1
    #         else:
    #             square = nums[left]
    #             left += 1
    #         result[i] = square * square
    #     return result
    
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """ practice: Approach 2: Two Pointer O(n), o(n) """
        n = len(nums)
        result = [0] * n
        l, r = 0, n - 1
        for i in range(n - 1, -1, -1):
            if abs(nums[l]) < abs(nums[r]):
                sq = nums[r]
                r -= 1
            else:
                sq = nums[l]
                l += 1
            result[i] = sq * sq
        return result
            
# @lc code=end

