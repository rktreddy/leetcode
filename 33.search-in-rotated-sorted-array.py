#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    # def search(self, nums: List[int], target: int) -> int:
    #     """ Approach 1: Find Pivot Index + Binary Search O(log n), O(1) """
    #     n = len(nums)
    #     left, right = 0, n - 1

    #     while left <= right:
    #         mid = (left + right) // 2
    #         if nums[mid] > nums[-1]:
    #             left = mid + 1
    #         else:
    #             right = mid - 1

    #     def binarySearch(left_boundary, right_boundary, target):
    #         left, right = left_boundary, right_boundary
    #         while left <= right:
    #             mid = (left + right) // 2
    #             if nums[mid] == target:
    #                 return mid
    #             elif nums[mid] > target:
    #                 right = mid - 1
    #             else:
    #                 left = mid + 1

    #         return -1
            
    #     if (answer := binarySearch(0, left - 1, target)) != -1:
    #         return answer
        
    #     return binarySearch(left, n - 1, target)

    def search(self, nums: List[int], target: int) -> int:
        """ Approach 1: practice """
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1

        def binarySearch(left, right, target):
            # left, right = left_boundary, right_boundary
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1
        
        answer = binarySearch(0, left - 1, target)
        if answer != -1:
            return answer
        # if (answer := binarySearch(0, left - 1, target)) != -1:
        #     return answer
        
        return binarySearch(left, n - 1, target)


    # def search(self, nums: List[int], target: int) -> int:
    #     """ Approach 2: Find Pivot Index + Binary Search with Shift O(log n), O(1) """
    #     n = len(nums)
    #     left, right = 0, n - 1

    #     # Find the index of the pivot element (the smallest element)
    #     while left <= right:
    #         mid = (left + right) // 2
    #         if nums[mid] > nums[-1]:
    #             left = mid + 1
    #         else:
    #             right = mid - 1

    #     # Shift elements in circular manner, with the pivot element at index 0.
    #     # Then perform a regular binary search
    #     def shiftedBinarySearch(pivot_index, target):
    #         shift = n - pivot_index
    #         left, right = (pivot_index + shift) % n, (
    #             pivot_index - 1 + shift
    #         ) % n

    #         while left <= right:
    #             mid = (left + right) // 2
    #             if nums[(mid - shift) % n] == target:
    #                 return (mid - shift) % n
    #             elif nums[(mid - shift) % n] > target:
    #                 right = mid - 1
    #             else:
    #                 left = mid + 1
    #         return -1

    #     return shiftedBinarySearch(left, target)


        
# @lc code=end

