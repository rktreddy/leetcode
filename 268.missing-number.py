#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    # def missingNumber(self, nums: List[int]) -> int:
    #     """ Approach #1 Sorting O(nlogn), O(1) or O(n) """
    #     nums.sort()

    #     # Ensure that n is at the last index
    #     if nums[-1] != len(nums):
    #         return len(nums)
    #     # Ensure that 0 is at the first index
    #     elif nums[0] != 0:
    #         return 0

    #     # If we get here, then the missing number is on the range (0, n)
    #     for i in range(1, len(nums)):
    #         expected_num = nums[i-1] + 1
    #         if nums[i] != expected_num:
    #             return expected_num
        
    # def missingNumber(self, nums: List[int]) -> int:
    #     """ Approach #2 HashSet [Accepted] O(n), O(n) """
    #     num_set = set(nums)
    #     n = len(nums) + 1
    #     for number in range(n):
    #         if number not in num_set:
    #             return number
            
    def missingNumber(self, nums: List[int]) -> int:
        """ Approach #3 Bit Manipulation O(n), O(1) """
        
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing
    

# @lc code=end

