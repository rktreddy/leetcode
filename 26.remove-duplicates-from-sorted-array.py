#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    # def removeDuplicates(self, nums: List[int]) -> int:
    #     """ Approach 1: Two indexes approach O(N), O(1) """
    #     size = len(nums)
    #     insertIndex = 1
    #     for i in range(1, size):
    #         if nums[i - 1] != nums[i]:
    #             nums[insertIndex] = nums[i]
    #             insertIndex += 1
    #     return insertIndex
    
    def removeDuplicates(self, nums: List[int]) -> int:
        """ practice: Approach 1: Two indexes approach O(N), O(1) """
        n = len(nums)
        insertIndex = 1
        for i in range(1, n):
            if nums[i - 1] != nums[i]:
                nums[insertIndex] = nums[i]
                insertIndex += 1
        return insertIndex
            
# @lc code=end

