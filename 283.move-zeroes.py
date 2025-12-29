#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    # def moveZeroes(self, nums: List[int]) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     zero = 0
    #     for i in range(len(nums)):
    #         if nums[i] != 0:
    #             nums[i], nums[zero] = nums[zero], nums[i]
    #             zero += 1
        
    # def moveZeroes(self, nums: List[int]) -> None:
    #     """ practice Two pointers O(n), O(1) """
    #     left = 0
    #     for right in range(len(nums)):
    #         if nums[right] != 0:
    #             nums[left], nums[right] = nums[right], nums[left]
    #             left += 1

    def moveZeroes(self, nums: List[int]) -> None:
        """ practice Two pointers O(n), O(1) """
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                
        
# @lc code=end

