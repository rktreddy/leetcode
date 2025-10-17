#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    # def searchRange(self, nums: List[int], target: int) -> List[int]:
    #     """ Approach: Binary Search O(logN), O(1) """

    #     lower_bound = self.findBound(nums, target, True)
    #     if lower_bound == -1:
    #         return [-1, -1]

    #     upper_bound = self.findBound(nums, target, False)

    #     return [lower_bound, upper_bound]

    # def findBound(self, nums: List[int], target: int, isFirst: bool) -> int:

    #     N = len(nums)
    #     begin, end = 0, N - 1
    #     while begin <= end:
    #         mid = int((begin + end) / 2)

    #         if nums[mid] == target:

    #             if isFirst:
    #                 # This means we found our lower bound.
    #                 if mid == begin or nums[mid - 1] < target:
    #                     return mid

    #                 # Search on the left side for the bound.
    #                 end = mid - 1
    #             else:

    #                 # This means we found our upper bound.
    #                 if mid == end or nums[mid + 1] > target:
    #                     return mid

    #                 # Search on the right side for the bound.
    #                 begin = mid + 1

    #         elif nums[mid] > target:
    #             end = mid - 1
    #         else:
    #             begin = mid + 1

    #     return -1
    
    # def searchRange(self, nums: List[int], target: int) -> List[int]:
    #     """Approach: Binary Search O(logN), O(1)"""

    #     def find_first(nums, target):
    #         left, right = 0, len(nums) - 1
    #         while left <= right:
    #             mid = left + (right - left) // 2
    #             if nums[mid] < target:
    #                 left = mid + 1
    #             else:
    #                 right = mid - 1
    #         # Ensure left is within bounds and matches the target
    #         if left < len(nums) and nums[left] == target:
    #             return left
    #         return -1

    #     def find_last(nums, target):
    #         left, right = 0, len(nums) - 1
    #         while left <= right:
    #             mid = left + (right - left) // 2
    #             if nums[mid] <= target:
    #                 left = mid + 1
    #             else:
    #                 right = mid - 1
    #         # Ensure right is within bounds and matches the target
    #         if right >= 0 and nums[right] == target:
    #             return right
    #         return -1

    #     if not nums:  # Handle empty input array
    #         return [-1, -1]

    #     first_index = find_first(nums, target)
    #     if first_index == -1:  # Early return if the target isn't found
    #         return [-1, -1]
    #     last_index = find_last(nums, target)

    #     return [first_index, last_index]

    #  def searchRange(self, nums: List[int], target: int) -> List[int]:
    #     """Approach: Binary Search O(logN), O(1)"""
    #     def find_first(nums, target):
    #         l, r = 0, len(nums) - 1            
    #         while l <= r:
    #             mid = (l + r) // 2
    #             if nums[mid] < target:
    #                 l = mid + 1
    #             else:
    #                 r = mid - 1
    #         if l < len(nums) and nums[l] == target:
    #             return l
    #         return -1
               
    #     def find_last(nums, target):
    #         l, r, = 0, len(nums) - 1
    #         while l <= r:
    #             mid = (l + r) // 2
    #             if nums[mid] <= target:
    #                 l = mid + 1
    #             else:
    #                 r = mid - 1
    #         if r >= 0 and nums[r] == target:
    #             return r 
    #         return -1
        
    #     start = find_first(nums, target)
    #     last = find_last(nums, target)

    #     return [start, last]
     
     def searchRange(self, nums: List[int], target: int) -> List[int]:
        """ practce: simplified: Approach: Binary Search O(logN), O(1) """
        
        def find_first(nums, target):
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            if l < len(nums) and nums[l] == target:
                return l
            return -1
        
        def find_last(nums, target):
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid - 1
            if r >= 0 and nums[r] == target:
                return r
            return -1
        
        first, last = find_first(nums, target), find_last(nums, target)
        return [first, last]
                
        

# class Solution:
#     def searchRange(self, nums: list[int], target: int) -> list[int]:
#         l = bisect_left(nums, target)
#         if l == len(nums) or nums[l] != target:
#             return -1, -1
#         r = bisect_right(nums, target) - 1
#         return l, r
        
# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         l = bisect_left(nums, target)
#         r = bisect_left(nums, target + 1)
#         return [-1, -1] if l == r else [l, r - 1]
    
# from bisect import bisect_left
# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         # Find the leftmost (first) index where `target` should be inserted.
#         left_index = bisect_left(nums, target)
      
#         # Find the rightmost index by searching for the position where `target + 1` should be inserted.
#         # This will give us one position past the last occurrence of `target`.
#         right_index = bisect_left(nums, target + 1)
      
#         # If `left_index` and `right_index` are the same, the target is not present in the list.
#         if left_index == right_index:
#             return [-1, -1]  # Target not found, return [-1, -1].
#         else:
#             # Return the starting and ending index of `target`.
#             # Since `right_index` gives us one position past the last occurrence,
#             # we subtract one to get the actual right boundary.
#             return [left_index, right_index - 1]
        
# @lc code=end

