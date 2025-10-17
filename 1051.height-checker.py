#
# @lc app=leetcode id=1051 lang=python3
#
# [1051] Height Checker
#

# @lc code=start
class Solution:
    # def heightChecker(self, heights: List[int]) -> int:
    #     """ Approach 1: Bubble Sort O(n^2), O(n) """
    #     # Function to perform bubble sort on the input array.
    #     def bubble_sort():
    #         n = len(sorted_heights)
    #         # Loop through the array for bubble sort passes.
    #         for i in range(n - 1):
    #             # Inner loop to compare and swap elements.
    #             for j in range(n - i - 1):
    #                 # Compare and swap if elements are in the wrong order.
    #                 if sorted_heights[j] > sorted_heights[j + 1]:
    #                     sorted_heights[j], sorted_heights[j + 1] = (
    #                         sorted_heights[j + 1],
    #                         sorted_heights[j],
    #                     )

    #     # Sort the array using bubble sort.
    #     sorted_heights = heights[:]
    #     bubble_sort()

    #     count = 0
    #     # Loop through the original and sorted arrays.
    #     for i in range(len(sorted_heights)):
    #         # Increment count if elements at the same index differ.
    #         if heights[i] != sorted_heights[i]:
    #             count += 1
    #     # Return the total count of differing elements.
    #     return count
    
        
        
    # """ Approach 2: Merge Sort O(nlogn), O(n) """
    # # Function to merge two sub-arrays in sorted order.
    # def merge(self, arr, left, mid, right, temp_arr):
    #     # Calculate the start and sizes of two halves.
    #     start1 = left
    #     start2 = mid + 1
    #     n1 = mid - left + 1
    #     n2 = right - mid

    #     # Copy elements of both halves into a temporary array.
    #     for i in range(n1):
    #         temp_arr[start1 + i] = arr[start1 + i]
    #     for i in range(n2):
    #         temp_arr[start2 + i] = arr[start2 + i]

    #     # Merge the sub-arrays in 'temp_arr' back into the original array 'arr' in sorted order.
    #     i, j, k = 0, 0, left
    #     while i < n1 and j < n2:
    #         if temp_arr[start1 + i] <= temp_arr[start2 + j]:
    #             arr[k] = temp_arr[start1 + i]
    #             i += 1
    #         else:
    #             arr[k] = temp_arr[start2 + j]
    #             j += 1
    #         k += 1

    #     # Copy remaining elements
    #     while i < n1:
    #         arr[k] = temp_arr[start1 + i]
    #         i += 1
    #         k += 1
    #     while j < n2:
    #         arr[k] = temp_arr[start2 + j]
    #         j += 1
    #         k += 1

    # # Recursive function to sort an array using merge sort.
    # def merge_sort(self, arr, left, right, temp_arr):
    #     if left >= right:
    #         return
    #     mid = (left + right) // 2
    #     # Sort first and second halves recursively.
    #     self.merge_sort(arr, left, mid, temp_arr)
    #     self.merge_sort(arr, mid + 1, right, temp_arr)
    #     # Merge the sorted halves.
    #     self.merge(arr, left, mid, right, temp_arr)

    # def heightChecker(self, heights: List[int]) -> int:
    #     """ Approach 2: Merge Sort O(nlogn), O(n) """
    #     # Sort the array using merge sort.
    #     sorted_heights = heights[:]
    #     temp_arr = [0] * len(heights)
    #     self.merge_sort(sorted_heights, 0, len(sorted_heights) - 1, temp_arr)

    #     count = 0
    #     # Loop through the original and sorted arrays.
    #     for i in range(len(sorted_heights)):
    #         # Increment count if elements at the same index differ.
    #         if heights[i] != sorted_heights[i]:
    #             count += 1
    #     # Return the total count of differing elements.
    #     return count
    

    # """ Approach 3: Heap Sort O(nlogn), O(n) """
    # # Function to max heapify a subtree (in top-down order) rooted at index i.
    # def heapify(self, arr, n, i):
    #     # Initialize largest as root 'i'.
    #     largest, left, right = i, 2 * i + 1, 2 * i + 2

    #     # If the left child is larger than the root.
    #     if left < n and arr[left] > arr[largest]:
    #         largest = left

    #     # If the right child is larger than the largest so far.
    #     if right < n and arr[right] > arr[largest]:
    #         largest = right

    #     # If largest is not root swap root with the largest element
    #     # Recursively heapify the affected sub-tree (i.e. move down).
    #     if largest != i:
    #         arr[i], arr[largest] = arr[largest], arr[i]
    #         self.heapify(arr, n, largest)

    # def heap_sort(self, arr):
    #     n = len(arr)
    #     # Build heap; heapify all elements except leaf nodes, in bottom-up order.
    #     for i in range(n // 2 - 1, -1, -1):
    #         self.heapify(arr, n, i)

    #     # Traverse elements one by one, to move the current root to the end, and
    #     for i in range(n - 1, 0, -1):
    #         arr[0], arr[i] = arr[i], arr[0]
    #         # call max heapify on the reduced array.
    #         self.heapify(arr, i, 0)

    # def heightChecker(self, heights: List[int]) -> int:
    #     # Sort the array using heap sort.
    #     sorted_heights = heights[:]
    #     self.heap_sort(sorted_heights)

    #     count = 0
    #     # Loop through the original and sorted arrays.
    #     for i in range(len(sorted_heights)):
    #         # Increment count if elements at the same index differ.
    #         if heights[i] != sorted_heights[i]:
    #             count += 1
    #     # Return the total count of differing elements.
    #     return count

    # """ Approach 4: Counting Sort O(n + k), O(n) """
    # def counting_sort(self, arr):
    #     # Create the counting hash map.
    #     counts = {}
    #     # Find the minimum and maximum values in the array.
    #     min_val, max_val = min(arr), max(arr)

    #     # Update element's count in the hash map.
    #     for val in arr:
    #         if val in counts:
    #             counts[val] += 1
    #         else:
    #             counts[val] = 1

    #     index = 0
    #     # Place each element in its correct position in the array.
    #     for val in range(min_val, max_val + 1):
    #         # Append all 'val's together if they exist.
    #         while counts.get(val, 0) > 0:
    #             arr[index] = val
    #             index += 1
    #             counts[val] -= 1

    # def heightChecker(self, heights: List[int]) -> int:
    #     # Sort the array using counting sort.
    #     sorted_heights = heights[:]
    #     self.counting_sort(sorted_heights)

    #     count = 0
    #     # Loop through the original and sorted arrays.
    #     for i in range(len(sorted_heights)):
    #         # Increment count if elements at the same index differ.
    #         if heights[i] != sorted_heights[i]:
    #             count += 1
    #     # Return the total count of differing elements.
    #     return count
    
    """ Approach 5: Radix Sort O(d * (n+b)), O(n + b) """
    # Bucket sort function for each place value digit.
    def bucket_sort(self, arr, place_value):
        buckets = [[] for _ in range(10)]

        # Store the respective number based on its digit.
        for val in arr:
            digit = abs(val) // place_value
            digit = digit % 10
            buckets[digit].append(val)

        # Overwrite 'arr' in sorted order of current place digits.
        index = 0
        for digit in range(10):
            for val in buckets[digit]:
                arr[index] = val
                index += 1

    # Radix sort function.
    def radix_sort(self, arr):
        # Find the absolute maximum element to find max number of digits.
        max_element, max_digits = max(abs(val) for val in arr), 0
        while max_element > 0:
            max_digits += 1
            max_element //= 10

        # Radix sort, least significant digit place to most significant.
        place_value = 1
        for _ in range(max_digits):
            self.bucket_sort(arr, place_value)
            place_value *= 10

    def heightChecker(self, heights: List[int]) -> int:
        # Sort the array using radix sort.
        sorted_heights = heights[:]
        self.radix_sort(sorted_heights)

        count = 0
        # Loop through the original and sorted arrays.
        for i in range(len(sorted_heights)):
            # Increment count if elements at the same index differ.
            if heights[i] != sorted_heights[i]:
                count += 1
        # Return the total count of differing elements.
        return count


        
# @lc code=end

