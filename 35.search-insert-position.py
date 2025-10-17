#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """ Approach 1: Binary Search O(log n), O(1) """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1 
        return left 
    
    # def searchInsert(self, nums: List[int], target: int) -> int:
    #      """ leetcode solution"""
    #     left, right = 0, len(nums) - 1
    #     while left <= right:
    #         pivot = (left + right) // 2
    #         if nums[pivot] == target:
    #             return pivot
    #         if target < nums[pivot]:
    #             right = pivot - 1
    #         else:
    #             left = pivot + 1
    #     return left
        
# @lc code=end

