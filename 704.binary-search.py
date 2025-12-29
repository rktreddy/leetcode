#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    # def search(self, nums: List[int], target: int) -> int:
    #     # if len(nums) == 0:
    #     #     return -1
    #     left, right = 0, len(nums) - 1
    #     while left <= right:
    #         mid_index = (left + right) // 2
    #         if nums[mid_index] == target:
    #             return mid_index
    #         elif nums[mid_index] < target:
    #             left = mid_index + 1
    #         else:
    #             right = mid_index - 1
    #     return -1

    # def search(self, nums: List[int], target: int) -> int:
    #     """ Iterative biranry search O(logn), O(1) """
    #     if len(nums) == 0:
    #         return -1
        
    #     l, r = 0, len(nums) - 1
    #     while l <= r:
    #         mid = (l + r) // 2
    #         if nums[mid] == target:
    #             return mid
    #         elif nums[mid] < target:
    #             l = mid + 1
    #         else:
    #             r = mid - 1
    #     return -1
    
    def search(self, nums: List[int], target: int) -> int:
        """ Iterative biranry search O(logn), O(1) """
        if len(nums) == 0:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1 

        
# @lc code=end

