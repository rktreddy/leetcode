#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution:
    # def removeDuplicates(self, nums: List[int]) -> int:
    #     """ Approach 1: Popping Unwanted Duplicates: Time O(N) to O(n^2), space O(1)"""
    #     if not nums:
    #         return 0
        
    #     i = 1
    #     count = 1

    #     while i < len(nums):
    #         if nums[i] == nums[i - 1]:
    #             count += 1
    #             if count > 2:
    #                 nums.pop(i)
    #                 i -= 1
    #                 count -= 1
    #         else:
    #             count = 1
    #         i += 1

    #     return len(nums)


    def removeDuplicates(self, nums: List[int]) -> int:
        """ Approach 2: Overwriting unwanted duplicates O(N), O(1) """
        if not nums:
            return 0
        
        i = 1
        j = 1
        count = 1

        while i < len(nums):
            if nums[i] == nums[i - 1]:
                count += 1
                if count > 2:
                    i += 1
                    continue
            else:
                count = 1
            nums[j] = nums[i]
            j += 1
            i += 1
        del nums[j:]
        return len(nums)



        
# @lc code=end

