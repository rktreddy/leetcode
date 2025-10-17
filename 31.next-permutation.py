#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
class Solution:
    # def nextPermutation(self, nums: List[int]) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     """ Approach 1: Brute Force O(n!), O(n) """

    #     """ Approach 2: Single Pass Approach O(n), O(1) """
        
    #     i = len(nums) - 2
    #     while i >= 0 and nums[i + 1] <= nums[i]:
    #         i -= 1
        
    #     if i >= 0:
    #         j = len(nums) - 1
    #         while nums[j] <= nums[i]:
    #             j -= 1
    #         self.swap(nums, i, j)
    #     self.reverse(nums, i + 1)

    # def reverse(self, nums, start):
    #     i, j = start, len(nums) - 1
    #     while i < j:
    #         self.swap(nums, i, j)
    #         i += 1
    #         j -= 1

    # def swap(self, nums, i, j):
    #     temp = nums[i]
    #     nums[i] = nums[j]
    #     nums[j] = temp

    # def nextPermutation(self, nums: List[int]) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     """ practice: Approach 2: Single Pass Approach O(n), O(1) """

    #     i = len(nums) - 2
    #     while i >= 0 and nums[i + 1] <= nums[i]:
    #         i -= 1

    #     if i >= 0:
    #         j = len(nums) - 1
    #         while nums[j] <= nums[i]:
    #             j -= 1
    #         self.swap(nums, i, j)
    #     self.reverse(nums, i + 1)
        
    # def reverse(self, nums, start):
    #     i, j = start, len(nums) - 1
    #     while i < j:
    #         self.swap(nums, i, j)
    #         i += 1
    #         j -= 1

    # def swap(self, nums, i, j):
    #     nums[i], nums[j] = nums[j], nums[i]
    
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """ practice: Approach 2: Single Pass Approach O(n), O(1) """
        i = len(nums) - 2
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1

        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            self.swap(nums, i, j)
        self.reverse(nums, i + 1)


    def reverse(self, nums, start):
        i, j = start, len(nums) - 1
        while i < j:
            self.swap(nums, i, j)
            i += 1
            j -= 1

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]
        
# @lc code=end

