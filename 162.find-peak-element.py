#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
class Solution:
    # def findPeakElement(self, nums: List[int]) -> int:
    #     """ Approach 1: Linear Scan O(n), O(1) """
    #     for i in range(len(nums) - 1):
    #         if nums[i] > nums[i + 1]:
    #             return i
    #     return len(nums) - 1
    
    # def findPeakElement(self, nums: List[int]) -> int:
    #     """ Approach 2: Recursive Binary Search O(log2(n)), O(log2(n)) """
    #     return self.search(nums, 0, len(nums) - 1)

    # def search(self, nums: List[int], l: int, r: int) -> int:
    #     if l == r:
    #         return l
    #     mid = (l + r) // 2
    #     if nums[mid] > nums[mid + 1]:
    #         return self.search(nums, l, mid)
    #     return self.search(nums, mid + 1, r)
        
    # def findPeakElement(self, nums: List[int]) -> int:
    #     """ Approach 3: Iterative Binary Search O(log2(n)), O(1) """
    #     l = 0
    #     r = len(nums) - 1
    #     while l < r:
    #         mid = (l + r) // 2
    #         if nums[mid] > nums[mid + 1]:
    #             r = mid
    #         else:
    #             l = mid + 1
    #     return l
    
    def findPeakElement(self, nums: List[int]) -> int:
        """ practice: Approach 3: Iterative Binary Search O(log2(n)), O(1) """
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return l
    
# @lc code=end

