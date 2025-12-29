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

    # def nextPermutation(self, nums):
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     """ chatgpt: Approach 2: Single Pass Approach O(n), O(1) """
    #     n = len(nums)
        
    #     # 1. Find first decreasing element from the right
    #     i = n - 2
    #     while i >= 0 and nums[i] >= nums[i + 1]:
    #         i -= 1
        
    #     if i >= 0:
    #         # 2. Find number just larger than nums[i] from right side
    #         j = n - 1
    #         while nums[j] <= nums[i]:
    #             j -= 1
    #         nums[i], nums[j] = nums[j], nums[i]
        
    #     # 3. Reverse the suffix
    #     left, right = i + 1, n - 1
    #     while left < right:
    #         nums[left], nums[right] = nums[right], nums[left]
    #         left += 1
    #         right -= 1

    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        """ practice: chatgpt: Approach 2: Single Pass Approach O(n), O(1) """
        n = len(nums)
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        l, r = i + 1, n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
            
    # def swap(self, nums, i, j):
    #     nums[i], nums[j] = nums[j], nums[i]

    #  def nextPermutation(self, nums: List[int]) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     """ cracking faang: Approach 2: Single Pass Approach O(n), O(1) """
    #     pivot = None
    #     for i in range(len(nums) - 1, 0, -1):
    #         if nums[i] > nums[i - 1]:
    #             pivot = i - 1
    #             break
    #         else:
    #             nums.reverse()
    #             return
    #     swap = len(nums) - 1
    #     while nums[swap] <= nums[pivot]:
    #         swap -= 1

    #     nums[pivot], nums[swap] = nums[swap], nums[pivot]
    #     nums[pivot + 1:] = reversed(nums[pivot + 1:])

    #     return

        
# @lc code=end

