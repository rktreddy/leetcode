#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution:
    # def maxProduct(self, nums: List[int]) -> int:
    #     """ Approach 1: Brute Force O(N^2), O(1) """
    #     if len(nums) == 0:
    #         return 0

    #     result = nums[0]

    #     for i in range(len(nums)):
    #         accu = 1
    #         for j in range(i, len(nums)):
    #             accu *= nums[j]
    #             result = max(result, accu)

    #     return result
    
    def maxProduct(self, nums: List[int]) -> int:
        """ Approach 2: Dynamic Programming O(N), O(1) """
        if len(nums) == 0:
            return nums[0]
        
        max_prod = nums[0]
        min_prod = nums[0]
        result = max_prod

        for num in nums[1:]:
            curr_prod = max(num, max_prod * num, min_prod * num)
            min_prod = min(num, max_prod * num, min_prod * num)
            max_prod = curr_prod

            result = max(result, max_prod)

        return result
        
# @lc code=end

