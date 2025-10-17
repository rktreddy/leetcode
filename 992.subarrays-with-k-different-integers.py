#
# @lc app=leetcode id=992 lang=python3
#
# [992] Subarrays with K Different Integers
#

# @lc code=start
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        """ Approach 1: Sliding Window  O(n), O(n) """
        return self.slidingWindowAtMost(nums, k) - self.slidingWindowAtMost(nums, k - 1)

    # Helper function to count the number of subarrays with at most k distinct elements.
    def slidingWindowAtMost(self, nums: List[int], distinctK: int) -> int:
        # To store the occurrences of each element.
        freq_map = defaultdict(int)
        left = 0
        total_count  = 0

        # Right pointer of the sliding window iterates through the array.
        for right in range(len(nums)):
            freq_map[nums[right]] += 1

            # If the number of distinct elements in the window exceeds k,
            # we shrink the window from the left until we have at most k distinct elements.
            while len(freq_map) > distinctK:
                freq_map[nums[left]] -= 1
                if freq_map[nums[left]] == 0:
                    del freq_map[nums[left]]
                left += 1

            # Update the total count by adding the length of the current subarray.
            total_count  += right - left + 1

        return total_count 


# from collections import defaultdict
# from typing import List

# class Solution:
#     def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
#         """ chatgpt slidng window O(n), O(k) """
#         # Helper function to count subarrays with at most `k` distinct integers
#         def atMostKDistinct(k):
#             count = defaultdict(int)
#             left = 0
#             res = 0
#             for right in range(len(nums)):
#                 if count[nums[right]] == 0:
#                     k -= 1
#                 count[nums[right]] += 1
                
#                 while k < 0:
#                     count[nums[left]] -= 1
#                     if count[nums[left]] == 0:
#                         k += 1
#                     left += 1
                
#                 # Number of subarrays ending at `right` with at most `k` distinct integers
#                 res += right - left + 1
#             return res
        
#         # The result is the difference between subarrays with at most `k` and at most `k - 1` distinct integers
#         return atMostKDistinct(k) - atMostKDistinct(k - 1)

        
# @lc code=end

