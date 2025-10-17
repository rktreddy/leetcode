#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    # def removeElement(self, nums: List[int], val: int) -> int:
    #     """ my initial attempt """
    #     left, right = 0, len(nums) - 1
    #     count = 0
    #     while left < right:
    #         if nums[left] == val:
    #             count += 1
    #             if nums[right] == val:
    #                 count += 1
    #                 right -= 1
    #             nums[left], nums[right] = nums[right], nums[left]
    #             left += 1
    #             right -= 1
    #     return nums
    

    # def removeElement(self, nums: List[int], val: int) -> int:
    #     """ Approach 1: Two Pointers O(n), O(1) """
    #     i = 0
    #     for j in range(len(nums)):
    #         if nums[j] != val:
    #             nums[i] = nums[j]
    #             i += 1
    #     return i 
    
    # def removeElement(self, nums: List[int], val: int) -> int:
    #     """ Approach 2: Two Pointers - when elements to remove are rare O(n), O(1) """
    #     i = 0
    #     n = len(nums)
    #     while i < n:
    #         if nums[i] == val:
    #             nums[i] = nums[n - 1]
    #             n -= 1
    #         else:
    #             i += 1
    #     return n
    
    def removeElement(self, nums: List[int], val: int) -> int:
        """ practice: Approach 2: Two Pointers - when elements to remove are rare O(n), O(1) """
        i, j = 0, len(nums)
        while i < j:
            if nums[i] == val:
                nums[i] = nums[j - 1]
                j -= 1
            else:
                i += 1
        return j

# @lc code=end

