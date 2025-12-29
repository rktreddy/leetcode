#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#

# @lc code=start
class Solution:
    # def pivotIndex(self, nums: List[int]) -> int:
    #     """ Approach #1: Prefix Sum [Accepted] T:O(N), S:O(1) """
    #     S = sum(nums)
    #     leftsum = 0
    #     for i, x in enumerate(nums):
    #         if leftsum == (S - leftsum - x):
    #             return i
    #         leftsum += x
    #     return -1
    
    # def pivotIndex(self, nums: List[int]) -> int:
    #     global_sum = sum(nums)
    #     left_sum = 0
    #     for i, num in enumerate(nums):
    #         if global_sum - 2 * left_sum == num:
    #             return i
    #         left_sum += num
    #     return -1
    
    def pivotIndex(self, nums: List[int]) -> int:
        global_sum = sum(nums)
        left_sum = 0
        for i, num in enumerate(nums):
            if global_sum - 2 * left_sum == num:
                return i
            left_sum += num
        return -1
        
# @lc code=end
""" carcking faang: Prefix Sum [Accepted] T:O(N), S:O(1) """

