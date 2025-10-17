#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#

# @lc code=start
class Solution:
    # def search(self, nums: List[int], target: int) -> bool:
    #     """ Approach 1: Binary Search O(logN) to O(N), O(1) """

    #     n = len(nums)
    #     if n == 0:
    #         return False
    #     end = n - 1
    #     start = 0
    #     while start <= end:
    #         mid = start + (end - start) // 2
    #         if nums[mid] == target:
    #             return True
    #         if not self.isBinarySearchHelpful(nums, start, nums[mid]):
    #             start += 1
    #             continue
    #         # which array does pivot belong to.
    #         pivotArray = self.existsInFirst(nums, start, nums[mid])
    #         # which array does target belong to.
    #         targetArray = self.existsInFirst(nums, start, target)
    #         if pivotArray ^ targetArray:
    #             # if pivot and target exist in different sorted arrays, recall that xor is true
    #             if pivotArray:
    #                 start = mid + 1  # pivot in the first, target in the second
    #             else:
    #                 end = mid - 1  # target in the first, pivot in the second
    #         else:  # if pivot and target exist in same sorted array
    #             if nums[mid] < target:
    #                 start = mid + 1
    #             else:
    #                 end = mid - 1
    #     return False

    # # returns true if we can reduce the search space in current binary search space
    # def isBinarySearchHelpful(self, nums, start, element):
    #     return nums[start] != element

    # # returns true if element exists in first array, false if it exists in second
    # def existsInFirst(self, nums, start, element):
    #     return nums[start] <= element
        
    # def search(self, nums: List[int], target: int) -> bool:
    #     """ Algomonster: binary search"""
    #     # The length of the input array
    #     num_length = len(nums)
      
    #     # Initialize the left and right pointers
    #     left, right = 0, num_length - 1
      
    #     # Binary search with modifications to handle the rotated sorted array
    #     while left < right:
    #         # Calculate the middle index
    #         mid = (left + right) // 2
          
    #         # If the middle element is greater than the rightmost element,
    #         # it means the smallest element is to the right of mid.
    #         if nums[mid] > nums[right]:
    #             # Target is in the left sorted portion
    #             if nums[left] <= target <= nums[mid]:
    #                 right = mid
    #             else:
    #                 left = mid + 1
    #         # If the middle element is less than the rightmost element,
    #         # it means the smallest element is to the left of mid.
    #         elif nums[mid] < nums[right]:
    #             # Target is in the right sorted portion
    #             if nums[mid] < target <= nums[right]:
    #                 left = mid + 1
    #             else:
    #                 right = mid
    #         # If the middle element is equal to the rightmost element,
    #         # we can't determine the smallest element's position,
    #         # so we reduce the search space by one from the right.
    #         else:
    #             right -= 1
      
    #     # Final comparison to see if the target is at the left index
    #     return nums[left] == target
    
    def search(self, nums, target):
        """ Top voted leetcode """
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return True
            while l < mid and nums[l] == nums[mid]: # tricky part
                l += 1
            # the first half is ordered
            if nums[l] <= nums[mid]:
                # target is in the first half
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # the second half is ordered
            else:
                # target is in the second half
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False
    
# @lc code=end

