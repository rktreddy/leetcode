#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """ Approach 1: Optimized Brute Force O(n^2) """
        # max_subarray_sum = -math.inf
        # for i in range(len(nums)):
        #     subarray_sum = nums[i]
        #     max_subarray_sum = max(max_subarray_sum, subarray_sum)
        #     for j in range(i + 1, len(nums)):
        #         subarray_sum += nums[j]
        #         max_subarray_sum = max(max_subarray_sum, subarray_sum)
        # return max_subarray_sum

        
        # """ Approach 2: Dynamic Programming, Kadane's Algorithm  O(N), O(1) """
        # if not nums:
        #     return 0
        
        # cum_sum = max_sum = nums[0]
        # for num in nums[1:]:
        #     cum_sum = max(num, cum_sum + num)
        #     max_sum = max(max_sum, cum_sum)
    
        # return max_sum

        """ practice: Approach 2: Dynamic Programming, Kadane's Algorithm  O(N), O(1) """
        if not nums:
            return 0
        cum_sum = max_sum = nums[0]
        for num in nums[1:]:
            cum_sum = max(num, cum_sum + num)
            max_sum = max(max_sum, cum_sum)
        return max_sum

        

    # def maxSubArray(self, nums: List[int]) -> int:
    #     """ Approach 3: Divide and Conquer (Advanced) O(N LogN), O(Log N)"""
    #     def findBestSubarray(nums, left, right):
    #         # Base case - empty array.
    #         if left > right:
    #             return -math.inf

    #         mid = (left + right) // 2
    #         curr = best_left_sum = best_right_sum = 0

    #         # Iterate from the middle to the beginning.
    #         for i in range(mid - 1, left - 1, -1):
    #             curr += nums[i]
    #             best_left_sum = max(best_left_sum, curr)

    #         # Reset curr and iterate from the middle to the end.
    #         curr = 0
    #         for i in range(mid + 1, right + 1):
    #             curr += nums[i]
    #             best_right_sum = max(best_right_sum, curr)

    #         # The best_combined_sum uses the middle element and
    #         # the best possible sum from each half.
    #         best_combined_sum = nums[mid] + best_left_sum + best_right_sum

    #         # Find the best subarray possible from both halves.
    #         left_half = findBestSubarray(nums, left, mid - 1)
    #         right_half = findBestSubarray(nums, mid + 1, right)

    #         # The largest of the 3 is the answer for any given input array.
    #         return max(best_combined_sum, left_half, right_half)

    #     # Our helper function is designed to solve this problem for
    #     # any array - so just call it using the entire input!
    #     return findBestSubarray(nums, 0, len(nums) - 1)
        
# @lc code=end

