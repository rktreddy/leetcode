#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#

# @lc code=start
class Solution:
    # def sortArray(self, nums: List[int]) -> List[int]:
    #     """ Approach 1: Merge Sort O(nlogn), O(n)"""
    #     temp_arr = [0] * len(nums)

    #     # Function to merge two sub-arrays in sorted order.
    #     def merge(left, mid, right):
    #         start1 = left
    #         start2 = mid + 1
    #         n1 = mid - left + 1
    #         n2 = right - mid

    #         # Copy elements of both halves into a temporary array.
    #         for i in range(n1):
    #             temp_arr[start1 + i] = nums[start1 + i]
    #         for i in range(n2):
    #             temp_arr[start2 + i] = nums[start2 + i]

    #         # Merge the sub-arrays 'in tempArray' back into the original 
    #         # array 'arr' in sorted order.
    #         i, j, k = 0, 0, left
    #         while i < n1 and j < n2:
    #             if temp_arr[start1 + i] <= temp_arr[start2 + j]:
    #                 nums[k] = temp_arr[start1 + i]
    #                 i += 1
    #             else:
    #                 nums[k] = temp_arr[start2 + j]
    #                 j += 1
    #             k += 1
            
    #         # Copy remaining elements
    #         while i < n1:
    #             nums[k] = temp_arr[start1 + i]
    #             i += 1
    #             k += 1

    #         while j < n2:
    #             nums[k] = temp_arr[start2 + j]
    #             j += 1
    #             k += 1

    #     # Recursive function to sort an array using merge sort
    #     def merge_sort(left, right):
    #         if left >= right:
    #             return
    #         mid = (left + right) // 2
    #         # Sort first and second halves recursively.
    #         merge_sort(left, mid)
    #         merge_sort(mid + 1, right)
    #         # Merge the sorted halves.
    #         merge(left, mid, right)

    #     merge_sort(0, len(nums) - 1)
    #     return nums 


    # def sortArray(self, nums: List[int]) -> List[int]:
    #     """ Approach 1: Heap Sort O(nlogn), O(logn)"""
    #     # Function to heapify a subtree (in top-down order) rooted at index i.
    #     def heapify(n: int, i: int):
    #         # Initialize largest as root 'i'.
    #         largest = i
    #         left = 2 * i + 1
    #         right = 2 * i + 2
    #         # If left child is larger than root.
    #         if left < n and nums[left] > nums[largest]:
    #             largest = left
    #         # If right child is larger than largest so far.
    #         if right < n and nums[right] > nums[largest]:
    #             largest = right
    #         # If largest is not root swap root with largest element
    #         # Recursively heapify the affected sub-tree (i.e. move down).
    #         if largest != i:
    #             nums[i], nums[largest] = nums[largest], nums[i]
    #             heapify(n, largest)

    #     def heap_sort():
    #         n = len(nums)
    #         # Build heap; heapify (top-down) all elements except leaf nodes.
    #         for i in range(n // 2 - 1, -1, -1):
    #             heapify(n, i)
    #         # Traverse elements one by one, to move current root to end, and
    #         for i in range(n - 1, -1, -1):
    #             nums[0], nums[i] = nums[i], nums[0]
    #             # call max heapify on the reduced heap.
    #             heapify(i, 0)

    #     heap_sort()
    #     return nums

    # def sortArray(self, nums: List[int]) -> List[int]:
    #     """ Approach 3: Counting Sort O(n + k), O(n) """
    #     def counting_sort():
    #         # Create the counting hash map.
    #         counts = {}
    #         # Find the minimum and maximum values in the array.
    #         minVal, maxVal = min(nums), max(nums)
    #         # Update element's count in the hash map.
    #         for val in nums:
    #             counts[val] = counts.get(val, 0) + 1

    #         index = 0
    #         # Place each element in its correct position in the array.
    #         for val in range(minVal, maxVal + 1, 1):
    #             # Append all 'val's together if they exist.
    #             while counts.get(val, 0) > 0:
    #                 nums[index] = val
    #                 index += 1
    #                 counts[val] -= 1

    #     counting_sort()
    #     return nums
    
    def sortArray(self, nums: List[int]) -> List[int]:
        """ Approach 4: Radix Sort O(n + k), O(n) """


# @lc code=end

